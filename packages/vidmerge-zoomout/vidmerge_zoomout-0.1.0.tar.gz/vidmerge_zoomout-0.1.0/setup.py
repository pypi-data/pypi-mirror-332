from setuptools import setup

setup(
    name='vidmerge_zoomout',
    version='0.1.0',
    py_modules=['vidmerge_zoomout'],
    entry_points={
        'console_scripts': [
            'generate = generate_zoom_out_video:main',
        ],
    },
    install_requires=[
        'opencv-python>=4.5.1',
        'tqdm>=4.56.0',
    ],
)