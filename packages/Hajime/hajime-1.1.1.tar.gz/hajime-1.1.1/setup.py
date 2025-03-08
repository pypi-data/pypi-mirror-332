from setuptools import setup, find_packages

setup(
    name="Hajime",
    version="1.1.1",
    packages=find_packages(),
    install_requires=['sqlalchemy', 'termcolor'],
    author="Franciszek Czajkowski",
    description="Lightweight Website Framework",
    url="https://Hajime.pythonanywhere.com",
    project_urls={
        "Source": "https://github.com/FCzajkowski/Hajime",
        "Documentation": "https://Hajime.pythonanywhere.com/Documentation"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)