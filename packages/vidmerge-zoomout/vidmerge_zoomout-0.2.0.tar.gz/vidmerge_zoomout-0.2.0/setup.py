from setuptools import setup
from setuptools import find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
long_description = (HERE / 'README.md').read_text(encoding='utf-8')

setup(
    name='vidmerge_zoomout',
    version='0.2.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires='>=3.6',
    install_requires=[
        'opencv-python>=4.5.1',
        'tqdm>=4.56.0',
        'pathlib',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)