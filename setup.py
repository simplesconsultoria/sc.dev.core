from setuptools import setup, find_packages
import os

version = '20120528.1dev'

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
        'Babel',
        'collective.dist==0.2.5',
        'i18ndude==3.2.2',
        'rst2pdf==0.16',
        'sc.templer.buildout',
        'sc.templer.core',
        'sc.templer.docs',
        'sc.templer.policy',
        'sc.templer.theme',
        'setuptools-git==0.4.2',
        'setuptools_hg==0.3',
        'Sphinx',
        'Sphinx-PyPI-upload==0.2.1',
        'templer.core',
        'templer.plone',
        'templer.plonebuildout',
        'templer.plonelocalcommands'
        'zc.rst2',
        'zest.releaser==3.30',
#        'zopeskel.dexterity==1.3',
      ],
      entry_points={
          'zest.releaser.releaser.after':
          'sphinx_pypi=sc.dev.core.sphinx_pypi:upload'
          },
      )
