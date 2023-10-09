from pathlib import Path
from src.locales import Locale


class I18N:
    def __init__(self, path: Path, locale: Locale):
        self.path = path if isinstance(path, Path) else Path(path)
        self.locale = locale

        if not self.path.is_dir():
            raise SystemError("Locale path has to be a directory.")

    def _load_translations(self, locale: Locale):
        translations = {}
        locale_directory = self.path / locale.value

        if not locale_directory.is_dir():
            raise SystemError(f"Locale directory for {locale.value} not found.")

        for file_path in locale_directory.iterdir():
            if file_path.is_file():
                with open(file_path, "r", encoding="UTF-8") as f:
                    translation_data = f.read()

                translations[file_path.stem] = translation_data

        return translations

    def get_all_translations(self, locale: Locale):
        translations = self._load_translations(locale)
        for key, value in translations.items():
            print(f"{key} - {value}")

    def get_translation(self, translation: str, locale: Locale):
        translations = self._load_translations(locale)
        return translations[translation]
