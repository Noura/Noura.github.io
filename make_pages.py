#!/usr/bin/env python
import os, os.path, shutil, codecs, sys

import jinja2

# news and announcements
news = [ \
#     {
#        'date': "Mar'20",
#        'description': "Talk at NYU Music and Audio Research Laboratory (MARL) and Integrated Digital Media (IDM) (cancelled)",
#        'link': None,
#     },
#     {
#        'date': "Mar'20",
#        'description': "Talk at IST Lisbon in the Department of Computer Science and Engineering",
#        'link': None,
#     },
     {
        'date': "Dec'19",
        'description': "Paper accepted to CHI 2020 - Expanding Modes of Reflection in Design Futuring with Sandjar Kozubaev, Chris Elsden, Marie Louise Juul S&oslash;ndergaard, Nick Merrill, Britta Schulte, Richmond Y. Wong",
        'link': 'https://dl.acm.org/doi/abs/10.1145/3313831.3376526',
     },
     {
        'date': "Feb'20",
        'description': "Late-Breaking Work accepted to CHI 2020 - Teachable Machine: Approachable Web-Based Tool for Exploring Machine Learning Classification, with Google AI and Google Creative Lab folks Michelle Carney, Barron Webster, Irene Alvarado, Kyle Phillips, Jordan Griffith, Jonas Jongejan, Amit Pitaru, and Alexander Chen",
        'link': 'https://dl.acm.org/doi/abs/10.1145/3334480.3382839',
     },
     {
        'date': "Mar'20",
        'description': "Research visit to RITMO with Greg Niemeyer and Alexander Jensenius (cancelled)",
        'link': 'https://www.uio.no/ritmo/english/',
     },
#     {
#        'date': "Feb'20",
#        'description': "Talk at Purdue Computer Graphics Technology Department",
#        'link': None,
#     },
#     {
#        'date': "Feb'20",
#        'description': "Talk at Georgia Tech School of Literature, Media, and Communication",
#        'link': None,
#     },
#     {
#        'date': "Jan'20",
#        'description': "Talk at North Carolina State University Department of Communication",
#        'link': None,
#     },
#     {
#        'date': "Jan'20",
#        'description': "Talk at Queen's School of Computing in Kingston, Ontario",
#        'link': None,
#     },
     {
        'date': "Jan'20",
        'description': "Grant from Center for Technology Society and Policy joint with Algorithmic Fairness and Opacity Group on the project An Alternate Lexicon for AI with Noopur Raval and Morgan Ames",
        'link': 'https://ctsp.berkeley.edu/projects-2020/',
     },
#     {
#        'date': "Dec'19",
#        'description': "Paper accepted to CHI 2020 - Expanding Modes of Reflection in Design Futuring with Sandjar Kozubaev, Chris Elsden, Marie Louise Juul S&oslash;ndergaard, Nick Merrill, Britta Schulte, Richmond Y. Wong",
#        'link': None,
#     },
#     {
#        'date': "Nov'19",
#        'description': "Talk at U Michigan School of Information",
#        'link': None,
#     },
#     {
#        'date': "Oct'19",
#        'description': "Collaborator Franchesca Spektor presented our work at Center for Technology, Society, and Policy",
#        'link': 'https://ctsp.berkeley.edu/projects2018/#menstrualBiosensing',
#     },
#     {
#        'date': "Oct'19",
#        'description': "Talk at Center for Long-Term Cybersecurity Research Exchange",
#        'link': 'https://cltc.berkeley.edu/grants/speculating-smart-city-cybersecurity-with-the-heart-sounds-bench-detourning-data-and-surveillance-in-public-space/',
#     },
#     {
#        'date': "June'19",
#        'description': "Paper at DIS on Menstrual Biosensing",
#        'link': '/projects/menstrual_biosensing.html',
#     },
#     {
#        'date': "May'19",
#        'description': "Paper at CHI on Life-Affirming Biosensing",
#        'link': '/projects/heart_sounds_bench.html',
#     },
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
#    {
#        'date': "Jan'19",
#        'description': "Grant from Center for Long-Term Cybersecurity",
#        'link': 'https://cltc.berkeley.edu/2019grantees/',
#    },
#    {
#        'date': "Jan'19",
#        'description': "Grant from Center for Technology, Society, & Policy",
#        'link': 'https://ctsp.berkeley.edu/projects2019/',
#    }
]

