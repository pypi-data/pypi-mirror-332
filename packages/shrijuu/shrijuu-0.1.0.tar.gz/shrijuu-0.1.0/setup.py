from setuptools import setup, find_packages

setup(
    name='shrijuu',
    version='0.1.0',
    author='Harshit Kumar',  # Updated from 'Your Name'
    author_email='harshitkumar9030@gmail.com',
    description='A fun Python module representing a girlfriend character with interactive features.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/harshitkumar9030/shrijuu',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # No external dependencies needed for this package
    ],
)