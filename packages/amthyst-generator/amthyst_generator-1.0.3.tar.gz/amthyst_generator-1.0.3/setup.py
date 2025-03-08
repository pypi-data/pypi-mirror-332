from setuptools import setup, find_packages

setup(
    name = "amthyst_generator",
    version = "1.0.3",
    packages = find_packages(),
    install_requires = [
        "PyYAML~=6.0.2",
        "questionary~=2.1.0"
    ],
    entry_points = {
        "console_scripts": [
            "amthyst-generator = amthyst_generator:datapack_generator"
        ]
    },
    package_data={"amthyst_generator": ["files.yaml"]},
    include_package_data=True
)