from setuptools import setup, find_packages

setup(
    name="mp4-to-gif-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "moviepy"
    ],
    entry_points={
        "console_scripts": [
            "mp4_to_gif=mp4_to_gif.cli:main"
        ]
    },
    author="Shahid Hussain",
    description="A CLI tool to convert MP4 to GIF with size optimization",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shahidhussain07/mp4-to-gif",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
