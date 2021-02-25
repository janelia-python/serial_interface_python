
import pathlib
import codecs
import setuptools


here = pathlib.Path(__file__).resolve().parent

with codecs.open(here.joinpath('DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='serial_interface',

    use_scm_version = True,
    setup_requires=['setuptools_scm'],

    description='Extends serial.Serial to add methods such as auto discovery of available serial ports in Linux, Windows, and Mac OS X',
    long_description=long_description,

    url='https://github.com/janelia-pypi/serial_interface_python',

    author='Peter Polidoro',
    author_email='peterpolidoro@gmail.com',

    license='BSD',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 3',
    ],

    keywords='serial',

    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['pyserial>=3',
                      ],
)
