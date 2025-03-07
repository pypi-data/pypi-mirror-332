from setuptools import setup, find_packages

setup(
    name="dsainone",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["numpy", "numba"],
    author="Kinshuk jain",
    description="A high-performance DSA library optimized for speed and memory efficiency.",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
