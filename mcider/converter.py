""" mcider - converter
Copyright(c) 2012 ogom

slide maker
"""
import os
import shutil
from markdown import markdown
import util

class Slide():
    """ Create a slide from the content and theme. """

    def __init__(self, contents=None, theme=None):
        self.contents = contents
        self.theme = theme
        
    def maker(self, path=None):
        template = self._get_template(path)
        slide = self._get_slide()
        return template.replace('{{ slide }}', slide)

    def _get_template(self, path=None):
        """ copy theme assets and read base.html """
        theme = self.theme
        theme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'themes', theme))

        assets = ['css', 'js', 'images']
        for asset in assets:
            src_path = os.path.join(theme_path, asset)
            if os.path.isdir(src_path):
                dst_path = os.path.join(path, asset)
                if not os.path.isdir(dst_path):
                    shutil.copytree(src_path, dst_path)
        return util.fs_reader(os.path.join(theme_path, 'base.html'))

    def _get_slide(self, extensions=None):
        theme = self.theme
        html = None

        if theme == 'io2011':
            html = self._get_slide_io2011(extensions)
        elif theme == 'io2012':
            html = self._get_slide_io2012(extensions)
        else:
            html = self._get_slide_none(extensions)
        return html

    def _get_slide_none(self, extensions=None):
        """ none style """
        contents = self.contents
        pages = markdown(contents) + '\n'
        slides = pages.split('<hr />\n')

        html = '\n'
        for slide in slides:
            html += '<article>\n'
            html += slide
            html += '</article>\n\n'
        return html

    def _get_slide_io2012(self, extensions=None):
        """ io-2012 style """
        contents = self.contents
        splits = [
            {'horizon': '---', 'style': 'none'},
            {'horizon': '___', 'style': 'smaller'},
            {'horizon': '***', 'style': 'fill'}
        ]

        styles = []
        for split in splits:
            styles.append(split['style'])
            horizon = '\n' + split['horizon'] + '\n'
            contents = contents.replace(horizon, '\n---\n' + split['style'] + '\n')

        pages = contents.split('\n---\n')

        slides = []
        for page in pages:
            sections = page.split('\n\n', 2)
            slide = {}
            if not sections[0] in styles:
                sections.insert(0, 'none')
            slide['style'] = sections[0]
            if len(sections) > 1:
                slide['hgroup'] = sections[1]
            if len(sections) > 2:
                slide['article'] = sections[2]
            slides.append(slide)

        html = '\n'
        for slide in slides:
            html += '<slide>\n'
            if slide.has_key('hgroup'):
                html += '<hgroup>\n'
                html += markdown(slide['hgroup']) + '\n'
                html += '</hgroup>\n'
            if slide.has_key('article'):
                html += '<article class="' + slide['style'] + '">\n'
                html += markdown(slide['article']) + '\n'
                html += '</article>\n'
            html += '</slide>\n\n'
        return html

    def _get_slide_io2011(self, extensions=None):
        """ io-2011 style """
        contents = self.contents
        splits = [
            {'horizon': '---', 'style': 'none'},
            {'horizon': '___', 'style': 'smaller'},
            {'horizon': '***', 'style': 'fill'}
        ]

        styles = []
        for split in splits:
            styles.append(split['style'])
            horizon = '\n' + split['horizon'] + '\n'
            contents = contents.replace(horizon, '\n---\n' + split['style'] + '\n')

        pages = contents.split('\n---\n')

        slides = []
        for page in pages:
            sections = page.split('\n\n', 1)
            slide = {}
            if not sections[0] in styles:
                sections.insert(0, 'none')
            slide['style'] = sections[0]
            if len(sections) > 1:
                slide['article'] = sections[1]
            slides.append(slide)

        html = '\n'
        for slide in slides:
            if slide.has_key('article'):
                html += '<article class="' + slide['style'] + '">\n'
                html += markdown(slide['article']) + '\n'
                html += '</article>\n\n'
        return html
