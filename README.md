# Build source Python into An executable file
## Environment
OS: Ubuntu - Linux Kernel<br>
Python version: 3.8.5<br>
## Install library
```
pip3 install pyinstaller
```
## Compile
Enter to source directory.
```
cd ~/build_executable_file
```

Run this command:
```
python3 -m PyInstaller <main_file>.py --onefile -n <name_release>
```

Example:
```
python3 -m PyInstaller test.py --onefile -n run

```

Build destination is <b>dist</b> directory

## Test
```
cd dist
./run
```

Expect output:
```
||===================||
||   Hello python3   ||
||===================||
9328-5734j
```