# pages appear in the order listed here
pages = [ \
    {
        'name': 'Life-Affirming Biosensing with the Heart Sounds Bench',
        'thumbnail': 'red_bench.jpg',
        'path': 'heart_sounds_bench',
        'template': 'heart_sounds_bench.html',
        'date': '2018 - present',
        'type': 'dissertation',
    }, 
    {
        'name': 'Survey of Emotional Biosensing Technologies and Conceptual Reworkings',
        'thumbnail': 'spire_feel_oura.jpg',
        'path': 'emotional_biosensing',
        'template': 'emotional_biosensing.html',
        'date': '2018',
        'type': 'dissertation',
    }, 
    {
        'name': 'Color-Changing Garments for Emotional Reflection',
        'thumbnail': 'ripple.png',
        'path': 'ripple',
        'template': 'ripple.html',
        'date': '2015 - 2018',
        'type': 'dissertation',
    },
    {
        'name': 'Speculating Near-Future Menstrual Biosensing',
        'thumbnail': 'vivewell_vivid.png',
        'path': 'menstrual_biosensing',
        'template': 'menstrual_biosensing.html',
        'date': '2018 - present',
        'type': 'research_collab',
    },
    {
        'name': 'Cherishing Laughter as Biosensory Data',
        'thumbnail': 'choc_tile.jpg',
        'path': 'laughter',
        'template': 'laughter.html',
        'date': '2016 - 2017',
        'type': 'research_collab',
    },
    {
        'name': 'Color-Changing Fabric as Realtime Data Display',
        'thumbnail': 'weave_4x4.png',
        'path': 'ebb',
        'template': 'ebb.html',
        'date': '2015',
        'type': 'research_collab',
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
        'type': 'interactive_art',
    },
    {
        'name': 'Heart Sounds in Cheap Plastic Buckets',
        'thumbnail': 'hsb3_square.jpg',
        'path': 'heart_sounds_buckets',
        'template': 'heart_sounds_buckets.html',
        'date': 'spring 2019',
        'type': 'interactive_art',
    },
    {
        'name': 'Performing VR Together',
        'thumbnail': 'vr_square.jpg',
        'path': 'performing_vr',
        'template': 'performing_vr.html',
        'date': 'fall 2016',
        'type': 'interactive_art',
    },
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
        'type': 'sound',
    },
    {
        'name': 'Intel Connect Anything Prototyping Kit',
        'thumbnail': 'galileo_w_pin.jpg',
        'path': 'intel',
        'template': 'intel.html',
        'date': '2014',
        'type': 'industry',
    },
    {
        'name': 'WaaZam!',
        'thumbnail': 'waazam_space.png',
        'path': 'waazam',
        'template': 'waazam.html',
        'date': '2013',
        'type': 'research_collab',
    },
    {
        'name': 'Defamiliarizing Sound with Granular Synthesis',
        'thumbnail': 'IMG_E1207_square.JPG',
        'path': 'sounds',
        'template': 'sounds.html',
        'date': 'ongoing',
        'type': 'sound',
    },
    {
        'name': 'Harmonograph Visualizer',
        'thumbnail': 'lissa2.png',
        'path': 'lissa',
        'template': 'lissajous.html',
        'date': '2013',
        'type': 'sound',
    },
    {
        'name': 'Chladni Waves Visualizer',
        'thumbnail': 'chladni2.png',
        'path': 'chladni',
        'template': 'chladni.html',
        'date': '2013',
        'type': 'sound',
    },
    {
        'name': 'Smart Bamboo Blinds for Bali',
        'thumbnail': 'bali_house.jpg',
        'path': 'bamboo_blinds',
        'template': 'bali.html',
        'date': 'May 2014',
        'type': 'ictd',
    },
    {
        'name': 'Mobile Phones & Illiteracy in Morocco',
        'thumbnail': 'apples.jpg',
        'path': 'moblit',
        'template': 'mobile_illiteracy.html',
        'date': '2012',
        'type': 'ictd',
    },
    {
        'name': 'Solar Cooker for the Himalayas',
        'thumbnail': 'solsource.jpg',
        'path': 'solsource',
        'template': 'solar_cooker.html',
        'date': '2010',
        'type': 'ictd',
    },
