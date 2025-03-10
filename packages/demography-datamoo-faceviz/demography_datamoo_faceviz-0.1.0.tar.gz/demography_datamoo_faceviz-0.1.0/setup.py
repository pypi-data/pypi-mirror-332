import os
from setuptools import setup, find_packages

# Read requirements from requirements.txt
def read_requirements():
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

# Read README file for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="demography_datamoo_faceviz",  # Package name
    version="0.1.0",
    packages=find_packages(include=["gender_detection", "gender_detection.*"]),
    install_requires=read_requirements(),  # Load dependencies from requirements.txt
    entry_points={
        "console_scripts": [
            "detect-gender=gender_detection.main:run_detection",
        ],
    },
    author="Datamoo",
    author_email="sunitha.a@datamoo.ai",
    description="Age and Gender detection using PyQt UI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/datamoo-projects/age-gender-detection/src/main/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True,  # Include non-code files if necessary
)
