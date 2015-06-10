from .text import slugify
from .validators import slug_re


def patch_django_urls():
    import django.utils.text as django_text
    import django.core.validators as django_validators

    django_text.slugify = slugify
    django_validators.slug_re = slug_re
