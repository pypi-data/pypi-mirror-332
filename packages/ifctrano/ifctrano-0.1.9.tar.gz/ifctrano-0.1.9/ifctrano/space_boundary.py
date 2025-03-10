import multiprocessing
import re
from typing import Optional, List, Tuple, Any

import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.shape
from ifcopenshell import entity_instance, file
from pydantic import BaseModel, Field
from trano.data_models.conversion import SpaceParameter  # type: ignore
from trano.elements import Space as TranoSpace, ExternalWall, Window, BaseWall, ExternalDoor  # type: ignore
from trano.elements.construction import (  # type: ignore
    Construction,
    Layer,
    Material,
    Glass,
    GlassLayer,
    GasLayer,
    GlassMaterial,
    Gas,
)
from trano.elements.system import Occupancy  # type: ignore
from trano.elements.types import Tilt  # type: ignore

from ifctrano.base import (
    GlobalId,
    settings,
    BaseModelConfig,
    CommonSurface,
    ROUNDING_FACTOR,
    CLASH_CLEARANCE,
    Vector,
)
from ifctrano.bounding_box import OrientedBoundingBox


def initialize_tree(ifc_file: file) -> ifcopenshell.geom.tree:
    tree = ifcopenshell.geom.tree()

    iterator = ifcopenshell.geom.iterator(
        settings, ifc_file, multiprocessing.cpu_count()
    )
    if iterator.initialize():  # type: ignore
        while True:
            tree.add_element(iterator.get())  # type: ignore
            if not iterator.next():  # type: ignore
                break
    return tree


def remove_non_alphanumeric(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]", "", text).lower()


class Space(GlobalId):
    name: Optional[str] = None
    bounding_box: OrientedBoundingBox
    entity: entity_instance
    average_room_height: float
    floor_area: float
    bounding_box_height: float
    bounding_box_volume: float

    @classmethod
    def from_entity(cls, entity: entity_instance) -> "Space":
        bounding_box = OrientedBoundingBox.from_entity(entity)
        entity_shape = ifcopenshell.geom.create_shape(settings, entity)
        area = ifcopenshell.util.shape.get_footprint_area(entity_shape.geometry)  # type: ignore
        volume = ifcopenshell.util.shape.get_volume(entity_shape.geometry)  # type: ignore
        if area:
            average_room_height = volume / area
        else:
            area = bounding_box.volume / bounding_box.height
            average_room_height = bounding_box.height
        return cls(
            global_id=entity.GlobalId,
            name=entity.Name,
            bounding_box=bounding_box,
            entity=entity,
            average_room_height=average_room_height,
            floor_area=area,
            bounding_box_height=bounding_box.height,
            bounding_box_volume=bounding_box.volume,
        )

    def check_volume(self) -> bool:
        return round(self.bounding_box_volume, ROUNDING_FACTOR) == round(
            self.floor_area * self.average_room_height, ROUNDING_FACTOR
        )

    def space_name(self) -> str:
        main_name = f"{remove_non_alphanumeric(self.name)}_" if self.name else ""
        return f"space_{main_name}{remove_non_alphanumeric(self.entity.GlobalId)}"


material_1 = Material(
    name="material_1",
    thermal_conductivity=0.046,
    specific_heat_capacity=940,
    density=80,
)
construction = Construction(
    name="construction_4",
    layers=[
        Layer(material=material_1, thickness=0.18),
    ],
)
id_100 = GlassMaterial(
    name="id_100",
    thermal_conductivity=1,
    density=2500,
    specific_heat_capacity=840,
    solar_transmittance=[0.646],
    solar_reflectance_outside_facing=[0.062],
    solar_reflectance_room_facing=[0.063],
    infrared_transmissivity=0,
    infrared_absorptivity_outside_facing=0.84,
    infrared_absorptivity_room_facing=0.84,
)

air = Gas(
    name="Air",
    thermal_conductivity=0.025,
    density=1.2,
    specific_heat_capacity=1005,
)
glass = Glass(
    name="double_glazing",
    u_value_frame=1.4,
    layers=[
        GlassLayer(thickness=0.003, material=id_100),
        GasLayer(thickness=0.0127, material=air),
        GlassLayer(thickness=0.003, material=id_100),
    ],
)


