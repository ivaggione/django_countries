from setuptools import setup, find_packages

setup(
    name = "django_countries",
    version = "0.1.0",
    description = 'Provides models for a "complete" list of countries',
    author = 'David Danier',
    author_email = 'david.danier@team23.de',
    url = 'https://github.com/ddanier/django_countries',
    long_description=open('README.txt', 'r').read(),
    packages = [
        'countries',
        'countries.management',
        'countries.management.commands',
        'countries.templatetags',
        'countries.utils',
    ],
    package_data = {
        'countries': ['fixtures/*', 'locale/*/LC_MESSAGES/*'],
    },
    requires = [
        'django(>=1.2)',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)

