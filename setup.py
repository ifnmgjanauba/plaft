if __import__("os").name == "nt":
    raise RuntimeError("plaft does not support Windows directly. Instead, you should install the Windows Subsystem for Linux (https://docs.microsoft.com/en-us/windows/wsl/install-win10) and then install plaft within that.")

from setuptools import setup

setup(
    name='plaft',
    version='0.0.1',
    description='Simple tool for automating the correction of programming language exercises',
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Utilities"
    ],
    author='IFNMG Campus Janaúba',
    author_email='cezarfelipe@gmail.com',
    url='https://github.com/ifnmgjanauba/plaft',
    license='GPLv3',
    platforms='ALL',
    install_requires=['click','pyyaml','pexpect'],
    packages=["plaft"],
    python_requires=">= 3.6",
    entry_points={
        "console_scripts": ["plaft=plaft.__main__:main"]
    },
    include_package_data=True
)