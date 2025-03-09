from setuptools import setup, find_packages

setup(
    name="bloyid",
    version="0.2",  # <- Hier die Versionsnummer erhöhen
    packages=find_packages(),
    install_requires=[],
    author="Jason Schmitz",
    description="Bloyid Bot Api",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ukyyyy/bloyid",
)
