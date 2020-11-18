import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imagecolorizer", # Replace with your own username
    version="0.1.3",
    author="Guilherme Silveira",
    author_email="guilherme.silveira@alura.com.br",
    description="Uses InstColorization to colorize images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guilhermesilveira/imagecolorizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'cython',
        'pyyaml==5.1',
        'dominate==2.4.0',
    ],
    dependency_links=[
        'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI',
    ],
)