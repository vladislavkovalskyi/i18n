from src import I18N
from src.locales import Locale

i18n = I18N("../tests/locales", Locale.RU)
i18n.get_all_translations(Locale.RU)

print(f"hello ru: {i18n.get_translation('hello', Locale.RU)}")
print(f"hello en: {i18n.get_translation('hello', Locale.EN)}")
print(f"bye ru: {i18n.get_translation('bye', Locale.RU)}")
print(f"bye en: {i18n.get_translation('bye', Locale.EN)}")
