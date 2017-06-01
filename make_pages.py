#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

# pages appear in the order listed here
pages = [ \
    {
        # appears as title for that project page, and title of tile on homepage
        'name': 'Peace Sculpture',
        # refers to the image as specified in app.scss
        'thumbnail': 'salaam_closeup_15.JPG',
        # the hash of the URL at which the project page appears
        'path': 'salaam',
        # template file in templates/
        'template': 'salaam.html',
        # appears at bottom of project page just as text
        'date': 'spring 2017',
    },
    {
        'name': 'Performing VR',
        'thumbnail': 'vr_square.jpg',
        'path': 'performing_vr',
        'template': 'performing_vr.html',
        'date': 'fall 2016',
    },
    {
        'name': 'Biosignals as Social Cues',
        'thumbnail': 'hint_shirt_tile.png',
        'path': 'hint',
        'template': 'hint.html',
        'date': '2015 - present',
    },
    {
        'name': 'Color-Changing Fabric',
        'thumbnail': 'weave_4x4.png',
        'path': 'ebb',
        'template': 'ebb.html',
        'date': '2015',
    },
    {
        'name': 'Code 510 Mentoring',
        'thumbnail': 'code510.png',
        'path': 'code510',
        'template': 'code510.html',
        'date': '2014 - 2016',
    },
    {
        'name': 'Buddy the HugBug',
        'thumbnail': 'hugbug.jpg',
        'path': 'hugbug',
        'template': 'hugbug.html',
        'date': '2015',
    },
    {
        'name': 'Myo DJ Effects Controller',
        'thumbnail': 'beatwave.png',
        'path': 'myodj',
        'template': 'myodj.html',
        'date': '2014',
    },
    {
        'name': 'Intel: Connect Anything',
        'thumbnail': 'galileo_w_pin.jpg',
        'path': 'intel',
        'template': 'intel.html',
        'date': '2014',
    },
    {
        'name': 'WaaZam!',
        'thumbnail': 'waazam_space.png',
        'path': 'waazam',
        'template': 'waazam.html',
        'date': '2013',
    },
    {
        'name': 'Harmonograph Visualizer',
        'thumbnail': 'lissa2.png',
        'path': 'lissa',
        'template': 'lissajous.html',
        'date': '2013',
    },
    {
        'name': 'Chladni Waves Visualizer',
        'thumbnail': 'chladni2.png',
        'path': 'chladni',
        'template': 'chladni.html',
        'date': '2013',
    },
    {
        'name': 'Smart Bamboo Blinds for Bali',
        'thumbnail': 'bali_house.jpg',
        'path': 'bamboo_blinds',
        'template': 'bali.html',
        'date': 'May 2014',
    },
    {
        'name': 'Mobile Phones & Illiteracy in Morocco',
        'thumbnail': 'apples.jpg',
        'path': 'moblit',
        'template': 'mobile_illiteracy.html',
        'date': '2012',
    },
    {
        'name': 'Solar Cooker for the Himalayas',
        'thumbnail': 'solsource.jpg',
        'path': 'solsource',
        'template': 'solar_cooker.html',
        'date': '2010',
    },
    {
        'name': 'Biosignals Experiments',
        'thumbnail': 'peacebone_gsr.png',
        'path': 'biosignals',
        'template': 'biosignals.html',
        'date': '',
    },
    {
        'name': 'Music & Data @ The Echo Nest',
        'thumbnail': 'en.png',
        'path': 'the_echo_nest',
        'template': 'echonest.html',
        'date': '2012 - 2013',
    },
    {
        'name': 'Contact & Publications',
        'thumbnail': 'nyd2015.jpg',
        'path': 'about',
        'template': 'about.html',
        'date': '',
    },
  ]

