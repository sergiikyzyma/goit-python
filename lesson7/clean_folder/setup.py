from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version="1.0.0",
    author="teosoph",
    entry_points={"console_scripts": ["clean-folder=clean_folder.__main__:main"]},
    packages=find_packages(),
    include_package_data=True,
    description="This script will be sorting and cleaning the destinationsfolder",
    license="MIT License",
)
