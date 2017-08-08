#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pedro Abel Diaz'
SITENAME = 'Datascience CoderHook'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

PATH = 'content'

# Appearance
TYPOGRIFY = True
THEME = 'themes/pelican-elegant'
DEFAULT_PAGINATION = False

#Plugins
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']


# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social
SOCIAL = (
        ('Github', 'http://github.com/coderHook'),
        ('Email', 'diazpedroabel@gmail.com'),
          )

# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
MAILCHIMP_FORM_ACTION = u'empty'

# Legal
#SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"> coderHook DataScience;"</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="coderhook.github.io" property="cc:attributionName" rel="cc:attributionURL">Pedro Abel Diaz</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'

# SEO
SITE_DESCRIPTION = u'My name is Pedro Abel Diaz ― a Criminologist that realized how important is Data Science to get deeper insights. I am coderHook at Github. I design webpages and analyze data to get insights using Python and Machine Learning techniques. I work mainly with Python, but can use other programming languages such R. Criminology is my major degree but I am also interested in Finance and how the industry works. At this momment I am in the 2nd year of my Industrial management Bachelor degree. This is my personal blog.'

# Landing Page
PROJECTS = [
        {
            'name': 'Elegant',
            'url':
            'http://oncrashreboot.com/pelican-elegant',
            'description': 'A clean and distraction free Pelican theme, with'
            ' search and a'
            ' lot more unique features. Built with Jinja2 and Bootstrap'},
        {
            'name': 'Logpad + Duration',
            'url':
            'https://github.com/talha131/logpad-plus-duration#logpad--duration',
            'description': 'Vim plugin to emulate Windows Notepad logging feature,'
            ' and log duration of each entry'}
        ]

LANDING_PAGE_ABOUT = {'title': 'I analyze and get insights from Data.',
        'details': """<div itemscope itemtype="http://schema.org/Person"><p>My name
        is <span itemprop="name">Pedro Abel Diaz</span>.
       I am <a href="https://github.com/coderHook/" title="My Github
       profile" itemprop="url"><span itemprop="nickname">coderHook</span></a> on Github. You can also reach me via <a
       href="mailto:diazpedroabel@gmail.com" title="My email
       address" itemprop="email">email</a>.</p><p>I work mainly with Python, but can use other programming languages
       such R. Criminology is my major degree but I am also interested in Finance and how the industry works.
       At this momment I am in the 2nd year of my Industrial management Bachelor degree.

       <p>I plan to change my career, at this moment I am working as a sales agent in a shoe factory, and my intention is
       to become a data scientist, my competences includes research, product design, engineering and deployment.
       I also love to learn, I think one of the best motivation that you can get in live is when you have somehing new
       to learn which is fantastic because there is always room for improvement.</p>

       <p>I also love web development, <a href="https://www.freecodecamp.com/coderhook" title="My freecodecamp profile"
       itemprop="url"><span itemprop="nickname">coderHook Web developer</span></a> here you can see all the codes that I programmed in Javascript,
       jQuery, React.js, css, d3.js, node.js, express.js and most of their libraries. I do not
       pigeonhole myself to specific languages or frameworks. A good developer
       is receptive and has the ability to learn new technologies. I like to
       contribute to other projects, at this moment I am contributing in a meetUP group <a href="https://www.meetup.com/es-ES/Alicante-Data-Science-Meetup/" itemprop="url">Alicante Data Science </a>.</p>

       <p>Besides programming, I love sports, <a href="https://en.wikipedia.org/wiki/Ultimate_(sport)" title="Ultimate Frisbee" itemprop="url">Ultimate Frisbee</a> is my passion
       and <a href="https://en.wikipedia.org/wiki/Slacklining" itemprop="url"> Slacklining </a> gave me a lot of concentration and
       peace of mind, basically when you are on the cord you cannot thing in so many things at a time :)
       </p>

       <p>English is my second language. My mother tongue is Spanish and I always love to learn new words in exotic languages so I encourage you to teach me something.</p></div>"""}
