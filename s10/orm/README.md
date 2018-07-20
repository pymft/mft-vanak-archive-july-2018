f## STEPS
1. create a virtualenv, if you have't `virtualenv` installed on your computer
use this command:
```bash
 pip install virtualenv
```
2. create a directory to keep all things together. Then navigate to that directory and create your enviornment

```bash
$ mkdir orm-venv
$ cd orm-venv
$ virtualenv orm
```

3. activate env

for linux
```bash
$ source ./orm/bin/activate 
```

and for windows
```bash
$ ./orm/Scripts/activate.bat
```
you'll see the name of env shows up in the beginning of line 

```bash
(orm) $ pip install SQLAlchemy
```