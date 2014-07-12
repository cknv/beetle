from jinja2 import Environment, FileSystemLoader
import os


class TemplateRenderer:
    def __init__(self, template_folder):
        self.env = Environment(loader=FileSystemLoader(template_folder))
        self.template_folder = template_folder
        self.templates = {
            name: template for name, template in self.load_templates()
        }

    def load_templates(self):
        for template_file in os.listdir(self.template_folder):
            name, extension = os.path.splitext(template_file)
            yield name, self.env.get_template(template_file)

    def render_page(self, page, site):
        return self.templates[page['category']].render(page=page, site=site)


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
