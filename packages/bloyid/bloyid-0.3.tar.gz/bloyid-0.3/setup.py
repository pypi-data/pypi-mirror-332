from setuptools import setup, find_packages
from pathlib import Path

readme_path = Path(__file__).parent
readme = (readme_path / "README.md").read_text()

setup(
    name="bloyid",
    version="0.3",  # Version aktualisiert
    packages=find_packages(),
    author="Jason Schmitz",
    description="Bloyid Bot API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ukyyyy/bloyid",
    install_requires=[
        "aiohttp>=3.11.13",
        "websockets>=15.0.1",
        "requests>=2.32.3"
    ],
)
