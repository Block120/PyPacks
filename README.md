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
import pypacks

@pypacks.mcfunction("example:greet")
def greet():
    "Say 'Hello, World!' in the game chat."
    pypacks.say("Hello, World!")

```
To build this run this command:
```sh
python example.py
```
This will detect what versions of minecraft are installed and build it for those versions
