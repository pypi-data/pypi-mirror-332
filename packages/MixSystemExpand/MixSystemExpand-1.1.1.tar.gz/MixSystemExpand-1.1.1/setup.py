from setuptools import setup, find_packages
 
from pkg_resources import parse_requirements

text=''
with open("readme.md","r") as file:
    text=file.read()
 
setup(
    name="MixSystemExpand",
    version="1.1.1",
    author="WIN12_ZDY",
    author_email="win12zdy@163.com",
    description="systemapi",
    long_description=text,
    long_description_content_type="text/markdown",
    license="Apache License, Version 2.0",
    url="https://www.github.com/SYSTEM-WIN12-ZDY/PythonPackageOSAPI",
 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    
    include_package_data=True, # 一般不需要
    packages=find_packages(),
    python_requires=">=3.10",
    entry_points={
        'console_scripts': [
            'test = test.help:main'
        ]
    }
)