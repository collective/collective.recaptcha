from operator import attrgetter
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

LANGUAGES = dict([
    (u'Arabic', 'ar'),
    (u'Bulgarian', 'bg'),
    (u'Catalan', 'ca'),
    (u'Chinese (Simplified)', 'zh-CN'),
    (u'Chinese (Traditional)', 'zh-TW'),
    (u'Croatian', 'hr'),
    (u'Czech', 'cs'),
    (u'Danish', 'da'),
    (u'Dutch', 'nl'),
    (u'English (UK)', 'en-GB'),
    (u'English (US)', 'en'),
    (u'Filipino', 'fil'),
    (u'Finnish', 'fi'),
    (u'French', 'fr'),
    (u'French (Canadian)', 'fr-CA'),
    (u'German', 'de'),
    (u'German (Austria)', 'de-AT'),
    (u'German (Switzerland)', 'de-CH'),
    (u'Greek', 'el'),
    (u'Hebrew', 'iw'),
    (u'Hindi', 'hi'),
    (u'Hungarain', 'hu'),
    (u'Indonesian', 'id'),
    (u'Italian', 'it'),
    (u'Japanese', 'ja'),
    (u'Korean', 'ko'),
    (u'Latvian', 'lv'),
    (u'Lithuanian', 'lt'),
    (u'Norwegian', 'no'),
    (u'Persian', 'fa'),
    (u'Polish', 'pl'),
    (u'Portuguese', 'pt'),
    (u'Portuguese (Brazil)', 'pt-BR'),
    (u'Portuguese (Portugal)', 'pt-PT'),
    (u'Romanian', 'ro'),
    (u'Russian', 'ru'),
    (u'Serbian', 'sr'),
    (u'Slovak', 'sk'),
    (u'Slovenian', 'sl'),
    (u'Spanish', 'es'),
    (u'Spanish (Latin America)', 'es-419'),
    (u'Swedish', 'sv'),
    (u'Thai', 'th'),
    (u'Turkish', 'tr'),
    (u'Ukrainian', 'uk'),
    (u'Vietnamese', 'vi')])

THEMES = dict([
    (u'Dark', 'dark'),
    (u'Light', 'light')])


def available_themes(context):
    items = [SimpleTerm(value=value, token=str(value), title=title)
             for title, value in THEMES.items()]
    items.sort(key=attrgetter('title'))
    return SimpleVocabulary(items)


def available_languages(context):
    items = [SimpleTerm(value=value, token=str(value), title=title)
             for title, value in LANGUAGES.items()]
    items.sort(key=attrgetter('title'))
    return SimpleVocabulary(items)

