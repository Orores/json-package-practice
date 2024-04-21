from setuptools import setup, find_packages

setup(
    name='include_json',
    version='0.0.1',
    description='Test for including a json in a package',
    author='orores',
    author_email='orores@orores.com',
    url='http://orores.com',
    license='MIT',
    packages=find_packages(where='src'),
    include_package_data=True,
    package_dir={'': 'src'},
    package_data={
        "": ["*.json"]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': ['include_json=include_json:main']
    },
    keywords='include json',
    python_requires=">=3.6",
    setup_requires=['wheel'],
)
