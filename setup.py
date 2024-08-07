from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simple_gpu_queue",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Ben Hoover",
    author_email="benhoover34@gmail.com",
    description="A simple queue for running GPU workloads in JAX",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bhoov/simple-gpu-queue",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)