from setuptools import setup
import beetle

setup(
    name=beetle.name,
    version=beetle.version,
    author='Esben Sonne',
    author_email='esbensonne+code@gmail.com',
    url=beetle.project_url,
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
        'Jinja2==2.7.3',
    ],
)
