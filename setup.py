from distutils.core import setup

setup(
    name='canvas-data-sdk',
    version='0.1.0',
    author='Colin Murtaugh',
    author_email='cmurtaugh@gmail.com',
    packages=['canvas_data'],
    scripts=['bin/example.py'],
    url='http://pypi.python.org/pypi/canvas-data-sdk/',
    license='LICENSE',
    description='A Python SDK for working with Instructure\'s Canvas Data REST API.',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests >= 2.13.0",
    ],
)
