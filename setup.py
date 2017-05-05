try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import djangocms_shariff

version = djangocms_shariff.__version__

setup(
    name='djangocms_shariff',
    packages=['djangocms_shariff'],
    include_package_data=True,
    version=version,
    description="Content sharing buttons respecting privacy for django cms",
    author='Christoph Reimers',
    author_email='christoph@superservice-international.com',
    license='BSD License',
    url='https://github.com/byteyard/djangocms_shariff',
    keywords=['djangocms', 'django', 'shariff', 'share', 'social'],
    install_requires=[
        'django-cms>=3.2',
        'django-sekizai>=0.8',
    ],
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
)
