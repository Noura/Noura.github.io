#!/usr/local/bin/python3.9

import os, os.path, shutil, codecs, sys

import jinja2

import bibtexparser, json

# IMPORTING PUBLICATIONS FROM BIBTEX FILE
# Zotero, select citations, right click, export as bibtex UTF-8
# save file as data/zotero_export.bib

# some of the publications, i host pdfs for
# zoteroKey : filename
bibs_pdfs = {
    'howell_representation_2016': '16_DIS_DC.pdf',
    'howell_biosignals_2016': '16_DIS_Hint.pdf',
    'merrill_interrogating_2017': '17_DIS_Workshop_Biosensing.pdf',
    'howell_tensions_2018': '18_CHI_Ripple.pdf',
    'howell_emotional_2018': '18_CSCW_Emotional_Biosensing.pdf',
    'howell_life-affirming_2019': '19_CHI_Heart_Sounds_Bench.pdf',
    'fox_vivewell_2019': '19_DIS_Vivewell.pdf',
    'carney_teachable_2020': '2020_CHI_LBW_Teachable_Machine.pdf',
    'tsaknaki_challenges_2020': '2020_NordiCHI_Workshop_Biodata_as_Material.pdf',
    'howell_calling_2021': '2021_alt.chi_Plurality_Perspectives_Design_Futuring.pdf',
    'kozubaev_expanding_2020': '2020_CHI_Design_Futuring.pdf',
    'howell_cracks_2021': '2021_TOCHI_Rethinking_Failure_in_Design_Research.pdf',
    'sanches_diffraction_2022': '2022_CHI_Diffraction-in-action.pdf',
    'sharmaDesignFuturingLove2022': '2022_alt.chi_Design_Futuring_for_Love_Friendships_and_Kinships.pdf',
    'tsaknakiFabulatingBiodataFutures2022a': '2022_DIS_Fabulating_Biodata_Futures.pdf',
    'howellFeelingAirExploring2022': '2022_NordiCHI_Inflatables.pdf',
    'sondergaardFabulationApproachDesign2023': '2023_Fabulation_for_Design_Futuring.pdf',
    'riggsRedRedactedTheatre2024': '2024_DIS_Red_Redacted_Theatre.pdf',
    'kozubaevTuningListeningCurrent2024': '2024_DIS_Remote_Ritual_Practice.pdf',
    'janickiCripReflectionsDesigning2024': '2024_DIS_Crip_Reflections_on_Designing_with_Plants.pdf',
    'howellReflectiveDesignInformal2024': '2024_NordiCHI_Reflective_Design_for_Informal_Audits.pdf',
    'ichihashiHydropticalThermalFeedback2024': '2024_UIST_Hydroptical.pdf',
    'sharmaPromotingCriticalityDesign2024': '2024_NordiCHI_Criticality_Design_Futuring.pdf',
}
pdf_path = '/static/pdf/'

# jinja does not handle utf-8 well it seems. some author names require utf-8.
# i will scrub for the accented characters i know are in my co-authors' names
# and replace them with the corresponding HTML, using this mapping
# TODO find an actual official table for this instead of rolling my own
utf8_to_HTML_char_map = {
        u'á': '&aacute;',
        u'ó': '&oacute;',
        u'ø': '&oslash;',
}

# parse bibtex
with open('data/zotero_export.bib', 'r', encoding='utf-8') as bibtex_file:
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.customization = bibtexparser.customization.convert_to_unicode
    bibs = bibtexparser.load(bibtex_file, parser=parser)
    for entry in bibs.entries:
        for utf8_char, html_char in utf8_to_HTML_char_map.items():
            entry['author'] = entry['author'].replace(utf8_char, html_char)
        if entry['ID'] in bibs_pdfs:
            entry['pdf'] = pdf_path + bibs_pdfs[entry['ID']]

# get publications as a list and as a dictionary
# dictionary IDs are the Zotero IDs
bibs_list = bibs.entries
bibs_by_ID = {}
for entry in bibs_list:
    bibs_by_ID[entry['ID']] = entry


from data import news
news = news.news

from data import projects
from data import teaching
from data import alt_text_for_images

vars_for_template = {
    'ctx': {
        'page': {},
        'news': news,
        'bibs_list': bibs_list,
        'bibs_by_ID': bibs_by_ID,
        'alt': alt_text_for_images.alt_text,
    }
}

def make_tiled_pages(here, templates, rel_path, pages):
    for page in pages:
        vars_for_template['ctx']['pages'] = pages
        vars_for_template['ctx']['page'] = page
        tem = templates.get_template(page['template'])
        with codecs.open(os.path.join(here, rel_path, page['path']+'.html'), 'w', encoding='utf-8') as out:
            out.write(tem.render(**vars_for_template))


def make_top_level_page(here, templates, rel_path, this_template, pages=None):
    if rel_path != '':
        shutil.rmtree(os.path.join(here, rel_path), ignore_errors=True )
        os.mkdir(rel_path)

    if pages:
        vars_for_template['ctx']['pages'] = pages

    tem = templates.get_template(this_template)

    path = os.path.join(here, rel_path, 'index.html')

    with codecs.open(path, 'w', encoding='utf-8') as out:
        out.write(tem.render(**vars_for_template))

def make_pages():
    here = os.path.dirname(__file__)
    loader = jinja2.FileSystemLoader(os.path.join(here, 'templates'))
    templates = jinja2.Environment(loader=loader)

    # HOMEPAGE #######################################
    make_top_level_page(here, templates, '', 'home.html', projects.pages)

    # PUBLICATIONS PAGE ################################
    make_top_level_page(here, templates, 'pubs', 'publications.html')

    # CV PAGE ##########################################
    make_top_level_page(here, templates, 'cv', 'cv.html')

    # TEACHING PAGE ####################################
    make_top_level_page(here, templates, 'teaching', 'teaching.html', teaching.pages)

    # ABOUT PAGE #######################################
    make_top_level_page(here, templates, 'about', 'about.html')

    # NEWS PAGE ########################################
    make_top_level_page(here, templates, 'news', 'news.html')

    # PROJECTS PAGES ###################################
    # assumes projects dir already exists, so first delete it to clear contents
    shutil.rmtree(os.path.join(here, 'projects'), ignore_errors=True )
    # then recreate it empty to put in the updated project pages
    os.mkdir('projects')
    make_tiled_pages(here, templates, 'projects', projects.pages)

    # TEACHING PAGES ###################################
    # teaching dir should already exist from making the top level teaching page
    make_tiled_pages(here, templates, 'teaching', teaching.pages)

    print("make_pages()")

if __name__ == '__main__':
    make_pages()
