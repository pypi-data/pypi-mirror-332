# jsoncreatoor

A library for working with JSON files.

## Installation

```bash
pip install jsoncreatoor
```

# How does the library work?
It's quite simple.

First, we need an empty space with one Python file. After that, we write the code:
```python
import jsoncreatoor
# or for specific parts
from jsoncreatoor import example_json, create_json, json_config
```

Once we import the library, we have access to three functions: `example_json`, `create_json`, and `json_config`.

# Main functionality of the library

`example_json` - creates a file named `data.json` with the following content:
```json
{
    "Example_code": true,
    "Example": false,
    "data": 1,
    "Local": 0
}
```

`create_json` - creates a file with data provided by the user. For example:
```python
from jsoncreatoor import create_json

# Example JSON data
data = {
    "Example_code": true,
    "Example": false,
    "data": 1,
    "Local": 0
}

create_json(data, "file_name", '')  # data uses the variable containing your code
# file_name - you don't need to write file_name.json, just the name; otherwise, it will be file_name.json.json
# directory - if you leave it empty, the file will be created in the same folder as your script
```

`json_config` - creates or overwrites an already existing file. If the file does not exist, it will be created. Example:
```python
from jsoncreatoor import json_config

# Example JSON data
data = {
    "Example_code": true,
    "Example": false,
    "data": 1,
    "Local": 0
}

json_config(data, "file_name", '')  # similar to create_json
```

Good luck!