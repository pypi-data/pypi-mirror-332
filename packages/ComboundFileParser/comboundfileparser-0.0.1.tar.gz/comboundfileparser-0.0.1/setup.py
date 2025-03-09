from setuptools import setup, find_packages
import ComboundFileParser as package

setup(
    name='ComboundFileParser',
    version=package.__version__,
    py_modules=['ComboundFileParser'],
    packages=find_packages(include=[]),
    install_requires=[],
    scripts=[],
    author="Maurice Lambert",
    author_email="mauricelambert434@gmail.com",
    maintainer="Maurice Lambert",
    maintainer_email="mauricelambert434@gmail.com",
    description='This module implements a Compound file parser (file format used by OLE and base file format for macros, msi, msg, doc, xls...)',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mauricelambert/ComboundFileParser",
    project_urls={
        "Github": "https://github.com/mauricelambert/ComboundFileParser",
        "Documentation": "https://mauricelambert.github.io/info/python/security/ComboundFileParser.html",
    },
    download_url="https://mauricelambert.github.io/info/python/security/ComboundFileParser.pyz",
    include_package_data=True,
    classifiers=[
        "Topic :: System",
        "Topic :: Security",
        'Operating System :: POSIX',
        "Natural Language :: English",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        'Operating System :: MacOS :: MacOS X',
        "Programming Language :: Python :: 3.8",
        'Operating System :: Microsoft :: Windows',
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
    keywords=['OLE', 'CompoundFile', 'Parser', 'microsoft', 'macros', 'msi', 'msg', 'mail', 'doc', 'xls'],
    platforms=['Windows', 'Linux', "MacOS"],
    license="GPL-3.0 License",
    entry_points = {
        'console_scripts': [
            'ComboundFileParser = ComboundFileParser:main'
        ],
    },
    python_requires='>=3.8',
)