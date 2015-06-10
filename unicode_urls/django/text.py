import unicodedata
from django.utils.safestring import mark_safe


def slugify(value):
    """
    Unicode version of standart slugify.
    Converts spaces to hyphens. Removes characters that
    aren't unicode letters, underscores, or hyphens. Converts to lowercase.
    Also replaces whitespace with huphen and
    strips leading and trailing whitespace.
    :param value: String to slugify.
    :type value: str
    :returns: Slugified value.
    :rtype: str
    """
    value = unicodedata.normalize('NFKD', value)
    value = unicode(re.sub('(?u)[^\w\s-]+', '', value).strip().lower())
    return mark_safe(re.sub('[-\s]+', '-', value).strip('-'))
