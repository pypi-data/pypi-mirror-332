from setuptools import setup, find_packages

setup(
    name="maisagarhoo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Sagar Singh",
    author_email="sagarsingh802183@gmail.com",
    description="A sample package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gp-sagar/chegg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
