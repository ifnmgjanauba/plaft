# Plaft

Simple tool for automating the correction of programming language exercises

## Installation

First make sure you have Python 3.6 or higher installed. You can download Python [here](https://www.python.org/downloads/).

To install plaft under Linux / OS X:

```
pip install plaft
```

Under Windows, please [install the Linux subsystem](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Then install plaft within the subsystem.

## Usage

For example, the directory that contains all the student code files directories, look like this:

```
+ Tests
|-+ student1
    |-- ex01.py
    |-- ex02.py
|-+ student2
    |-- ex01.py
    |-- ex02.py
```

To check of students code files, run plaft like so:

```
plaft -a "/tests" -c "tests.yaml"
```