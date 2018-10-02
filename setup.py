""" Setup package """
from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='transintentlation',
      version='1.0.0',
      description=u"Analyze an intent config and a running config and translate\
      it to actual commands to apply to IOS-like devices",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"JP Mondet",
      url='https://github.com/jpmondet/transintentlation',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'diffios'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      transintentlation=transintentlation.cli:cli
      """
      )
