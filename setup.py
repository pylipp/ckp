from setuptools import setup, find_packages

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='ckp',
    version="0.2",
    description='TODO',
    long_description=long_description,
    url='https://github.com/pylipp/ckp',
    author='Philipp Metzner',
    author_email='beth.aleph@yahoo.de',
    license='GPLv3',
    #classifiers=[],
    py_modules=["main"],
    entry_points = {
        'console_scripts': ['ckp = main:main']
        },
    install_requires=[
        "pykeepass==2.7.2",
        "pyperclip==1.5.32",
    ],
    extras_require={
        "dev": [
            "coverage==5.1",
        ],
    },
)
