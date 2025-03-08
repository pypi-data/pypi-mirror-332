from setuptools import setup, find_packages

setup(
    name="gdrive_downloader",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gdown",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "gdrive-download=gdrive_downloader.downloader:main",
        ],
    },
    author="Yang Wang",
    author_email="yangwang4work@gmail.com",
    description="A CLI tool to download files or folders from Google Drive.",
    url="https://github.com/penguinwang96825/gdrive_downloader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
