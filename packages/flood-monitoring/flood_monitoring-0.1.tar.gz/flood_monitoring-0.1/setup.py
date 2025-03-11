from setuptools import setup, find_packages

setup(
    name='flood-monitoring',
    version='0.1',
    author='Yusuf Sulehman',
    author_email='yusuf.sulehman@postgrad.manchester.ac.uk',
    description='A simple flood monitoring package',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/YSulehman/flood-monitoring',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'flood_monitoring = flood_monitoring.main:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
