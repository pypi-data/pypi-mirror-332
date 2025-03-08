from setuptools import setup, find_packages

setup(
    name="simplearray",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["numpy"],
    author="Your Name",
    author_email="your@email.com",
    description="A simple library that returns a NumPy array",
    url="https://github.com/yourusername/simplearray",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
