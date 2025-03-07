# setup.py
from setuptools import setup, find_packages

setup(
    name="soc_monitor",
    version="0.1.0",
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
    description="A system monitoring tool with FastAPI backend.",
    author="Shreyas H S",
    author_email="s09082003@gmail.com",
    url="https://github.com/Shreyashs98/soc-monitor",
)