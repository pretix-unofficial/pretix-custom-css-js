from django.utils.translation import gettext_lazy
from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    name = "pretix_custom_css_js"
    verbose_name = "Custom CSS and JS"

    class PretixPluginMeta:
        name = gettext_lazy("Custom CSS and JS")
        author = "Your name"
        description = gettext_lazy("Add custom CSS and JS to your pretix installation. Please be very careful as future updates to pretix – especially its HTML-templates – may break your CSS and/or JS.")
        visible = True
        version = __version__
        category = "CUSTOMIZATION"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA


