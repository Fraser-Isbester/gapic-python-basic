import dataclasses
import datetime
from typing import Tuple
from enum import Enum, auto


@dataclasses.dataclass
class Widget:
    """The Widget type defines a Widget object
    
    # usage
    ```python
    from simple_types_v1.types import Widget

    def main():
        widget = Widget(
            "Toaster",
            Widget.Size.SMALL,
            datetime.date(2020, 1, 1),
            ("red", "blue")
        )
        print(widget.name)
    ```
    """

    # The name of the widget
    name: "str"
    # The size of the widget
    size: "Size"
    # The date the widget was created
    created: "datetime.date"
    # The colors available for the widget
    color: "Tuple[str]"

    class Size(Enum):
        """The WidgetSize enum defines the size of the widget"""

        # The widget size is unknown
        UNKNOWN = auto()
        # The widget is small
        SMALL = auto()
        # The widget is medium
        MEDIUM = auto()
        # The widget is large
        LARGE = auto()
