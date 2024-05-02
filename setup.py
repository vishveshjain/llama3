from setuptools import find_packages, setup

setup(
    name='1O1Help',
    version='0.0.1',
    author='Vishvesh',
    author_email='vishvesh2851994@gmail.com',
    install_requires=[
        "llamaapi",
        "streamlit",
        "python-dotenv",
    ],
    packages=find_packages()

)