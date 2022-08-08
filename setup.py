from setuptools import setup, find_packages

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='classicML-server',
    version='0.1a5',
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
        'classicML>=0.9, <0.10',
        'flask>=2.0.0, <=2.2.1',
        'numpy>=1.21.0, <=1.23.1',
        'waitress>=2.0.0, <=2.1.2',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
              'classicML-server = classicML_server.console:run'
        ]
    },
)
