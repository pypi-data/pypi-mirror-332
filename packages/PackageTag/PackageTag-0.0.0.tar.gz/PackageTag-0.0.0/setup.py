from setuptools import setup, find_packages

setup(
    name='PackageTag',
    version='0.0.0',
    packages=find_packages(),
    install_requires=['requests',
    'numpy',],  # Liste des dépendances,
    author='Fatma Kchaou',
    author_email='fatma.kchaou29@gmail.com',
    description='Package ',
    long_description='But de crée package with v0.0.0 ', #
    long_description_content_type='text/markdown',
    url='https://github.com/Fatma-Kchaou1/Cars/tree/masterv',  # Lien vers ton repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
