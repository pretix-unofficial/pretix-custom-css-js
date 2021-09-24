
from django.contrib.staticfiles import finders
from django.dispatch import receiver
from django.template.loader import get_template
from pretix.presale.signals import html_footer, sass_postamble, sass_preamble


@receiver(sass_preamble, dispatch_uid="pretix_custom_css_js_sass_preamble")
def r_sass_preamble(sender, **kwargs):
    with open(finders.find('pretix_custom_css_js/preamble.scss'), 'r') as fp:
        return fp.read()


@receiver(sass_postamble, dispatch_uid="pretix_custom_css_js_sass_postamble")
def r_sass_postamble(sender, filename, **kwargs):
    if filename == "main.scss":
        with open(finders.find('pretix_custom_css_js/postamble.scss'), 'r') as fp:
            return fp.read()
    elif filename == "widget.scss":
        with open(finders.find('pretix_custom_css_js/widget.scss'), 'r') as fp:
            return fp.read()
    return ""


@receiver(html_footer, dispatch_uid="pretix_custom_css_js_html_footer")
def html_foot_presale(sender, request=None, **kwargs):
    template = get_template("pretix_custom_css_js/presale_footer.html")
    return template.render()
