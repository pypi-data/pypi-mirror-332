from setuptools import setup, find_packages
from pathlib import Path

def get_version():
    version_file = Path(__file__).parent / "pyconstrobe" / "__init__.py"
    for line in version_file.read_text().splitlines():
        if line.startswith("__version__"):
            return line.split("=")[-1].strip().strip('"').strip("'")

setup(
    name="pyconstrobe",      # Replace with your package name
    version=get_version(),                 # Version number
    packages=find_packages(),      # Automatically find and include all packages
    author="Joseph Louis",
    author_email="joseph.louis@oregonstate.edu",
    description="This package is used to automate the DES application ConStrobe.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6',       # Specify minimum Python version (optional)
)
