from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='classicML-server',
    version='0.1a1',
    description='classicML web service',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Steve R. Sun',
    author_email='s1638650145@gmail.com',
    url='https://github.com/sun1638650145/classicML-server',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    license='Apache Software License',
    install_requires=[
        'classicML==0.6',
        'flask>=1.1.2',
        'gunicorn>=20.1.0',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
              'classicML-server = classicML_server.main:main'
        ]
    },
)
