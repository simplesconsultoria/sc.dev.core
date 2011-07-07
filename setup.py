from setuptools import setup, find_packages
import os

version = '20110530.2dev'

setup(name='sc.dev.core',
      version=version,
      description="Developement core packages used by Simples Consultoria",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone development helpers',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='http://www.simplesconsultoria.com.br',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sc', 'sc.dev'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'sc.paster.package==0.8',
          'sc.paster.buildout==0.7.1',
          'sc.paster.policy==0.7',
          'sc.paster.theme==0.8',
          'setuptools-git==0.3.4',
          'setuptools_hg==0.2',
          'collective.dist==0.2.5',
          'zest.releaser==3.22',
          'collective.dist==0.2.5',
          'Sphinx==1.0.4',
          'rst2pdf==0.16',
          'i18ndude==3.2.2',
          'Sphinx-PyPI-upload==0.2.1'
      ],
      entry_points={
          'zest.releaser.releaser.after':
              'sphinx_pypi=sc.dev.core.sphinx_pypi:upload'
          },
      )
