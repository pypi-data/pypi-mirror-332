import sys
if sys.version_info < (3, 6):
    sys.exit('cmakerer requires Python 3.6+')

from setuptools import setup

setup(
  name='cmakerer',
  version='1.3.2',
  description='Generates CMakeLists.txt files from arbitrary C/C++ codebases.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author='Jeff Dileo',
  author_email='jtdileo@gmail.com',
  url='https://github.com/ChaosData/cmakerer',
  license='BSD (2 Clause)',

  python_requires='>=3.6.0',
  install_requires=[],
  include_package_data=True,
  packages=['cmakerer'],

  entry_points={
    'console_scripts': [
      'cmakerer=cmakerer:main',
    ],
  },
  classifiers=[
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3.6',
  ],
  keywords='cmake clion'
)

