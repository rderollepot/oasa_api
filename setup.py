from setuptools import setup, find_packages

setup(
    name='oasa_api',
    version='0.1.0',
    url='https://github.com/rderollepot/oasa_api',
    author='Romain DEROLLEPOT',
    author_email='romain.derollepot@univ-eiffel.fr',
    description='This Python package provides a convenient wrapper for interacting with the OASA S.A. (Athens Public Transport) API, allowing users to retrieve various information related to the public transport network in Athens, Greece.',
    packages=find_packages(),
    install_requires=['requests', 'pandas'],
)