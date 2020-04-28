#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

from data import publications
publications_list = publications.publications_list

from data import news
news = news.news

from data import pages
pages = pages.pages

# some data munging so that templates can refer to publications by name
publications_by_name = {}
for pub in publications_list:
    publications_by_name[pub['name']] = pub

def make_top_level_page(here, templates, rel_path, this_template, vars_for_template):
    if rel_path != '':
        shutil.rmtree(os.path.join(here, rel_path), ignore_errors=True )
        os.mkdir(rel_path)

    tem = templates.get_template(this_template)

    path = os.path.join(here, rel_path, 'index.html')

    with codecs.open(path, 'w') as out:
        out.write(tem.render(**vars_for_template))

def make_pages():
    here = os.path.dirname(__file__)
    loader = jinja2.FileSystemLoader(os.path.join(here, 'templates'))
    templates = jinja2.Environment(loader=loader)

    # HOMEPAGE #######################################
    make_top_level_page(here, templates, '', 'home.html', {
        'ctx': {
            'pages': pages,
            'publications_list': publications_list,
            'publications_by_name': publications_by_name,
            'news': news,
        }
    })

    # PUBLICATIONS PAGE ################################
    make_top_level_page(here, templates, 'pubs', 'publications.html', {
        'ctx': {
            'publications_list': publications_list,
            'publications_by_name': publications_by_name,
        }
    })

    # CV PAGE ##########################################
    make_top_level_page(here, templates, 'cv', 'cv.html', {})
    
    # TEACHING PAGE ####################################
    make_top_level_page(here, templates, 'teaching', 'teaching.html', {})

    # ABOUT PAGE #######################################
    make_top_level_page(here, templates, 'about', 'about.html', {})

    # NEWS PAGE ########################################
    make_top_level_page(here, templates, 'news', 'news.html', {
        'news': news
    })

    # PROJECTS PAGES ###################################
    vars_for_project_pages = {
        'ctx': {
            'page': {},
            'publications_list': publications_list,
            'publications_by_name': publications_by_name,
            'news': news,
        }
    }

    # assumes projects dir already exists, so first delete it to clear contents
    shutil.rmtree(os.path.join(here, 'projects'), ignore_errors=True )
    # then recreate it empty to put in the updated project pages
    os.mkdir('projects')
    for page in pages:
        vars_for_project_pages['ctx']['page'] = page
        tem = templates.get_template(page['template'])
        with codecs.open(os.path.join(here, 'projects', page['path']+'.html'), 'w') as out:
            out.write(tem.render(**vars_for_project_pages))

    print "make_pages()"

if __name__ == '__main__':
    make_pages()
