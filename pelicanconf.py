#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pedro Abel Diaz'
SITENAME = 'Datascience para el Bien Social'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'es'

#PATH = 'content'

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
AUTHOR_SAVE_AS = 'coderHook'
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
SITE_DESCRIPTION = u'My nombre es Pedro Abel Diaz - Estudie Criminologia aunque otra de mis grandes pasiones es la tecnologia, juntas creo que tiene el potencial necesario para alcanzar grandes metas. En este blog tratate de enmarcar el camino que voy siguiendo para juntar estas dos ramas. DataScience y Criminologia para el bien Social.'

# Landing Page
PROJECTS = [
        {
            'name': 'Predicting the Stock Market Using Machine Learning',
            'url':
            'https://github.com/coderHook/Apple-predicting-price/blob/master/apple_predictions.ipynb',
            'description': 'Prediciendo los mercados usando Python'
            ' Machine learning Techniques'
            ' such as, linear regression and tree forest'},
        {
            'name': 'Ganando al juego de Jeopardy usando Python y tecnicas de analisis de datos.',
            'url':
            'https://github.com/coderHook/Project--Winning-Jeopardy',
            'description': 'Jeopardy is an '
            'interesting game on we can use our data science habilities to'
            'know what question can increase our chances to win the game'}
        ]

LANDING_PAGE_ABOUT = {'title': 'Aprendiendo DataScience para el bien Social.',
        'details': """
        <div itemscope itemtype="http://schema.org/Person">
        <p>My nombre es <span itemprop="name">Pedro Abel Diaz</span>.
       Soy <a href="https://github.com/coderHook/" title="My Github
       profile" itemprop="url"><span itemprop="nickname">coderHook</span></a> en Github. Puedes contactar conmigo via email <a
       href="mailto:diazpedroabel@gmail.com" title="My email
       address" itemprop="email">email</a>.</p>

       <p>Estudie Criminologia aunque otra de mis grandes pasiones es la tecnologia,
       juntas creo que tiene el potencial necesario para alcanzar grandes metas.
       En este blog tratate de enmarcar el camino que voy siguiendo para juntar estas dos ramas. DataScience y Criminologia para el bien Social.'
       </p>
       <p>
       Principalmente trabajo con Python, R y Javascript. En este momento trabajo como agente de ventas en una fabrica de calzado
       aunque planeo cambiar mi profesion en el proximo año. Me encanta aprender cosas nuevas, creo que una de las mayores motivaciones que encuentro
       en mi vida es cuando descubro un nuevo camino lleno de posibilidades y de nuevas maneras de hacer las cosas que quiza antes por desconocimiento no
       era capaz de ver.
       </p>

       <p>
       Por esta razon creo que aprende ciencia de datos "Data Science" es tan encearia para un criminologo, pues le capacita a este
       para poder tomar decisiones en la sociedad que ayuden  a buen desarrollo de esta y prevenir o buscar la mejor manera de enfrentarnos
       a nuevos retos.
       </p>

       <h4><b>Estructura del blog</b></h4>
       <p>Al principio ire colgando ejercicios basicos, quiza alguna cosita mas compleja que haga para mostrar como se lleva a cabo un proyecto de Data Science,
       y que asi quede mas claro las series de post que ahremos sobre limpieza de datos, Visulaizacion de los datos, donde encontrar Datasets y por ultimo tecnicas de
       "Machine learning" que podemos utilizar para enseñar a nuestra maquina a sacar predicciones basandose en los datos que tenemos.
       </p>

       <p>
       Espero que con este blog, alguien que quiera aprender Data Science para el bien social, encuentre la motivacion
       necesaria para hacerlo.
       </p>

       </div>

      """}
