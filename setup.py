from setuptools import setup, find_packages
import os

version = '20100806.01'

setup(name='sc.dev.core',
      version=version,
      description="Developement core packages used by Simples Consultoria",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sc', 'sc.dev'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'sc.paster.package==0.5.1',
          'sc.paster.buildout==0.5.1',
          'sc.paster.policy==0.6.1',
          'sc.paster.theme==0.6.2',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
