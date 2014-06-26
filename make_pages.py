#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

pages = [ {
            'template': 'index.html',
            'path': '',
            'tabname': 'Projects',
            'projects': ['mobile_illiteracy.html', 'solar_cooker.html', 'waazam.html', 'sxm.html', 'qa.html'],
          },
          {
            'template': 'index.html',
            'path': 'experiments',
            'tabname': 'Experiments',
            'projects': ['lissajous.html', 'chladni.html'],
          },
          {
            'template': 'about.html',
            'path': 'about',
            'tabname': 'About'
          }
        ]

def main():
    here = os.path.dirname(__file__)
    loader = jinja2.FileSystemLoader(os.path.join(here, 'templates'))
    templates = jinja2.Environment(loader=loader)

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
