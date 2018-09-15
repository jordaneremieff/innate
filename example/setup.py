from setuptools import find_packages, setup


setup(
    name="myapp",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["innate"],
    entry_points={"console_scripts": ["myapp = myapp.__main__:main"]},
)
