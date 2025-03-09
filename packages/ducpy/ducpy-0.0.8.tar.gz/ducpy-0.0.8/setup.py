from setuptools import find_packages, setup


setup(
    name='ducpy',
    version='0.0.8',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=['flatbuffers', 'nanoid'],
    python_requires='>=3.7',
    include_package_data=True,
    package_data={'ducpy': ['Duc/*']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)