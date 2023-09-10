# gapic-python-basic
Set of Python Code Generation tools & templates for Human beings.

Support:
- [x] Simple Dataclass


# Templates
## Python Types (@dataclass)
This template generates basic Python Dataclasses from Proto Messages.

<details>
    <summary>Buf Configuration</summary>


```yaml
# ./proto/buf.gen.yaml
version: v1
managed:
  enabled: true
  go_package_prefix:
    default: github.com/fraser-isbester/gapic-python-basic/examples/simple-types
plugins:
  - plugin: python_gapic
    out: ../gen/python
    opt:
      - python-gapic-templates=/Users/fraser/code/gapic-python-basic/templates/dataclasses

```

```yaml
# ./proto/buf.yaml
version: v1
name: buf.build/fraser/simple-types
breaking:
  use:
    - FILE
lint:
  use:
    - DEFAULT
    - COMMENTS
```

</details>

<details>
    <summary>Proto Definition</summary>

```protobuf
// examples/simple-types/proto/widgets/v1/widgets.proto
// A proto file for the Widget service
syntax = "proto3";

package simple_types.v1 ;

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
    // global stock by color
    map<string, int32> stock_by_color = 5;
    // The number of widgets in stock at various locations
    map<int32, WidgetFactory> stock_by_warehouse = 6;

    // The Size enum defines the size of the widget
    enum Size {
        // The Widget Size is unknown
        SIZE_UNSPECIFIED = 0;
        // The Widget Size is small
        SIZE_SMALL = 1;
        // The Widget Size is medium
        SIZE_MEDIUM = 2;
        // The Widget Size is large
        SIZE_LARGE = 3;
    }
}

// Describes a Widget Factory
message WidgetFactory {
	// The id of the factory
	int32 id = 1 ;
	// The name of the factory
	string name = 2 ;
	// The address of the factory
	string address = 3 ;
}
```
</details>

<details>
    <summary>Generated Python Class</summary>

```python
# examples/simple-types/gen/simple_types_v1/types/widgets.py
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

    # The name of the widget.
    name: str

    # The size of the widget.
    size: "Size"

    # The date the widget was created.
    created: int

    # The colors available for the widget.
    colors: Tuple[str] = dataclasses.field(default_factory=Tuple)

    # global stock by color.
    stock_by_color: OrderedDict[str, int] = dataclasses.field(default_factory=Tuple)

    # The number of widgets in stock at various locations.
    stock_by_warehouse: OrderedDict[int, "WidgetFactory"] = dataclasses.field(
        default_factory=Tuple
    )

    class Size(Enum):
        r"""The Size enum defines the size of the widget"""

        # The Widget Size is unknown
        SIZE_UNSPECIFIED = 0
        # The Widget Size is small
        SIZE_SMALL = 1
        # The Widget Size is medium
        SIZE_MEDIUM = 2
        # The Widget Size is large
        SIZE_LARGE = 3


@dataclasses.dataclasses
class WidgetFactory:
    r"""Describes a Widget Factory"""

    # The fixed set of attrbiutes for the WidgetFactory Type.
    __slots__ = ("id", "name", "address")

    # The id of the factory.
    id: int

    # The name of the factory.
    name: str

    # The address of the factory.
    address: str

```
</details>


# References
- [Gapic Generator Python Documentation](https://gapic-generator-python.readthedocs.io/en/stable/index.html)
- [Google API Improvement Proposals](https://google.aip.dev/)
- [GAPIC Showcase](https://github.com/googleapis/gapic-showcase)
