from setuptools import setup
import beetle

setup(
    name=beetle.name,
    version=beetle.version,
    author='Esben Sonne',
    author_email='esbensonne+code@gmail.com',
    description='Beetle is a simple static site generator',
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
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Text Processing',
    ],
    install_requires=[
        'PyYAML',
        'awesome-slugify',
        'Jinja2',
    ],
)
