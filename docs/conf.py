# -*- coding: utf-8 -*-
# Sphinx configuration
# For more information see http://sphinx.pocoo.org/config.html

extensions = []

templates_path = ['_templates']

source_suffix = '.txt'
source_encoding = 'utf-8'

master_doc = 'index'

project = u'sc.dev.core'
copyright = u'2010-2012, Simples Consultoria'

language = 'pt_BR'

exclude_trees = ['_build']

pygments_style = 'sphinx'

html_theme = 'default'
html_title = u'Padrões de desenvolvimento Simples Consultoria'
html_short_title = u'Padrões de desenvolvimento'
html_style = 'simples.css'
html_logo = '_static/simples.gif'
html_static_path = ['_static']
htmlhelp_basename = 'scdevcoredoc'

latex_documents = [
  ('index', 'scdevcore.tex', u'sc.dev.core Documentation',
   u'Erico Andrei', 'manual'),
]

from pkg_resources import get_distribution
version = release = get_distribution(project).version
