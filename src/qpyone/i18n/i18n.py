import os

from babel.support import Translations

from qpyone.constants import BASE_DIR
from qpyone.render import templates

TRANSLATIONS = {
    "zh_CN": Translations.load(os.path.join(BASE_DIR, "locales"), locales=["zh_CN"]),
    "en_US": Translations.load(os.path.join(BASE_DIR, "locales"), locales=["en_US"]),
}

translations = TRANSLATIONS.get("zh_CN")


def set_locale(locale: str):
    global translations
    translations = TRANSLATIONS.get(locale) or TRANSLATIONS.get("en_US")
    templates.env.install_gettext_translations(translations)
    translations.install(locale)
