import setuptools

with open("README.md", "r") as file_handle:
    long_description = file_handle.read()

setuptools.setup(
        name='graphtool',
        version='0.1.0',
        author="Guillaume Coiffier",
        description="A graph toolbox implementing classical algorithms",
        long_description=long_description,
        packages=setuptools.find_packages()
        )
