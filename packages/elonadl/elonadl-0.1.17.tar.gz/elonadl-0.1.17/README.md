# ElonaPlusCustom-GX Installer script for Windows

A Installer to download and setup ElonaPlusCustom-GX on Windows.

New Repo: **[JianmengYu](https://github.com/JianmengYu/ElonaPlusCustom-GX)** Current Repo based.

Please visit **[Ruin0x11](https://github.com/Ruin0x11/ElonaPlusCustom-GX)**'s Previous Archived Repo

# Version:
Game Version: **Elona+ 2.25R**<br>
Custom-GX Version: **2.25.1.1**<br>

# How to Install:

(Make sure you have **_Python3.10_** or higher prior)

Just go to the _dist_ folder and download the package.

Go to the folder you downloaded the package to and install it with the following command.

## Installation:
```
pip install elonadl

python elonadl
```
## Install stragiht from .whl or tar.gz packages
```
pip install elonadl-<VERSION>-py3-none-any.whl
```

or

```
py -m pip install elonadl-<VERSION>.tar.gz
```

To run the module just run the following command. _**Whenever there is a new update for Custom-GX simply rerun this command and it'll update your installation.**_

```
py -m elonadl
```

The game will be setup in your **%APPDATA%** folder.
The script will inform you of the steps in the command line.

# How to Remove Package.

This won't impact the Elona+CGX setup, just remove the elonadl package from your computer.

```
pip uninstall elonadl
```

or

```
py -m pip uninstall elonadl
```

# In case there are new releases:

If you see a newer release to a newer version of Elona+ just rerun `py -m elonadl` it'll automatically create a new install for the latest version and not touch your older install.

# To Create a new Build

```
py setup.py bdist_wheel # .whl

or

py setup.py sdist # .tar.gz
```

_Make sure in have `wheel` package installed on your system prior to building_
Make sure to alter the attributes in **setup.py**
