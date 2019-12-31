#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Andreas Lloyd'
SITENAME = "Andreas Lloyd's blog about stuff"
SITEURL = ''

# Flex theme basic info
SITETITLE = 'Andreas Lloyd'
SITESUBTITLE = 'Bits and pieces about data science'
SITEDESCRIPTION = 'python, data science, model, algorithm, business, cabify'
SITELOGO = '/images/photo.jpeg'

# Main Menu
MAIN_MENU = True
MENUITEMS = (('Categories', '/categories'),)


PATH = 'content'
STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (,)

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/andreas-lloyd/'),
    ('github', 'https://github.com/andreas-lloyd'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Typogrpahical improvements
TYPOGRIFY = False

# Theme
THEME = 'Flex'

# Invent some copyright stuff
COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = 2020
