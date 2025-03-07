from setuptools import setup, find_packages

# TESTING
# python -m unittest discover -s tests
# PRE-COMMIT TESTING (with .yaml file ready)
# pre-commit install

# BUILD
# python setup.py sdist bdist_wheel
# PUBLISH
# twine upload dist/*

setup(
    name="geogeometry",
    version="0.0.5",
    description="A Python geometrical library made for geotechnical engineering.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jorge Martinez",
    author_email="jmartinez@gmintec.com",
    license="MIT",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
