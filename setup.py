from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

VERSION = '0.1'

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']


setup(
    name='django-form-template-generator',
    version=VERSION,
    description="Generates Django Template code for all fields of a form so they can be customised afterwords",
    long_description="",
    author="Francois Constant",
    author_email="francois@piran.com.au",
    url="http://github.com/FrancoisConstant/django-form-template-generator",
    license="MIT License",
    platforms=["any"],
    packages=['form_template_generator'],
    #data_files=[(template_dir, templates)],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
)
