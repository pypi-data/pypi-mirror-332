from setuptools import setup, find_packages
import os

# Define a default long description
long_description = "A Python package to replicate folders in Lamar CMS."

# Check if README.md exists and read its contents
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="lamar_folder_sync",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["requests", "python-dotenv"],
    entry_points={
        "console_scripts": [
            "lamar-sync = lamar_folder_sync.cli:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package to replicate folders in Lamar CMS.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
