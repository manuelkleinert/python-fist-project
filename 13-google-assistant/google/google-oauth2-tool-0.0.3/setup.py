from setuptools import setup, find_packages
from codecs import open
from os import path
import json

here = path.abspath(path.dirname(__file__))

with open('Pipfile.lock') as fd:
    lock_data = json.load(fd)
    install_requires = [package_name for package_name in lock_data['default'].keys()]
    tests_require = [package_name for package_name in lock_data['develop'].keys()]


setup(
    name='google-oauth2-tool',
    use_scm_version=True,
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    extras_require={
        'test': tests_require,
    },
    entry_points={
        'console_scripts': [
            'oauth2_tool=google_oauth2_tool.__main__:main'
        ]
    },
    license='BSD',
    include_package_data=True,
    description='Create OAuth2 key file from OAuth2 client id file',
    long_description=open('README.rst', 'r', encoding='utf-8').read(),
    url='https://github.com/dlancer/google-oauth2-tool',
    author='dlancer',
    author_email='dmdpost@gmail.com',
    maintainer='dlancer',
    maintainer_email='dmdpost@gmail.com',
    zip_safe=False,
    python_requires='>=3.5',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 3 - Alpha',
    ],
)
