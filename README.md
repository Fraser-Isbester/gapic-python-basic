# gapic-python-basic
Set of Python Code Generation tools & templates for Human beings.

Support:
- [x] Simple Dataclass


# Templates
## Python Types (@dataclass)
This template generates basic Python Dataclasses from Proto Messages.

<details>
    <summary>Proto Definition</summary>

```protobuf
// examples/simple-types/proto/widgets/v1/widgets.proto
// A proto file for the Widget service
syntax = "proto3";

package simple_types.v1.widget;

// The Widget type defines a Widget object
message Widget {
    // The name of the widget
    string name = 1;
    // The size of the widget
    Size size = 2;
    // The date the widget was created
    int64 created = 3;
    // The colors available for the widget
    repeated string colors = 4;
    // The number of widgets in stock at various locations
    map<string, int32> stock_by_warehouse = 5;

    // The Size enum defines the size of the widget
    enum Size {
        // The Widget Size is unknown
        UNKNOWN = 0;
        // The Widget Size is small
        SMALL = 1;
        // The Widget Size is medium
        MEDIUM = 2;
        // The Widget Size is large
        LARGE = 3;
    }
}
```
</details>

<details>
    <summary>Generated Python Class</summary>

```python
# examples/simple-types/gen/simple_types_v1/types/widgets.py
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import Tuple
from collections import OrderedDict
from enum import Enum


@dataclass
class Widget:
    r"""The Widget type defines a Widget object"""

    # The name of the widget
    name: str
    # The size of the widget
    size: "Size"
    # When the widget entry was created
    created: int
    # The colors the widget is available in
    colors: Tuple[str] = field(default_factory=Tuple)
    # The stock of the widget by warehouse
    stock_by_warehouse: OrderedDict[str, int] = field(default_factory=OrderedDict)

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

```
</details>


# References
- [Gapic Generator Python Documentation](https://gapic-generator-python.readthedocs.io/en/stable/index.html)
- [Google API Improvement Proposals](https://google.aip.dev/)
- [GAPIC Showcase](https://github.com/googleapis/gapic-showcase)
