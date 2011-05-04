from setuptools import setup, find_packages

def get_version(version):
    import datetime
    if "dev" in version:
        now = int(datetime.datetime.now().strftime('%Y%m%d%H%M'))
        return "%s-r%d" % (version, now)
    else:
        return version

version = '0.1.0'

setup(
    name='sact.resizabletable',
    version=get_version(version),
    description='A Reportlab/Platypus table that can resize itself automatically.',
    long_description=open("README.rst").read(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    keywords='sact platypus table resizable',
    author='SecurActive SA',
    author_email='opensource@securactive.net',
    url='https://github.com/securactive/sact.resizabletable',
    license='BSD',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    namespace_packages=['sact'],
    zip_safe=True,
    install_requires=[
        'setuptools',
        'reportlab',
    ],
    entry_points={},
    extras_require={'test': []},
)
