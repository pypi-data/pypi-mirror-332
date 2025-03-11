from setuptools import setup, find_packages

setup(
    name="melonn-cli-project",
    version="0.1.0",
    description="CLI para la creación del proyecto completo",
    author="Joaquin Mejia",
    author_email="nmejia@melonn.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "typer",
        "aws-cdk-lib"
    ],
    entry_points={
        "console_scripts": [
            "melonn-python-cli=main:app"
        ]
    },
)
