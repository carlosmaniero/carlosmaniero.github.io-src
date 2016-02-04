#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Carlos Maniero'
SITENAME = u'Dev Diary'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
LINKS = (
    ('GitHub', 'http://github.com/carlosmaniero'),
    ('Facebook', 'http://facebook.com/carlosmaniero'),
    ('Twitter', 'http://twitter.com/carlosmaniero'),
)

DEFAULT_PAGINATION = 10

THEME = 'themes/Casper2Pelican'

# Theme Configs
AUTHOR_PIC_URL = 'https://avatars0.githubusercontent.com/u/2002011?v=3&s=460'
AUTHOR_BIO = 'Python Developer and an open source evangelist. ' \
             'Focused in web  development. ' \
             'Working with Django and Tornado for async web solutions. ' \
             'A lover of the Linux terminal and the creator of the Pygamii, ' \
             'an ascii game engine written in Python.'
AUTHOR_LOCATION = 'São Paulo/Brazil'
TWITTER_USERNAME = 'carlosmaniero'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS = 'UA-73329109-1'
DISQUS_SITENAME = 'carlosmaniero-github-io.disqus.com'
