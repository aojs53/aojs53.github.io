#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'aojs53'
SITENAME = u'あ、じゃぁ近況報告でも'
SITEURL = 'https://aojs53.github.io'

PATH = 'content'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

THEME = 'theme/pelican-blueidea'
TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('ココログ', 'http://aojs53.txt-nifty.com/aojs53/'),)


# Social widget
SOCIAL = (('twitter', 'https://twitter.com/aojs53/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
