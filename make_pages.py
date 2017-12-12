#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

# pages appear in the order listed here
pages = [ \
    {
        'name': 'Social Emotional Biosensing',
        'thumbnail': 'hint_shirt_tile.png',
        'path': 'ripple',
        'template': 'ripple.html',
        'date': '2015 - present',
    },
    {
        'name': 'Tangible Laughter',
        'thumbnail': 'choc_tile.jpg',
        'path': 'laughter',
        'template': 'laughter.html',
        'date': '2016 - present',
    },
    {
        'name': 'Color-Changing Fabric as Realtime Data Display',
        'thumbnail': 'weave_4x4.png',
        'path': 'ebb',
        'template': 'ebb.html',
        'date': '2015',
    },
    {
        'name': 'Assembling Critical Practices Reading Group',
        'thumbnail': 'assembling_critical_practices.png',
        'path': 'assembling_critical_practices',
        'template': 'assembling_critical_practices.html',
        'date': '2016 - present',
    },
    {
        # appears as title for that project page, and title of tile on homepage
        'name': 'Participatory Peace Sculpture',
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
        'name': 'Performing VR Together',
        'thumbnail': 'vr_square.jpg',
        'path': 'performing_vr',
        'template': 'performing_vr.html',
        'date': 'fall 2016',
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
        'name': 'Bio-Controlled DJ Effects',
        'thumbnail': 'beatwave.png',
        'path': 'myodj',
        'template': 'myodj.html',
        'date': '2014',
    },
    {
        'name': 'Intel Connect Anything Prototyping Kit',
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
        'name': 'Music & Data at The Echo Nest',
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
        'name': 'ripple',
        'cite': """<b>Noura Howell</b>, Laura Devendorf, Tom&aacute;s Vega G&aacute;lvez, Rundong (Kevin) Tian, Kimiko Ryokai. 2017. Tensions of data-driven reflection: A case study of real-time emotional biosensing. <i>In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems</i> (CHI'17) (forthcoming).""",
        'url': None,
    },
    {
        # custom name to refer to this publication in templates
        'name': 'chi18laughter',
        # the citation text, can include HTML, just gets inserted as is
        'cite': """Kimiko Ryokai, Elena Duran, <b>Noura Howell</b>, Jonathan Gillick, David Bamman. 2018. Capturing, Representing, and Interacting with Laughter. <i>In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems</i> (CHI'18) (forthcoming).""",
        # link to pdf or official hosting
        'url': None,
    },
    {
        'name': 'dis17laughter',
        'cite': """Kimiko Ryokai, Elena Duran, Dina Bseiso, <b>Noura Howell</b>,Ji Won Jun. 2017. Celebrating Laughter: Capturing and Sharing Tangible Representations of Laughter. <i>In Extended Abstracts of the SIGCHI Conference on Designing Interactive Systems Companion</i> (DIS'17).""",
        'url': "http://dl.acm.org/citation.cfm?id=3079146",
    },
    {
        'name': 'hint',
        'cite': """<b>Noura Howell</b>, Laura Devendorf, Rundong (Kevin) Tian, Tom&aacute;s Vega G&aacute;lvez, Nan-Wei Gong, Ivan Poupyrev, Eric Paulos, Kimiko Ryokai. 2016. Biosignals as social cues: Ambiguity and emotional interpretation in social displays of skin conductance. <i>In Proceedings of the SIGCHI Conference on Designing Interactive Systems</i> (DIS'16).""",
        'url': '/static/pdf/16_DIS_Hint.pdf',
    },
    {
        'name': 'ebb',
        'cite': """Laura Devendorf, Joanne Lo, <b>Noura Howell</b>, Jung Lin Lee, Nan-Wei Gong, M. Emre Karagozler, Shiho Fukuhara, Ivan Poupyrev, Eric Paulos, Kimiko Ryokai. 2016. "I don't want to wear a screen": Probing perceptions of and possibilities for dynamic displays on clothing. <i>In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems</i> (CHI'16) Best Paper Award.""",
        'url': "http://artfordorks.com/pubs/16_CHI_Ebb.pdf",
    },
    {
        'name': 'disWorkshopBiosensing',
        'cite': """Nick Merrill, Richmond Wong, <b>Noura Howell</b>, Luke Stark, Lucian Leahu, Dawn Nafus. 2017. Interrogating Biosensing in Everyday Life. <i>In Proceedings of the Companion Publication on Designing Interactive Systems</i> (DIS Companion'17).""",
        'url': "/static/pdf/17_DIS_Workshop_Biosensing.pdf",
    },
    {
        'name': 'chimici',
        'cite': """<b>Noura Howell</b>. 2017. Personal Reflection as Creative Practice in Collaboration with Biosensing Machines. <i>Workshop paper at CHI'17</i>. <a href="https://mici2017.org/">workshop</a>.""",
        'url': "/static/pdf/17_CHI_MICI.pdf",
    },
    {
        'name': 'disDC',
        'cite': """<b>Noura Howell</b>. 2016. Representation and interpretation of biosensing. <i>In Proceedings of the Companion Publication on Designing Interactive Systems</i> (DIS Companion'16).""",
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
    vars_for_homepage = { 
        'ctx': {
            'pages': pages,
            'publications_list': publications_list,
            'publications_by_name': publications_by_name,
        }
    }

    tem = templates.get_template('home.html')
    with codecs.open(os.path.join(here, 'index.html'), 'w') as out:
        out.write(tem.render(**vars_for_homepage))

    vars_for_project_pages = {
        'ctx': {
            'page': {},
            'publications_list': publications_list,
            'publications_by_name': publications_by_name,
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