#    {
#        'name': 'Biosignals Experiments',
#        'thumbnail': 'peacebone_gsr.png',
#        'path': 'biosignals',
#        'template': 'biosignals.html',
#        'date': '',
#        'type': 'sound',
#    },
    {
        'name': 'Music & Data at The Echo Nest',
        'thumbnail': 'en.png',
        'path': 'the_echo_nest',
        'template': 'echonest.html',
        'date': '2012 - 2013',
        'type': 'industry',
    },
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
        'name': 'hint',
        'cite': """<b>Noura Howell</b>, Laura Devendorf, Rundong (Kevin) Tian, Tom&aacute;s Vega G&aacute;lvez, Nan-Wei Gong, Ivan Poupyrev, Eric Paulos, Kimiko Ryokai. 2016. Biosignals as social cues: Ambiguity and emotional interpretation in social displays of skin conductance. <i>Designing Interactive Systems (DIS'16)</i>.""",
        'pdf': '/static/pdf/16_DIS_Hint.pdf',
        'url': 'https://dl.acm.org/citation.cfm?id=2901850',
    },
    {
        'name': 'teachable_machine',
        'cite': """Michelle Carney, Barron Webster, Irene Alvarado, Kyle Phillips, <b>Noura Howell</b>, Jordan Griffith, Jonas Jongejan, Amit Pitaru, Alexander Chen. 2020. Teachable Machine: Approachable Web-Based Tool for Exploring Machine Learning Classification. <i>Late-Breaking Works of Human Factors in Computing Systems (CHI'20)</i>.""",
        'pdf': '/static/pdf/2020_CHI_LBW_Teachable_Machine.pdf',
        'url': 'https://dl.acm.org/doi/abs/10.1145/3334480.3382839',
    },
    {
        'name': 'design_futuring',
        'cite': """Sandjar Kozubaev, Chris Elsden, <b>Noura Howell</b>, Marie Louise Juul S&oslash;ndergaard, Nick Merrill, Britta Schulte, Richmond Y. Wong. 2020. Expanding Modes of Reflection in Design Futuring. <i>Human Factors in Computing Systems (CHI'20)</i>.""",
        'pdf': '/static/pdf/2020_CHI_Design_Futuring.pdf',
        'url': 'https://dl.acm.org/doi/abs/10.1145/3313831.3376526',
    },
    {
        'name': 'vivewell',
        'cite': """Sarah Fox, <b>Noura Howell</b>, Richmond Wong, Franchesca Spektor. 2019. Vivewell: Speculating Near-Future Menstrual Tracking through Current Data Practices. <i>Designing Interactive Systems Pictorials (DIS'19)</i>.""",
        'pdf': '/static/pdf/19_DIS_Vivewell.pdf',
        'url': 'https://dl.acm.org/citation.cfm?id=3323695',
    },
    {
        'name': 'vivewell_zine',
        'cite': """Sarah Fox, <b>Noura Howell</b>, Richmond Wong, Franchesca Spektor. 2019. Vivewell: Winter Product Catalog.""",
        'pdf': '/static/pdf/19_Zine_Vivewell.pdf',
        'url': None,
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
