from jinja2 import Environment, FileSystemLoader
import markdown
import os


class TemplateRenderer:
    def __init__(self, template_folder, beetle_about):
        self.beetle_about = beetle_about
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
        template = self.templates[page['type']]
        return template.render(page=page, site=site, beetle=self.beetle_about)


def render_plain(raw_content):
    return raw_content


class ContentRenderer:
    renderers = {}

    def render(self, page):
        return self.renderers[page['extension']](page['raw_content'] or '')

    def add_renderer(self, extensions, function):
        for extension in extensions:
            self.renderers[extension] = function

    @classmethod
    def default(cls):
        instance = cls()

        # Plain
        plain_extensions = [None, '', 'txt']
        instance.add_renderer(plain_extensions, render_plain)

        return instance
