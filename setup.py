from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(

    name='pytracertool',
    version='1.0.0',
    author='Darshan Lakshman',
    author_email='darshan.lakshman@icloud.com',
    description='A versatile tool for tracing code execution, capturing variable changes, and logging print statements.',
    long_description=long_description,
    url='https://github.com/DarshanLakshman/PyTracerTool.git',
    packages=find_packages(),
    install_requires=['sys', 'copy', 'tabulate', 'types', 'typing'],
    keywords=["trace", "debugging", "tracing", "execution", "visualisation"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0 License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)

