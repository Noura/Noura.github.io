#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

pages = [ \
    {
        'name': 'Mobile Phones & Illiteracy in Morocco',
        'thumbnail': 'apples',
        'path': 'moblit',
        'template': 'mobile_illiteracy.html',
    },
    {
        'name': 'Solar Cooker for the Himalayas',
        'thumbnail': 'solsource',
        'path': 'solsource',
        'template': 'solar_cooker.html',
    },
    {
        'name': 'WaaZam!',
        'thumbnail': 'waazam',
        'path': 'waazam',
        'template': 'waazam.html',
    },
    {
        'name': 'SiriusXM Radio Station Creator',
        'thumbnail': '',
        'path': 'sxm',
        'template': 'sxm.html',
    },
    {
        'name': 'Tools for Quality Assurance',
        'thumbnail': '',
        'path': 'en_qa',
        'template': 'qa.html',
    },
    {
        'name': 'Lissajous & Rotary Harmonograph Visualizer',
        'thumbnail': 'lissa',
        'path': 'lissa',
        'template': 'lissajous.html',
    },
    {
        'name': 'Chladni Waves Visualizer',
        'thumbnail': 'chladni',
        'path': 'chladni',
        'template': 'chladni.html',
    },
    {
        'name': 'About',
        'thumbnail': '',
        'path': 'about',
        'template': 'about.html',
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
