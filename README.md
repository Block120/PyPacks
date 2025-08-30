![](logo/logo.png)
### An API for Minecraft: Bedrock Edition and Minecraft: Java Edition written in Python
## Installation
To install PyPacks it is recommended to create a virtual environment first

### Windows

```sh
python -m venv .venv
```

Once the virtual environment is created then activate it

```sh
.venv\\Scripts\\activate.bat
```

### MacOS

```sh
python3 -m venv .venv
```

Once the virtual environment is created then activate it

```sh
source .venv/bin/activate
```

### Before you can use PyPacks you need to install it

```sh
pip install pypacks
```

## Usage
Here is an example of usage for PyPacks:
```python
import math

def example:circle:
    for radius in range(100):
        angle = 2 * math.pi * radius / 100
        x = radius * math.sin(angle)
        z = radius * math.cos(angle)
        particle flame ~x ~ ~z

```
To build this run this command:
```sh
pypacks example.pxs
```
This will detect what versions of minecraft are installed and build it for those versions
