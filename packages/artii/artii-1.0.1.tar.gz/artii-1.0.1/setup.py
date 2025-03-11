from setuptools import setup, find_packages

setup(
    name="artii",
    version="1.0.1",
    packages=find_packages(),
    install_requires=["opencv-python"],
    entry_points={
        "console_scripts": [
            "artii = artii.main:main",
        ],
    },
    author="Mikael Gibert",
    author_email="",
    description="A CLI tool to convert images, GIFs, and videos to ASCII",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/migibert/artii",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

