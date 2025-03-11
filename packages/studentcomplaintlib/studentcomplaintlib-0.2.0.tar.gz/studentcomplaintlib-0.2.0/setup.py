from setuptools import setup, find_packages

setup(
  name='studentcomplaintlib',
  version='0.2.0',
  description='This is a simple message for complaint posting.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Rohith',
  author_email='x23411520@student.ncirl.ie',
  classifiers=[
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
],
  keywords='studentcomplaintlib', 
  packages=find_packages(),
  python_requires=">=3.6"
)
  