# publications appear in the order listed here
publications_list = [
    {
        # custom name to refer to this publication in templates
        'name': 'hint',
        # the citation text, can include HTML, just gets inserted as is
        'cite': """<b>Noura Howell</b>, Laura Devendorf, Rundong (Kevin) Tian, Tom&aacute;s Vega, Nan-Wei Gong, Ivan Poupyrev, Eric Paulos, Kimiko Ryokai. 2016. Biosignals as social cues: Ambiguity and emotional interpretation in social displays of skin conductance. <i>Designing Interactive Systems</i>.""",
        # link to pdf or official hosting
        'url': '/static/pdf/16_DIS_Hint.pdf',
    },
    {
        'name': 'ebb',
        'cite': """Laura Devendorf, Joanne Lo, <b>Noura Howell</b>, Jung Lin Lee, Nan-Wei Gong, M. Emre Karagozler, Shiho Fukuhara, Ivan Poupyrev, Eric Paulos, Kimiko Ryoaki. 2016. "I don't want to wear a screen": Probing perceptions of and possibilities for dynamic displays on clothing. <i>SIGCHI Conference on Human Factors in Computing Systems (CHI'16 - Best Paper Award)</i>.""",
        'url': "http://artfordorks.com/pubs/16_CHI_Ebb.pdf",
    },
    {
        'name': 'disWorkshopBiosensing',
        'cite': """Nick Merrill, Richmond Wong, <b>Noura Howell</b>, Luke Stark, Lucian Leahu, Dawn Nafus. 2017. Interrogating Biosensing in Everyday Life. <i>Designing Interactive Systems Companion</i>.""",
        'url': "/static/pdf/17_DIS_Workshop_Biosensing.pdf",
    },
    {
        'name': 'disDC',
        'cite': """<b>Noura Howell</b>. 2016. Representation and interpretation of biosensing. <i>Designing Interactive Systems Companion</i>.""",
        'url': "/static/pdf/16_DIS_DC.pdf",
    },
    {
        'name': 'caiot',
        'cite': """<b>Noura Howell</b>. 2015. Connecting two Oakland neighborhoods: surveillance and self-representation. <i>Workshop paper at Critical Alternatives 2015</i>. <a href="https://depts.washington.edu/tatlab/participationiot/">workshop</a>.""",
        'url': "/static/pdf/15_CA_IoT.pdf",
    },
    {
        'name': 'L21',
        'cite': """Sarah Spence Adams, <b>Noura Howell</b>, Nathaniel Karst, Denise Sakai Troxell, Junjie Zhu. 2013. On the L(2,1)-labelings of amalgamations of graphs. <i>Discrete Applied Mathematics, 161</i>(7-8): 881-8.""",
        'url': "https://dl.acm.org/citation.cfm?id=2452099",
    },
    {
        'name': 'ethanol',
        'cite': """Jian Shi, Ratna R. Sharma-Shivappa, Mari Chinn, <b>Noura Howell</b>. 2009. Effect of microbial pretreatment on enzymatic hydrolysis and fermentation of cotton stalks for ethanol production. <i>Biomass and Bioenergy, 33</i>(1): 88-96.""",
        'url': "http://agris.fao.org/agris-search/search.do?recordID=US201301683178",
    },
  ]

# some data munging so that templates can refer to publications by name
publications_by_name = {}
for pub in publications_list:
    publications_by_name[pub['name']] = pub

def make_pages():
    here = os.path.dirname(__file__)
    loader = jinja2.FileSystemLoader(os.path.join(here, 'templates'))
    templates = jinja2.Environment(loader=loader)

    # this is a bit hacky, but, jinja templates like to receive an unpacked dict where the keys of the dict become the variable names in the template. but it was getting too annoying to pass all the variables to different templates individually. now the jinja template just gets one variable ctx which is a dict with all the other variables
    vars_for_templates = { 
        'ctx': {
            'pages': pages,
            'publications_list': publications_list,
            'publications_by_name': publications_by_name,
        }
    }

    tem = templates.get_template('index.html')
    with codecs.open(os.path.join(here, 'index.html'), 'w') as out:
        out.write(tem.render(**vars_for_templates))

    print "make_pages()"

if __name__ == '__main__':
    make_pages()
