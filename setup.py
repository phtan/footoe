from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    
requirements = []

setup(
    name = "footoe-by-phtan",
    version = "0.0.1",
    author = "Pheng Heong Tan",
    author_email = "phtan90@gmail.com"
    description = "A package to ease writing and maintaining 
        foot-notes",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/phtan/footoe",
    packages = find_packages(),
    install_requires = requirements
    classifiers = [
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)
    
    
    