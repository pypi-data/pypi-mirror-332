from setuptools import setup, find_packages

setup(
    name="airoframework",
    version="0.1.3",
    packages=find_packages(),
    include_package_data=True,  
    install_requires=[],
    entry_points={
        "console_scripts": [
            "airoframework=airoframework.cli:create_project",
        ],
    },
)
