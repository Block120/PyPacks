![](logo/logo.png)
### An API for Minecraft: Bedrock Edition and Minecraft: Java Edition written in Python
## Installation
### Windows
To install PyPacks it is recommended to create a virtual environment first
```sh
python -m venv .venv
```
Once the virtual environment is created then activate it
```sh
.venv\\Scripts\\activate.bat
```
Finally, you can install PyPacks
```sh
pip install pypacks
```
## Usage
Here is an example of usage for PyPacks
```python
import pypacks

# Create the PyPack
example = pypacks.PyPack("example", "Example Pack")

# Define a function in the PyPack that says "Hello World!"
hello = pypacks.Function("hello")
hello.add_command("say", "Hello")
hello.add_command("say", "World!")
hello.attach(example)

# Define another function in the PyPack
yello = pypacks.Function("yello")
yello.attach(example)

# Build the PyPack for Bedrock and Java
example.build(pypacks.PyPackType.JAVA, "Example")
example.build(pypacks.PyPackType.BEDROCK, "Example")

```

### MacOS
To install PyPacks it is recommended to create a virtual environment first
```sh
python -m venv .venv
```
Once the virtual environment is created then activate it
```sh
source venv/bin/activate
```
Finally, you can install PyPacks
```sh
pip install pypacks
```
## Usage
Here is an example of usage for PyPacks
```python
import pypacks

# Create the PyPack
example = pypacks.PyPack("example", "Example Pack")

# Define a function in the PyPack that says "Hello World!"
hello = pypacks.Function("hello")
hello.add_command("say", "Hello")
hello.add_command("say", "World!")
hello.attach(example)

# Define another function in the PyPack
yello = pypacks.Function("yello")
yello.attach(example)

# Build the PyPack for Bedrock and Java
example.build(pypacks.PyPackType.JAVA, "Example")

# Since MacOS can't run bedrock, no option for it.
#Sorry!

```
