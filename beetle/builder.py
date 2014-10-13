from .renderers import TemplateRenderer
from . import version, project_url, name, BeetleError
from .utils import read_folder
from slugify import slugify
from collections import defaultdict
from datetime import datetime
import yaml
import distutils.core
import os


class NoUrlError(BeetleError):
    pass


class GroupKey:
    def __init__(self, name):
        self.name = name
        self.slug = slugify(name)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class Builder:
    def __init__(self, config, content_renderer):
        self.about = {
            'name': name,
            'version': version,
            'url': project_url,
            'now': datetime.utcnow(),
        }

        self.folders = config.folders
        self.page_defaults = config.page_defaults
        self.site = config.site

        self.template_renderer = TemplateRenderer(
            self.folders['templates'],
            self.about,
        )
        self.content_renderer = content_renderer

    def __iter__(self):
        page_generator = read_folder(self.folders['content'], mode='r')
        # print(page_generator)
        pages = make_pages(page_generator, self.page_defaults)
        # pages = make_pages(self.page_paths(), self.page_defaults)
        # pages = list(pages)

        self.site['pages'] = list(pages)

        self.site['groups'] = {
            field: groups for field, groups in group_pages(self.site)
        }

        give_subpages(self.site)

        render_pages(self.site['pages'], self.content_renderer)

        for page in self.site['pages']:
            destination = build_destination(page, self.folders['output'])
            html_page = self.template_renderer.render_page(page, self.site)
            yield destination, html_page.encode('utf-8')


def build_destination(page, folder):
    url = page['url']

    _, extension = os.path.splitext(url)
    if not extension:
        # This is a pretty url that points at a directory.
        # Add index.html to the destination.
        url = url + 'index.html'

    if url.startswith('/'):
        url = url[1:]
    return url


def make_pages(paths, page_defaults):
    for path, raw_content in paths:
        page = make_page(path, raw_content, page_defaults)
        if page:
            yield page


def give_subpages(site):
    for page in site['pages']:
        if 'subpages' not in page:
            continue
        primary, secondary = page['subpages'].split('.')
        if secondary == '*':
            page['subpages'] = site['groups'][primary]
        else:
            secondary_key = GroupKey(name=secondary)
            page['subpages'] = site['groups'][primary][secondary_key]


def make_page(path, raw_content, page_defaults):
    page = {}
    page.update(page_defaults)
    _, extension = os.path.splitext(path)
    page['extension'] = extension.strip('.')

    raw = raw_content.split('---', 1)

    page_config = yaml.load(raw[0]) or {}

    try:
        page['raw_content'] = raw[1]
    except:
        page['raw_content'] = None

    if not page_config.get('published', True):
        return

    page.update(page_config)

    # include the path
    page['path'] = path

    # make slug
    page['slug'] = make_slug(page)

    # make url
    page['url'] = make_url(page)
    return page


def make_slug(page):
    if 'slug' in page:
        return page['slug']
    elif 'title' in page:
        return slugify(page['title'].lower())
    else:
        # Erh. What else can we build slugs from?
        return None


def make_url(page):
    if 'url' in page:
        return page['url']
    elif 'url_pattern' in page:
        try:
            return page['url_pattern'].format(**page)
        except KeyError as err:
            msg = 'Missing field for url_pattern in file: {}'.format(
                page['path']
            )
            raise NoUrlError(msg, page)
    else:
        # Oh oh, beetle cannot make urls out of thin air.
        # This page does not belong anywhere.
        msg = 'No url or url_pattern, in file: {}'.format(
            page['path']
        )
        raise NoUrlError(msg, page=page)


def group_pages(site):
    for options in site.get('grouping', []):
        field = options['field']
        name = options.get('name', field)
        reverse = options.get('order') == 'desc'
        sort_key = options.get('key')

        grouping = defaultdict(list)
        for page in site['pages']:
            if field not in page:
                continue
            if not isinstance(page[field], list):
                if isinstance(page[field], GroupKey):
                    key = page[field]
                else:
                    value = page[field]
                    key = GroupKey(name=value)
                page[field] = key
                grouping[key].append(page)
            else:
                values = page[field]
                page[field] = []
                for value in values:
                    key = GroupKey(name=value)
                    page[field].append(key)
                    grouping[key].append(page)

        for key, pages in grouping.items():
            sort_lambda = lambda p: p[sort_key]
            grouping[key] = sorted(pages, key=sort_lambda, reverse=reverse)
        yield name, grouping


def render_pages(pages, renderer):
    for page in pages:
        page['content'] = renderer.render(page)
