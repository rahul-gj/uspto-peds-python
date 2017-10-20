import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'celery==4.1.0',
    'requests==2.18.4',
    'redis==2.10.6',
    'BeautifulSoup==3.2.1',
]

test_requires = [
]

setup(name='uspto-opendata-pair',
      version='0.0.0',
      description='uspto-opendata-pair   is a client for accessing the USPTO PAIR Bulk Data API',
      long_description=README,
      license="MIT",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Archiving",
        "Topic :: Text Processing",
        "Topic :: Utilities",
      ],
      author='Andreas Motl',
      author_email='andreas@ip-tools.org',
      url='https://github.com/ip-tools/uspto-opendata-pair',
      keywords='patent information research search',
      packages=find_packages(),
      include_package_data=True,
      package_data={
      },
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=requires,
      tests_require=test_requires,
      extras_require={
          'documentation': [
              'Sphinx==1.6.4',
              'sphinx_rtd_theme==0.2.5b1',
          ],
      },

      entry_points={
        'console_scripts': [
        ],
      },

    )