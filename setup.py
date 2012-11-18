from setuptools import setup, find_packages

import os

version = '20120528.1dev'

long_description = (open("README.txt").read() + "\n" +
                    open(os.path.join("docs", "HISTORY.txt")).read())

setup(name='sc.dev.core',
      version=version,
      description="Developement core packages used by Simples Consultoria",
      long_description=long_description,
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone development helpers',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='http://www.simplesconsultoria.com.br',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['sc', 'sc.dev'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'Babel',
        'collective.dist==0.2.5',
        'i18ndude==3.2.2',
        'pep8',
        'Pillow',
        'rst2pdf==0.91',
        'sc.templer.buildout',
        'sc.templer.core',
        'sc.templer.docs',
        'sc.templer.policy',
        'sc.templer.theme',
        'setuptools-git==0.4.2',
        'setuptools_hg==0.4',
        'Sphinx',
        'Sphinx-PyPI-upload==0.2.1',
        'templer.core',
        'templer.plone',
        'templer.plonebuildout',
        'templer.plone.localcommands',
        'z3c.dependencychecker',
        'zc.rst2',
        'zest.pocompile',
        'zest.releaser==3.34',
#        'zopeskel.dexterity==1.3',
      ],
      entry_points={
          'zest.releaser.releaser.after':
          'sphinx_pypi=sc.dev.core.sphinx_pypi:upload'
          },
      )
