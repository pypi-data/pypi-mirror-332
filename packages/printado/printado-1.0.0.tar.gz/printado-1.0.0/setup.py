from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="printado",
    version="1.0.0",
    description="Ferramenta de captura personalizada",
    author="Felipe Aquino",
    author_email="felipe@feharo.com.br",
    url="https://github.com/Feharo-Tech/Printado",
    packages=["printado"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "printado=printado.main:main",
        ]
    },
    include_package_data=True, 
)
