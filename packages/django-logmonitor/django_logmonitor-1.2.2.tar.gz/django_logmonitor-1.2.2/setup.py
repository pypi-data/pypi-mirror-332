import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django_logmonitor',
    version='1.2.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Utilidad Django para monitorear y auditar las acciones de los usuarios en tus modelos.',
    keywords="logs auditoria audit monitoreo utilidad herramientas Python Django",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JaviPulido/LogMonitor',
    author='Javier L. Pulido',
    author_email='grupol2st@gmail.com',
    install_requires=[
        'django>=3.2',
        'django-admin-list-filter-dropdown>=1.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)