from setuptools import setup
import beetle

setup(
    name='beetle',
    version=beetle.version,
    author='Esben Sonne',
    author_email='esbensonne@gmail.com',
    url='https://github.com/cknv/beetle',
    license='MIT',
    keywords='',
    packages=[
        'beetle'
    ],
    entry_points={
        'console_scripts': [
            'beetle = beetle.cli:main',
        ]
    },
    classifiers=[
        '',
    ],
    install_requires=[
        'PyYAML==3.11',
        'awesome-slugify==1.5',
        'markdown==2.4.1',
    ],
)
