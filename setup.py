import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pytikz-pglammers",  # Replace with your own username
    version="0.0.1",
    author="Piet Lammers",
    author_email="email@pietlammers.com",
    description="pytikz: generate TikZ with python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pglammers/pytikz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
