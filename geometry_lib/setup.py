from setuptools import setup, find_packages

setup(
    name='geometry_lib',
    version='0.3',
    packages=find_packages(),
    description='Library to compute and visualize areas of geometric figures',
    author='Your Name',
    install_requires=[
        'matplotlib',
    ],
    python_requires='>=3.7',
)
