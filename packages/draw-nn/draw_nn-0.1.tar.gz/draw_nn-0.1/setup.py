from setuptools import setup, find_packages

setup(
    name="draw_nn",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy"
    ],
    author="Atharva",
    author_email="developer.atharva2001@gmail.com",
    description="A simple package to visualize neural network architectures",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/developerAtharva/draw_nn",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
