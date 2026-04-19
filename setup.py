from setuptools import setup, find_packages

setup(
    name="task-cli",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "task-cli=core.main:main",
        ],
    },
)