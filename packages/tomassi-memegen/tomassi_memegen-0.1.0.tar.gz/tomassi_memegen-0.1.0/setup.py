from setuptools import setup, find_packages

setup(
    name='tomassi-memegen',
    version='0.1.0',
    description='A module to create memes with text on images',
    author='Tomáš Ivan',
    author_email='tomas.ivan.it@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Pillow', 
        'requests',
        'io'
    ],
    entry_points={
        'console_scripts': [
            'create-meme=memegen.meme:create_meme',
        ],
    },
)
