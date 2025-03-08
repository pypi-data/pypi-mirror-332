from setuptools import setup, find_packages

setup(
    name="maaranparottakadai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "parotta=maaranparottakadai.parotta:parotta"
        ]
    },
    author="Balamurugan",
    description="A fun Python package about Maaran Parotta Kadai!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/maaranparottakadai",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
