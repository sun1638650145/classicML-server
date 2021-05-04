from setuptools import setup, find_packages

with open('README.md', 'r') as fp:
    long_description = fp.read()

setup(
    name='classicML-server',
    version='0.1a3',
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
        'classicML>=0.6, <0.7',
        'flask>=1.1.2',
        'numpy>=1.19.2, <=1.19.4',
        'waitress>=2.0.0',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
              'classicML-server = classicML_server.console:main'
        ]
    },
)
