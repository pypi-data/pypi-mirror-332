import setuptools


setuptools.setup(
    name='pyvariantfilter',
    version='3.0.0',
    author='Joseph Halstead',
    author_email='josephhalstead89@gmail.com',
    description='Python package for filtering variants.',
    long_description='pyvariantfilter',
    long_description_content_type='text/markdown',
    url='https://github.com/josephhalstead/pyvariantfilter',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
   'pysam>=0.22.1',
   'pandas>=2.2'
],
)
