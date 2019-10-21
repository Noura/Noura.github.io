#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

# news and announcements
news = [ \
     {
        'date': "Oct'19",
        'description': "Talk at Cybersecurity Research Exchange",
        'link': 'https://cltc.berkeley.edu/2019/09/08/2019-cltc-research-exchange/',
     },
     {
        'date': "May'19",
        'description': "Paper at CHI on Life-Affirming Biosensing",
        'link': '/projects/heart_sounds_bench.html',
     },
     {
        'date': "June'19",
        'description': "Paper at DIS on Menstrual Biosensing",
        'link': '/projects/menstrual_biosensing.html',
     },
#    {
#        'date': "Mar'19",
#        'description': "Talk at InfoCamp Conference",
#        'link': 'https://berkeley-infocamp.org/',
#    },
#    {
#        'date': "Feb'19",
#        'description': "Talk at Bay Area Signal Hackers at Pandora",
#        'link': 'https://www.meetup.com/bishbash/events/258830536/',
#    },
#    {
#        'date': "Feb'19",
#        'description': "Art Opening at Worth-Ryder Gallery",
#        'link': 'http://scienceatcal.berkeley.edu/visionlight-processing-perception/',
#    },
    {
        'date': "Jan'19",
        'description': "Grant from Center for Long-Term Cybersecurity",
        'link': 'https://cltc.berkeley.edu/2019grantees/',
    },
    {
        'date': "Jan'19",
        'description': "Grant from Center for Technology, Society, & Policy",
        'link': 'https://ctsp.berkeley.edu/projects2019/',
    }
]

