# -*- coding: utf-8 -*-
#
# MongoDB documentation build configuration file, created by
# sphinx-quickstart on Mon Oct  3 09:58:40 2011.
#
# This file is execfile()d with the current directory set to its containing dir.

import sys
import os.path
import datetime

project_root = os.path.join(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(project_root)

from giza.config.runtime import RuntimeStateConfig
from giza.config.helper import fetch_config, get_versions, get_manual_path

conf = fetch_config(RuntimeStateConfig())
intersphinx_libs = conf.system.files.data.intersphinx
sconf = conf.system.files.data.sphinx_local

sys.path.append(os.path.join(conf.paths.projectroot, conf.paths.buildsystem, 'sphinxext'))

# -- General configuration ----------------------------------------------------


extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
    'mongodb',
    'directives',
    'intermanual',
    'tabs',
    'source_constants',
    'icon'
]

source_constants = {
  'download-page': '`downloads page <https://www.mongodb.com/download-center/compass?jmp=docs>`__'
}

templates_path = ['.templates']
exclude_patterns = []

source_suffix = '.txt'

master_doc = sconf.master_doc
language = 'en'
project = sconf.project
copyright = u'2008-{0}'.format(datetime.date.today().year)

version = conf.version.branch
release = conf.version.release

rst_epilog = '\n'.join([
    '.. |branch| replace:: ``{0}``'.format(conf.git.branches.current),
    '.. |copy| unicode:: U+000A9',
    '.. |year| replace:: {0}'.format(datetime.date.today().year),
    '.. |ent-build| replace:: MongoDB Enterprise',
    '.. |hardlink| replace:: http://docs.mongodb.com/compass/',
    '.. |compass| replace:: MongoDB Compass',
    '.. |compass-short| replace:: Compass',
    '.. |checkmark| unicode:: U+2713'
])

extlinks = {
    'issue': ('https://jira.mongodb.org/browse/%s', '' ),
    'source': ('https://github.com/mongodb/mongo/blob/master/%s', ''),
    'docsgithub' : ( 'http://github.com/mongodb/docs/blob/' + conf.git.branches.current + '/%s', ''),
    'manual': ('http://docs.mongodb.org/manual%s', ''),
}

intersphinx_mapping = {}

try:
    for i in intersphinx_libs:
        intersphinx_mapping[i['name']] = ( i['url'], os.path.join(conf.paths.projectroot,
                                                              conf.paths.output,
                                                              i['path']))
except:
    for i in intersphinx_libs:
        intersphinx_mapping[i.name] = ( i.url, os.path.join(conf.paths.projectroot,
                                                              conf.paths.output,
                                                              i.path))


languages = [
    ("ar", "Arabic"),
    ("cn", "Chinese"),
    ("cs", "Czech"),
    ("de", "German"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("hu", "Hungarian"),
    ("id", "Indonesian"),
    ("it", "Italian"),
    ("jp", "Japanese"),
    ("ko", "Korean"),
    ("lt", "Lithuanian"),
    ("pl", "Polish"),
    ("pt", "Portuguese"),
    ("ro", "Romanian"),
    ("ru", "Russian"),
    ("tr", "Turkish"),
    ("uk", "Ukrainian")
]

# -- Options for HTML output ---------------------------------------------------

html_theme = sconf.theme.name
html_theme_path = [ os.path.join(conf.paths.buildsystem, 'themes') ]
html_title = conf.project.title
htmlhelp_basename = 'MongoDB'

html_logo = ".static/logo-mongodb.png"
html_static_path = ['source/.static']
html_last_updated_fmt = '%b %d, %Y'

html_copy_source = False
html_domain_indices = True
html_use_index = True
html_split_index = False
html_show_sourcelink = False
html_show_sphinx = True
html_show_copyright = True

manual_edition_path = '{0}/{1}/{2}.{3}'

html_theme_options = {
    'branch': conf.git.branches.current,
    'translations': languages,
    'language': language,
    'manual_path': "compass",
    'repo_name': 'docs-compass',
    'jira_project': 'DOCS',
    'google_analytics': sconf.theme.google_analytics,
    'project': sconf.project,
    'nav_excluded': sconf.theme.nav_excluded,
    'version': version,
    'version_selector':  get_versions(conf),
    'active_branches': conf.version.active,

}

html_sidebars = sconf.sidebars


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = conf.project.title
epub_author = u'MongoDB Documentation Project'
epub_publisher = u'MongoDB, Inc.'
epub_copyright = copyright
epub_theme = 'epub_mongodb'
epub_tocdup = True
epub_tocdepth = 3
epub_language = 'en'
epub_scheme = 'url'
epub_identifier = 'http://docs.mongodb.com/compass/'
epub_exclude_files = []
epub_pre_files = []
epub_post_files = []
