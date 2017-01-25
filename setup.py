from setuptools import setup, find_packages
from os.path import dirname, realpath, join


CURRENT_DIR = dirname(realpath(__file__))

with open(join(CURRENT_DIR, "README.rst")) as long_description_file:
    long_description = long_description_file.read()

setup(
    name="bearychat",
    version="0.2.0",
    author="bearyinnovative",
    url="https://github.com/bearyinnovative/bearychat.py",
    description="SDK for BearyChat",
    long_description=long_description,
    packages=find_packages(exclude=["docs"]),
    platforms="any",
    install_requires=[
        "requests>=2.2.1",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ]
)
