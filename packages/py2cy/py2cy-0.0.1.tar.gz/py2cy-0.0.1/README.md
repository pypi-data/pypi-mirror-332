# 🗂️ py2cy 

*py2cy is a library designed to convert Python source code into Cython format, enabling the transformation of .py files into .so files on Linux and .pyd files on Windows. Additionally, it aids in obfuscating the code, making reverse engineering more challenging.*

## 🏃 Quickstart

Installing the package

```python
pip install py2cy
```	

Arrange the configuration file setup.cfg for your projects

```config
######CYTHON CONFIGURATIONS######
#threads for cythonize in linux
[NThreads]
nThreads=4

#path of the folder to be obfuscated
[SourcePath]
pkg_for_obfuscation=<<path of the project to be obfuscated>>

#files to be excluded from cythonization, comma separated values, must have file extension
[FilesToExclude]
files_to_exclude=abc.py,bde.py

#comma separated values
[PkgsToExclude]
pkgs_to_exclude=package1,package2

#If this is set, both exclude conditions metioned above will be ignored,#comma separated values
[FilesToInclude]
files_to_include=test1.py,test2.py

#If this is set, both exclude conditions above will be ignored,#comma separated values
[PkgsToInclude]
pkgs_to_include=
###############################
```

## ▶️ Execute

After the above configuration invoke py2cy in the command line interface as below

```python

py2cy <<path of the setup.cfg>>

or

py2cy #invoke from the current working directory where setup.cfg is present
```

Once the execution gets completed, a package with same name suffixed with _cython gets generated next to the actual source code.

Based on the configuration set in setup.cfg, respective files are cythonized.
