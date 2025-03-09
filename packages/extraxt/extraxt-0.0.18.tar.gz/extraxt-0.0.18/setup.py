from setuptools import setup, find_packages
import pathlib

# Read the contents of README.md
this_directory = pathlib.Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="extraxt",
    version="0.0.18",
    description="Easily extract data from PDFs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Matt J. Stevenson",
    author_email="dev@mattjs.me",
    url="https://github.com/samsa-eng/extraxt",
    packages=find_packages(),
    install_requires=["pandas", "PyMuPDF"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
