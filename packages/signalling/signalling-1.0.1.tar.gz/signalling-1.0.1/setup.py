import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='signalling',
    version='1.0.1',
    author='Mike Malinowski',
    author_email='mike.external@outlook.com',
    description='Pure python library for utilising a Signalling event pattern',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikemalinowski/signalling',
    python_requires='>3.5.2',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
    ],
    keywords="signal",
)
