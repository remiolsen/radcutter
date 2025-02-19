from setuptools import setup, find_packages

setup(
    name='radcutter',
    version='0.1',
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[x.strip() for x in open("requirements.txt").readlines()],
    entry_points={
        'console_scripts': [
            'radcutter = radcutter.radcutter:main',
        ],
    },
)