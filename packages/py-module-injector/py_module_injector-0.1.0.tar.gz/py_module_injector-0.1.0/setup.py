from setuptools import setup, find_packages

setup(
    name="py-module-injector",
    version="0.1.0",
    description="Uma biblioteca de modularização em python",
    author="Cleverson Pedroso",
    author_email="cleverson212121@gmail.com",
    packages=find_packages(),
    package_data={
        "python_module": ["py.typed"],
    },
    install_requires=[
        "typing-extensions",  # Adiciona suporte para extensões de tipagem
    ],
    entry_points={
        "console_scripts": [
            "python-module = python_module.__main__:main",
        ],
    },
)
