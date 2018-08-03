# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='aliases',
    version='v0.0.1',
    description='To create simple aliases',
    long_description="Nothing",
    url='',
    author='Aaron Valoroso',
    author_email='valoroso99@gmail.com',
    license='BSD License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['aliases', 'alias'],
    packages = find_packages(exclude=['build', 'docs', 'templates']),
)
