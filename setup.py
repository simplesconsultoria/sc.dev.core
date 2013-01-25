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
        'collective.dist',
        'docutils',
        'i18ndude',
        'Pillow',
        'rst2pdf',
        'sc.templer.buildout',
        'sc.templer.core',
        'sc.templer.docs',
        'sc.templer.policy',
        'sc.templer.theme',
        'setuptools-git',
        'setuptools_hg',
        'Sphinx',
        'Sphinx-PyPI-upload',
        'templer.core',
        'templer.plone',
        'templer.plonebuildout',
        'templer.plone.localcommands',
        'z3c.dependencychecker',
        'zc.rst2',
        'zest.pocompile',
        'zest.releaser',
#        'zopeskel.dexterity',
      ],
      entry_points={
          'zest.releaser.releaser.after':
          'sphinx_pypi=sc.dev.core.sphinx_pypi:upload'
          },
      )