class SpaceBoundary(BaseModelConfig):
    bounding_box: OrientedBoundingBox
    entity: entity_instance
    common_surface: CommonSurface
    adjacent_spaces: List[Space] = Field(default_factory=list)

    def boundary_name(self) -> str:
        return f"{self.entity.is_a()}_{remove_non_alphanumeric(self.entity.GlobalId)}"

    def model_element(
        self, exclude_entities: List[str], north_axis: Vector
    ) -> Optional[BaseWall]:
        if self.entity.GlobalId in exclude_entities:
            return None
        azimuth = self.common_surface.orientation.angle(north_axis)
        if "wall" in self.entity.is_a().lower():
            return ExternalWall(
                name=self.boundary_name(),
                surface=self.common_surface.area,
                azimuth=azimuth,
                tilt=Tilt.wall,
                construction=construction,
            )
        if "door" in self.entity.is_a().lower():
            return ExternalDoor(
                name=self.boundary_name(),
                surface=self.common_surface.area,
                azimuth=azimuth,
                tilt=Tilt.wall,
                construction=construction,
            )
        if "window" in self.entity.is_a().lower():
            return Window(
                name=self.boundary_name(),
                surface=self.common_surface.area,
                azimuth=azimuth,
                tilt=Tilt.wall,
                construction=glass,
            )
        if "roof" in self.entity.is_a().lower():
            return ExternalWall(
                name=self.boundary_name(),
                surface=self.common_surface.area,
                azimuth=azimuth,
                tilt=Tilt.ceiling,
                construction=construction,
            )

        return None

    @classmethod
    def from_space_and_element(
        cls, bounding_box: OrientedBoundingBox, entity: entity_instance
    ) -> Optional["SpaceBoundary"]:
        bounding_box_ = OrientedBoundingBox.from_entity(entity)
        common_surface = bounding_box.intersect_faces(bounding_box_)
        if common_surface:
            return cls(
                bounding_box=bounding_box_, entity=entity, common_surface=common_surface
            )
        return None

    def description(self) -> Tuple[float, Tuple[float, ...], Any, str]:
        return (
            self.common_surface.area,
            self.common_surface.orientation.to_tuple(),
            self.entity.GlobalId,
            self.entity.is_a(),
        )


class SpaceBoundaries(BaseModel):
    space: Space
    boundaries: List[SpaceBoundary] = Field(default_factory=list)

    def model(
        self, exclude_entities: List[str], north_axis: Vector
    ) -> Optional[TranoSpace]:
        external_boundaries = [
            boundary.model_element(exclude_entities, north_axis)
            for boundary in self.boundaries
            if boundary.model_element(exclude_entities, north_axis)
        ]
        if not external_boundaries:
            return None
        return TranoSpace(
            name=self.space.space_name(),
            occupancy=Occupancy(),
            parameters=SpaceParameter(
                floor_area=self.space.floor_area,
                average_room_height=self.space.average_room_height,
            ),
            external_boundaries=external_boundaries,
        )

    @classmethod
    def from_space_entity(
        cls,
        ifcopenshell_file: file,
        tree: ifcopenshell.geom.tree,
        space: entity_instance,
    ) -> "SpaceBoundaries":
        space_ = Space.from_entity(space)
        clashes = tree.clash_clearance_many(
            [space],
            ifcopenshell_file.by_type("IfcWall")
            + ifcopenshell_file.by_type("IfcSlab")
            + ifcopenshell_file.by_type("IfcRoof")
            + ifcopenshell_file.by_type("IfcDoor")
            + ifcopenshell_file.by_type("IfcWindow"),
            clearance=CLASH_CLEARANCE,
        )
        space_boundaries = []

        for clash in clashes:
            elements = [
                ifcopenshell_file.by_guid(clash.a.get_argument(0)),
                ifcopenshell_file.by_guid(clash.b.get_argument(0)),
            ]
            for element in elements:
                if element.GlobalId == space.GlobalId:
                    continue
                space_boundary = SpaceBoundary.from_space_and_element(
                    space_.bounding_box, element
                )
                if space_boundary:
                    space_boundaries.append(space_boundary)
        return cls(space=space_, boundaries=space_boundaries)
