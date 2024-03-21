from setuptools import setup, find_packages

with open("README.rst", "r") as f:
    long_description = f.read()

setup(

    name='pytracertool',
    version='2.0.1',
    author='Darshan Lakshman',
    author_email='darshan.lakshman@icloud.com',
    description='A versatile tool for tracing code execution, capturing variable changes, and logging print statements.',
    long_description=long_description,
    url='https://github.com/DarshanLakshman/PyTracerTool.git',
    packages=find_packages(),
    install_requires=['tabulate', 'typing'],
    keywords=["trace", "debugging", "tracing", "execution", "visualisation"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)

