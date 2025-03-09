# setup.py
from setuptools import setup, find_packages
import os

# Read the long description from the README file.
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="soc_monitor",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "psutil",
        "speedtest-cli",
    ],
    entry_points={
        "console_scripts": [
            "soc-monitor=soc_monitor.cli:main",
        ],
    },
    description="A comprehensive system monitoring tool powered by FastAPI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Shreyas H S",
    author_email="s09082003@gmail.com",
    url="https://github.com/Shreyashs98/soc-monitor",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Framework :: FastAPI",
    ],
    keywords="system monitoring fastapi uvicorn psutil speedtest-cli",
)
