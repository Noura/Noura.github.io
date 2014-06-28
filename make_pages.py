#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

pages = [ \
    {
        'name': 'ConnectAnyThing with the Intel Galileo',
        'thumbnail': 'galileo',
        'path': 'intel',
        'template': 'intel.html',
        'date': 'Current Work',
    },
    {
        'name': 'WaaZam!',
        'thumbnail': 'waazam',
        'path': 'waazam',
        'template': 'waazam.html',
        'date': '2013',
    },
    {
        'name': 'Mobile Phones & Illiteracy in Morocco',
        'thumbnail': 'apples',
        'path': 'moblit',
        'template': 'mobile_illiteracy.html',
        'date': '2012',
    },
    {
        'name': 'Solar Cooker for the Himalayas',
        'thumbnail': 'solsource',
        'path': 'solsource',
        'template': 'solar_cooker.html',
        'date': '2010',
    },
    {
        'name': 'Harmonograph Visualizer',
        'thumbnail': 'lissa',
        'path': 'lissa',
        'template': 'lissajous.html',
        'date': '2013',
    },
    {
        'name': 'Chladni Waves Visualizer',
        'thumbnail': 'chladni',
        'path': 'chladni',
        'template': 'chladni.html',
        'date': '2013',
    },
    {
        'name': 'SiriusXM Radio Station Creator',
        'thumbnail': 'en',
        'path': 'sxm',
        'template': 'sxm.html',
        'date': '2012',
    },
    {
        'name': 'Tools for Quality Assurance',
        'thumbnail': 'rickshawjs',
        'path': 'en_qa',
        'template': 'qa.html',
        'date': '2013',
    },
    {
        'name': 'About',
        'thumbnail': 'bali',
        'path': 'about',
        'template': 'about.html',
        'date': '',
    },
  ]

def main():
    here = os.path.dirname(__file__)
    loader = jinja2.FileSystemLoader(os.path.join(here, 'templates'))
    templates = jinja2.Environment(loader=loader)

    tem = templates.get_template('index.html')
    ctx = { 'pages': pages }
    with codecs.open(os.path.join(here, 'index.html'), 'w') as out:
        out.write(tem.render(**ctx))

    for page in pages:
        tem = templates.get_template(page['template'])
        ctx = { 'pages': pages , 'current_page': page }
        out_dir = os.path.join(here, page['path'])
        if page['path'] and not os.path.exists(page['path']):
            os.makedirs(out_dir)
        with codecs.open(os.path.join(out_dir, 'index.html'), 'w') as out:
            out.write(tem.render(**ctx))

if __name__ == '__main__':
    main()
