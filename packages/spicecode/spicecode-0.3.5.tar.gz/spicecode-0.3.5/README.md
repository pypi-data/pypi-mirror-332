# 🌶️ SpiceCode CLI - Making your code spicier 🔥🥵


### Installing via PIP
- Make sure you have Python installed on your system
- Open the terminal
- Install SpiceCode via PIP with:
```
pip install spicecode
```

### Using SpiceCode
- After installing via PIP, you can run these three commands: *(replace file with the filename)*
```
spice hello
```
```
spice translate
```
```
spice analyze FILE
```
- EXAMPLE: 
```
spice analyze code.js
```


---

### Supported Programming Langagues for Analysis:
[![My Skills](https://skillicons.dev/icons?i=python,js,java,ruby,lua&perline=5)](https://skillicons.dev)

- Python **(.py)**
- JavaScript **(.js)**
- Java **(.java)**
- Ruby **(.rb)**
- Lua **(.lua)**
- Many more **coming soon!**


### EXCEPTION:
If you are using the development build, only Ruby and Python are supported. since the dev build is using our own in-house parser, while the published pip package is using tree-sitter's open source parser with multi langague support, which is coming soon for our parser


---

You can also **visit our page on the pypi registry**: https://pypi.org/project/spicecode/

---


### For Development
i will write a better tutorial later but for now basically just:
- clone the repo yeah no shit
- create a python virtual enviroment with venv
- install the requirements.txt with ```pip install -r requirements.txt``` (not sure about this one but probably works)
- install the package locally with ```pip install -e . ```
- then run it using ```spice analyze``` followed by the file to be analyzed
- example: ```spice analyze example.js```
- you can also run ```spice hello``` for a hello idk
- idk if whats written above still works but for now, to run locally, im using this -> ```python -m cli.main``` followed by the command like hello or analyze

-----
we also have a pip package now:       
https://pypi.org/project/spicecode/     
or     
```pip install spicecode```     

