from setuptools import setup, find_packages

setup(
    name='mytool4docker',
    version='0.0.1',
    description='mytool4docker = mytoolset + akatool',
    author='du7ec',
    author_email='dutec6834@gmail.com',
    url='https://github.com/FarAway6834/mytool4docker',
    packages=find_packages(exclude=[]),
    install_requires=['akatool', 'mytoolset'],
    keywords='mytool4docker = mytoolset + akatool'.split(),
    python_requires='>=3.4',
    package_data={},
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
)