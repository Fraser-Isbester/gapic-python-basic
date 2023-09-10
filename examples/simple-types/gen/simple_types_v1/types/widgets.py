# -*- coding: utf-8 -*-

import dataclasses
from typing import Tuple
from typing import OrderedDict
from enum import Enum


@dataclasses.dataclasses
class Widget:
    r"""The Widget type defines a Widget object"""

    # The fixed set of attrbiutes for the Widget Type.
    __slots__ = (
        "name",
        "size",
        "created",
        "colors",
        "stock_by_color",
        "stock_by_warehouse",
    )

    # The name of the widget
    name: str

    # The size of the widget
    size: "Size"

    # The date the widget was created
    created: int

    # The colors available for the widget
    colors: Tuple[str] = dataclasses.field(default_factory=Tuple)

    # global stock by color
    stock_by_color: OrderedDict[str, int] = dataclasses.field(default_factory=Tuple)

    # The number of widgets in stock at various locations
    stock_by_warehouse: OrderedDict[int, "WidgetFactory"] = dataclasses.field(
        default_factory=Tuple
    )

    class Size(Enum):
        r"""The Size enum defines the size of the widget"""

        # The Widget Size is unknown
        UNKNOWN = 0
        # The Widget Size is small
        SMALL = 1
        # The Widget Size is medium
        MEDIUM = 2
        # The Widget Size is large
        LARGE = 3


@dataclasses.dataclasses
class WidgetFactory:
    r"""Describes a Widget Factory"""

    # The fixed set of attrbiutes for the WidgetFactory Type.
    __slots__ = ("id", "name", "address")

    # The id of the factory
    id: int

    # The name of the factory
    name: str

    # The address of the factory
    address: str


__all__ = tuple(sorted(__protobuf__.manifest))