# pages appear in the order listed here
pages = [ \
    {
        'name': 'Life-Affirming Biosensing with the Heart Sounds Bench',
        'thumbnail': 'red_bench.jpg',
        'path': 'heart_sounds_bench',
        'template': 'heart_sounds_bench.html',
        'date': '2018 - present',
    }, {
        'name': 'Conceptual Reworkings for Emotional Biosensing',
        'thumbnail': 'Feel.jpg',
        'path': 'emotional_biosensing',
        'template': 'emotional_biosensing.html',
        'date': '2018',
    }, {
        'name': 'Color-Changing Garments for Emotional Reflection',
        'thumbnail': 'ripple.png',
        'path': 'ripple',
        'template': 'ripple.html',
        'date': '2015 - 2018',
    },
    {
        'name': 'Speculating Near-Future Menstrual Biosensing',
        'thumbnail': 'vivewell_vivid.png',
        'path': 'menstrual_biosensing',
        'template': 'menstrual_biosensing.html',
        'date': '2018 - present',
    },
    {
        'name': 'Cherishing Laughter as Biosensory Data',
        'thumbnail': 'choc_tile.jpg',
        'path': 'laughter',
        'template': 'laughter.html',
        'date': '2016 - 2017',
    },
    {
        'name': 'Color-Changing Fabric as Realtime Data Display',
        'thumbnail': 'weave_4x4.png',
        'path': 'ebb',
        'template': 'ebb.html',
        'date': '2015',
    },
#    {
#        'name': 'Assembling Critical Practices Reading Group',
#        'thumbnail': 'IMG_E1207_square.JPG',
#        'path': 'assembling_critical_practices',
#        'template': 'assembling_critical_practices.html',
#        'date': '2016 - present',
#    },
    {
        # appears as title for that project page, and title of tile on homepage
        'name': 'Participatory Peace Sculpture',
        # refers to the image as specified in app.scss
        'thumbnail': 'salaam_square.JPG',
        # the hash of the URL at which the project page appears
        'path': 'salaam',
        # template file in templates/
        'template': 'salaam.html',
        # appears at bottom of project page just as text
        'date': 'spring 2017',
    },
    {
        'name': 'Heart Sounds in Cheap Plastic Buckets',
        'thumbnail': 'hsb3_square.jpg',
        'path': 'heart_sounds_buckets',
        'template': 'heart_sounds_buckets.html',
        'date': 'spring 2019',
    },
#    {
#        'name': 'Performing VR Together',
#        'thumbnail': 'vr_square.jpg',
#        'path': 'performing_vr',
#        'template': 'performing_vr.html',
#        'date': 'fall 2016',
#    },
#    {
#        'name': 'Code 510 Mentoring',
#        'thumbnail': 'code510.png',
#        'path': 'code510',
#        'template': 'code510.html',
#        'date': '2014 - 2016',
#    },
#    {
#        'name': 'Buddy the HugBug',
#        'thumbnail': 'hugbug.jpg',
#        'path': 'hugbug',
#        'template': 'hugbug.html',
#        'date': '2015',
#    },
    {
        'name': 'Bio-Controlled DJ Effects',
        'thumbnail': 'beatwave_arm.png',
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
        'name': 'Sounds',
        'thumbnail': 'IMG_E1207_square.JPG',
        'path': 'sounds',
        'template': 'sounds.html',
        'date': 'ongoing',
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
#    {
#        'name': 'Smart Bamboo Blinds for Bali',
#        'thumbnail': 'bali_house.jpg',
#        'path': 'bamboo_blinds',
#        'template': 'bali.html',
#        'date': 'May 2014',
#    },
#    {
#        'name': 'Mobile Phones & Illiteracy in Morocco',
#        'thumbnail': 'apples.jpg',
#        'path': 'moblit',
#        'template': 'mobile_illiteracy.html',
#        'date': '2012',
#    },
#    {
#        'name': 'Solar Cooker for the Himalayas',
#        'thumbnail': 'solsource.jpg',
#        'path': 'solsource',
#        'template': 'solar_cooker.html',
#        'date': '2010',
#    },
#    {
#        'name': 'Biosignals Experiments',
#        'thumbnail': 'peacebone_gsr.png',
#        'path': 'biosignals',
#        'template': 'biosignals.html',
#        'date': '',
#    },
    {
        'name': 'Music & Data at The Echo Nest',
        'thumbnail': 'en.png',
        'path': 'the_echo_nest',
        'template': 'echonest.html',
        'date': '2012 - 2013',
    }
  ]

# publications appear in the order listed here
publications_list = [
    {
        'name': 'hsb1',
        'cite': """<b>Noura Howell</b>, Greg Niemeyer, Kimiko Ryokai. 2019. Life-Affirming Biosensing in Public: Sounding Heartbeats on a Red Bench. <i>Human Factors in Computing Systems (CHI'19)</i>.""",
        'pdf': '/static/pdf/19_CHI_Heart_Sounds_Bench.pdf',
        'url': 'https://dl.acm.org/citation.cfm?id=3300910',
    },
    {
        'name': 'vivewell',
        'cite': """Sarah Fox, <b>Noura Howell</b>, Richmond Wong, Franchesca Spektor. 2019. Vivewell: Speculating Near-Future Menstrual Tracking through Current Data Practices. <i>Designing Interactive Systems Pictorials (DIS'19)</i>.""",
        'pdf': '/static/pdf/19_DIS_Vivewell.pdf',
        'url': None,
    },
    {
        'name': 'vivewell_zine',
        'cite': """Sarah Fox, <b>Noura Howell</b>, Richmond Wong, Franchesca Spektor. 2019. Vivewell: Winter Product Catalog.""",
        'pdf': '/static/pdf/19_Zine_Vivewell.pdf',
        'url': None,
    },
    {
        'name': 'cscw_emotional_biosensing',
        'cite': """<b>Noura Howell</b>, John Chuang, Abigail De Kosnik, Greg Niemeyer, Kimiko Ryokai. 2018. Emotional Biosensing: Exploring Critical Alternatives. <i>Computer Supported Cooperative Work (CSCW'18)</i>.""",
        'pdf': '/static/pdf/18_CSCW_Emotional_Biosensing.pdf',
        'url': 'https://dl.acm.org/citation.cfm?id=3274338',
    },
    {
        'name': 'ripple',
        'cite': """<b>Noura Howell</b>, Laura Devendorf, Tom&aacute;s Vega G&aacute;lvez, Rundong (Kevin) Tian, Kimiko Ryokai. 2018. Tensions of data-driven reflection: A case study of real-time emotional biosensing. <i>Human Factors in Computing Systems (CHI'18)</i>.""",
        'pdf': '/static/pdf/18_CHI_Ripple.pdf',
        'url': 'https://dl.acm.org/citation.cfm?id=3174005',
    },
    {
        # custom name to refer to this publication in templates
        'name': 'chi18laughter',
        # the citation text, can include HTML, just gets inserted as is
        'cite': """Kimiko Ryokai, Elena Duran, <b>Noura Howell</b>, Jonathan Gillick, David Bamman. 2018. Capturing, Representing, and Interacting with Laughter. <i>Human Factors in Computing Systems (CHI'18)</i>.""",
        # link to pdf
        'pdf': None,
        # link to official hosting
        'url': 'https://dl.acm.org/citation.cfm?id=3173932',
    },
    {
        'name': 'dis17laughter',
        'cite': """Kimiko Ryokai, Elena Duran, Dina Bseiso, <b>Noura Howell</b>,Ji Won Jun. 2017. Celebrating Laughter: Capturing and Sharing Tangible Representations of Laughter. <i>Extended Abstracts of Designing Interactive Systems (DIS'17)</i>.""",
        'pdf': None,
        'url': "http://dl.acm.org/citation.cfm?id=3079146",
    },
    {
        'name': 'hint',
        'cite': """<b>Noura Howell</b>, Laura Devendorf, Rundong (Kevin) Tian, Tom&aacute;s Vega G&aacute;lvez, Nan-Wei Gong, Ivan Poupyrev, Eric Paulos, Kimiko Ryokai. 2016. Biosignals as social cues: Ambiguity and emotional interpretation in social displays of skin conductance. <i>Designing Interactive Systems (DIS'16)</i>.""",
        'pdf': '/static/pdf/16_DIS_Hint.pdf',
        'url': 'https://dl.acm.org/citation.cfm?id=2901850',
    },
    {
        'name': 'ebb',
        'cite': """Laura Devendorf, Joanne Lo, <b>Noura Howell</b>, Jung Lin Lee, Nan-Wei Gong, M. Emre Karagozler, Shiho Fukuhara, Ivan Poupyrev, Eric Paulos, Kimiko Ryokai. 2016. "I don't want to wear a screen": Probing perceptions of and possibilities for dynamic displays on clothing. <i>Human Factors in Computing Systems (CHI'16)</i> - <b>Best Paper Award</b>.""",
        'pdf': "http://artfordorks.com/pubs/16_CHI_Ebb.pdf",
        'url': 'https://dl.acm.org/citation.cfm?id=2858192',
    },
    {
        'name': 'disWorkshopBiosensing',
        'cite': """Nick Merrill, Richmond Wong, <b>Noura Howell</b>, Luke Stark, Lucian Leahu, Dawn Nafus. 2017. Interrogating Biosensing in Everyday Life. <i>Designing Interactive Systems Companion (DIS Companion'17) </i>.""",
        'pdf': "/static/pdf/17_DIS_Workshop_Biosensing.pdf",
        'url': 'https://dl.acm.org/citation.cfm?id=3064865',
    },
    {
        'name': 'chimici',
        'cite': """<b>Noura Howell</b>. 2017. Personal Reflection as Creative Practice in Collaboration with Biosensing Machines. <i>Workshop paper at CHI'17</i>. <a href="https://mici2017.org/">workshop</a>.""",
        'pdf': "/static/pdf/17_CHI_MICI.pdf",
        'url': 'https://mici2017.org/proceedings/',
    },
    {
        'name': 'disDC',
        'cite': """<b>Noura Howell</b>. 2016. Representation and interpretation of biosensing. <i>Designing Interactive Systems Companion (DIS Companion'16)</i>.""",
        'pdf': "/static/pdf/16_DIS_DC.pdf",
        'url': 'https://dl.acm.org/citation.cfm?id=2909422',
    },
    {
        'name': 'caiot',
        'cite': """<b>Noura Howell</b>. 2015. Connecting two Oakland neighborhoods: surveillance and self-representation. <i>Workshop paper at Critical Alternatives 2015</i>. <a href="https://depts.washington.edu/tatlab/participationiot/">workshop</a>.""",
        'pdf': "/static/pdf/15_CA_IoT.pdf",
        'url': 'http://depts.washington.edu/tatlab/participationiot/',
    },
    {
        'name': 'L21',
        'cite': """Sarah Spence Adams, <b>Noura Howell</b>, Nathaniel Karst, Denise Sakai Troxell, Junjie Zhu. 2013. On the L(2,1)-labelings of amalgamations of graphs. <i>Discrete Applied Mathematics, 161</i>(7-8): 881-8.""",
        'pdf': None,
        'url': "https://dl.acm.org/citation.cfm?id=2452099",
    },
    {
        'name': 'ethanol',
        'cite': """Jian Shi, Ratna R. Sharma-Shivappa, Mari Chinn, <b>Noura Howell</b>. 2009. Effect of microbial pretreatment on enzymatic hydrolysis and fermentation of cotton stalks for ethanol production. <i>Biomass and Bioenergy, 33</i>(1): 88-96.""",
        'pdf': None,
        'url': "http://agris.fao.org/agris-search/search.do?recordID=US201301683178",
    },
  ]

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
