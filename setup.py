from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["", "", ""]
setup(
    name="ReapeaterMap",
    version="0.0.1",
    author="Adam Bird, Ryan Lynar, Aaron Macdonald",
    author_email="RepeaterMapDevs@gmail.com",
    description="Open source database and map of repeaters located in Canada",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github/birda14/repeatermap",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=["Programming language :: Python ::3.8",
                 "License :: ::"],

)
