from .renderers import ContentRenderer, TemplateRenderer
from slugify import slugify
from collections import defaultdict
from datetime import datetime
import yaml
import os


class Builder:
    def __init__(self, config=None):
        self.folders = {
            'content': 'content',
            'output': 'output',
            'templates': 'templates',
        }
        self.page_defaults = {}
        self.site = {}

        if config is not None:
            # Aha! We have a config, lets update accordingly.
            self.folders.update(config.get('folders', {}))
            self.site.update(config.get('site', {}))
            self.page_defaults.update(config.get('page_defaults', {}))

        self.template_renderer = TemplateRenderer(self.folders['templates'])

    def run(self):
        pages = make_pages(self.page_paths(), self.page_defaults)
        pages = list(pages)

        self.site['pages'] = pages
        self.site['categories'] = page_categories(pages)

        self.site['groups'] = {
            field: groups for field, groups in group_pages(self.site, pages)
        }

        give_subpages(self.site)

        self.write_pages()

    def page_paths(self):
        for folder, folders, files in os.walk(self.folders['content']):
            for file_name in files:
                yield os.path.join(folder, file_name)

    def write_pages(self):
        for page in self.site['pages']:
            destination = build_destination(page, self.folders['output'])
            destination_folder = os.path.dirname(destination)
            html_page = self.template_renderer.render_page(page, self.site)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            with open(destination, 'w+') as output:
                output.write(html_page)


def build_destination(page, folder):
    if page['url'].startswith('/'):
        dest_template = '{folder}{path}'
    else:
        dest_template = '{folder}/{path}'

    _, extension = os.path.splitext(page['url'])
    if not extension:
        # This is a pretty url that points at a directory.
        # Add index.html to the destination.
        dest_template = os.path.join(dest_template, 'index.html')
    return dest_template.format(
        folder=folder,
        path=page['url'],
    )


def page_categories(pages):
    categories = defaultdict(list)
    for page in pages:
        categories[page['category']].append(page)
    return categories


def make_pages(paths, page_defaults):
    for path in paths:
        page = make_page(path, page_defaults)
        if page:
            yield page


def give_subpages(site):
    for page in site['pages']:
        if 'subpages' not in page:
            continue
        subpage_group = page['subpages']['group']
        page['subpages'] = site['groups'][subpage_group]


def make_page(path, page_defaults):
    page = {}
    page.update(page_defaults)
    with open(path) as f:
        raw = f.read().split('---')

        page_config = yaml.load(raw[0]) or {}

        try:
            page['content'] = raw[1]
        except:
            page['content'] = None

        if not page_config.get('published', True):
            return

        page.update(page_config)

        if 'multipage' in page and page['multipage']:
            return page

        # make slugs
        page['slug'] = make_slug(page)

        # make dates
        page['date'] = make_date(page)

        # make urls
        page['url'] = make_url(page)
    return page


def make_slug(page):
    if 'slug' in page:
        return page['slug']
    elif 'title' in page:
        return slugify(page['title'].lower())
    else:
        # Erh. What else can we build slugs from?
        pass


def make_url(page):
    if 'url' in page:
        return page['url']
    elif 'url_pattern' in page:
        return page['url_pattern'].format(**page)
    else:
        # Oh oh, there is not even any url_pattern.
        # Throw exception, since we need something to make urls from.
        pass


def make_date(page):
    if 'date' in page:
        return page['date']
    else:
        return datetime.utcnow()


def group_pages(site, pages):
    for field in site.get('grouping', []):
        grouping = defaultdict(list)
        for page in pages:
            if field not in page:
                continue
            if not isinstance(page[field], list):
                values = [page[field]]
            else:
                values = page[field]
            for value in values:
                grouping[value].append(page)
        yield field, grouping
