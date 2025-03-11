from setuptools import setup, find_packages

setup(
    name="time-it-profiler",  # Your package name
    version="1.0.3",
    packages=find_packages(),
    install_requires=[],
    author="Brian Vess",
    author_email="brianvess@icloud.com",
    description="A lightweight Python decorator for measuring execution time and system resource usage.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brianvess/time_it.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)