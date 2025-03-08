from setuptools import setup, find_packages
import sys

# Function to read requirements from requirements.txt
def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

# Base requirements
requirements = read_requirements()

setup(
    name='droidsentinel',
    version='1.0',  # Update to your new version
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'droidsentinel=droidsentinel.main:main',
        ],
    },
    author='Chetan Kashyap',
    author_email='chetanbug@duck.com',
    description='Automated Static Analysis of APKs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ch3tanbug/DroidSentinel',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
