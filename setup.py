if __import__("os").name == "nt":
    raise RuntimeError("plaft does not support Windows directly. Instead, you should install the Windows Subsystem for Linux (https://docs.microsoft.com/en-us/windows/wsl/install-win10) and then install plaft within that.")

from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README    

setup(
    name='plaft',
    version='0.0.1',
    description='Simple tool for automating the correction of programming language exercises',
    long_description=readme(),
    long_description_content_type= 'text/markdown',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Utilities"
    ],
    author='IFNMG Campus Avançado de Janaúba',
    author_email='cezarfelipe@gmail.com',
    url='https://github.com/ifnmgjanauba/plaft',
    license='GPLv3',
    install_requires=['click','pyyaml','pexpect'],
    packages=["plaft"],
    include_package_data=True
    python_requires=">= 3.6",
    entry_points={
        "console_scripts": ["plaft=plaft.__main__:main"]
    },
)