import os
from distutils.command.build import build

from django.core import management
from setuptools import find_packages, setup

from pretix_custom_css_js import __version__


try:
    with open(
        os.path.join(os.path.dirname(__file__), "README.rst"), encoding="utf-8"
    ) as f:
        long_description = f.read()
except Exception:
    long_description = ""


class CustomBuild(build):
    def run(self):
        management.call_command("compilemessages", verbosity=1)
        build.run(self)


cmdclass = {"build": CustomBuild}


setup(
    name="pretix-custom-css-js",
    version=__version__,
    description="Add custom CSS and JS to your pretix installation.",
    long_description=long_description,
    url="https://github.com/pretix-unofficial/pretix-custom-css-js",
    author="Your name",
    author_email="Your email",
    license="Apache",
    install_requires=[],
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
pretix_custom_css_js=pretix_custom_css_js:PretixPluginMeta
""",
)
