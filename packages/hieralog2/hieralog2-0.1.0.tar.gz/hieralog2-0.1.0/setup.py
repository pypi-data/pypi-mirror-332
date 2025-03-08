from setuptools import setup, find_packages

setup(
    name='hieralog2',
    version='0.1.0',
    description='Hierarchical logging library with enhanced printing functions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/hieralog',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'colorama',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
