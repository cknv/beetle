from jinja2 import Environment, FileSystemLoader


class TemplateRenderer:
    def __init__(self, template_folder):
        self.env = Environment(loader=FileSystemLoader(template_folder))

    def render_page(self, page, site):
        template = self.env.get_template('template.html')
        # print(page)
        return template.render(page=page, site=site)


def render_plain(raw_content):
    return raw_content


class ContentRenderer:
    renderes = {
        None: render_plain,
        # 'md': 'markdown',
        # 'rst': 'reStructuredText',
    }

    def render(self, page):
        return self.renderes[page.extension](page.raw_content)
