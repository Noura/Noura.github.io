#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

TARGET = 'to-deploy/'

pages = [ {
            'template': 'index.html',
            'path': '',
            'tabname': 'Projects'
          },
          {
            'template': 'experiments.html',
            'path': 'experiments',
            'tabname': 'Experiments'
          },
          {
            'template': 'about.html',
            'path': 'about',
            'tabname': 'About'
          }
        ]

def main():
    here = os.path.dirname(__file__)
    deploy_target = os.path.join(here, TARGET)
    loader = jinja2.FileSystemLoader(os.path.join(here, 'templates'))
    templates = jinja2.Environment(loader=loader)

    if os.path.exists(deploy_target):
        shutil.rmtree(deploy_target)
    os.makedirs(deploy_target)
    shutil.copytree(os.path.join(here, 'static'), os.path.join(deploy_target, 'static'))

    for page in pages:
        tem = templates.get_template(page['template'])
        ctx = { 'pages': pages }
        out_dir = os.path.join(deploy_target, page['path'])
        if page['path']:
            os.makedirs(out_dir)
        with codecs.open(os.path.join(out_dir, 'index.html'), 'w') as out:
            out.write(tem.render(**ctx))

if __name__ == '__main__':
    main()
