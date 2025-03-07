from setuptools import setup, find_packages

setup(
    name="HAI_Bot",
    version="0.1",
    license="MIT",
    packages=find_packages(),
    description="A Python package for creating ChatBot with your own data",
    author="Hamed Amiri",
    url="https://github.com/HDAI654/HAI_Bot",
    install_requires=["keras", "numpy"],
    classifiers=["Programming Language :: Python :: 3", 
                 "Operating System :: OS Independent"
    ],
    package_data={
        'HAI_Bot': ['*.py'],
        'HAI_Bot': ['*.pyi'],
    },
    python_requires='>=3.6',
)