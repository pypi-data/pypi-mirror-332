from setuptools import setup

long_description = open('README', 'r').read()

setup(name='matek',
    version='0.1.4',
    description='Matek for the 3rd grade',
    url='',
    author='Csaba Saranszky',
    author_email='alt@256.hu',
    license='GPL',
    packages=['matek'],
    install_requires=['colorama'],
    zip_safe=False,
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'szorzas=matek.szorzas:main',
        ],
    })
