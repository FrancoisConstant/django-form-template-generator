from importlib import import_module
from django.core.management.base import BaseCommand
from form_template_generator.generator import Generator


class Command(BaseCommand):
    """
    Generate Templates fieldset based on included fields
    """

    args = '<module_name class_name>'
    help = """Generate Templates fieldset based on included fields
ex: ./manage.py generate_form_template my_app.forms MyForm"""

    def handle(self, *args, **kwargs):
        if len(args) != 2:
            self.stderr.write("Takes exactly 2 arguments. The module name and the class name")
            return False

        module_name = args[0]
        class_name = args[1]

        try:
            module = import_module(module_name)
            form_instance = getattr(module, class_name)()
        except:
            self.stderr.write("Class not found - {0} / {1}".format(module_name, class_name))
            return False

        generator = Generator()
        html = generator.get_twitter_form(form=form_instance)

        self.stdout.write(html)