#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

pages = [ \
    {
        'name': 'Color-Changing Fabric',
        'thumbnail': 'threads',
        'path': 'threads',
        'template': 'threads.html',
        'date': '2015',
    },
    {
        'name': 'Code 510 Mentoring',
        'thumbnail': 'code510',
        'path': 'code510',
        'template': 'code510.html',
        'date': '2014 - ongoing',
    },
    {
        'name': 'Buddy the HugBug',
        'thumbnail': 'hugbug',
        'path': 'hugbug',
        'template': 'hugbug.html',
        'date': '2015',
    },
    {
        'name': 'Myo DJ Effects Controller',
        'thumbnail': 'myodj',
        'path': 'myodj',
        'template': 'myodj.html',
        'date': '2014',
    },
    {
        'name': 'Intel: Connect Anything',
        'thumbnail': 'galileo',
        'path': 'intel',
        'template': 'intel.html',
        'date': '2014',
    },
    {
        'name': 'WaaZam!',
        'thumbnail': 'waazam',
        'path': 'waazam',
        'template': 'waazam.html',
        'date': '2013',
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
        'name': 'Smart Bamboo Blinds for Bali',
        'thumbnail': 'bali-house',
        'path': 'bamboo_blinds',
        'template': 'bali.html',
        'date': 'May 2014',
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
        'name': 'Biosignals Experiments',
        'thumbnail': 'peacebone-gsr',
        'path': 'biosignals',
        'template': 'biosignals.html',
        'date': '',
    },
    {
        'name': 'Music & Data @ The Echo Nest',
        'thumbnail': 'en',
        'path': 'the_echo_nest',
        'template': 'echonest.html',
        'date': '2012 - 2013',
    },
    {
        'name': 'Contact & Publications',
        'thumbnail': 'nyd2015',
        'path': 'publications',
        'template': 'publications.html',
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

if __name__ == '__main__':
    main()
