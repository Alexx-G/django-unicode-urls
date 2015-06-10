from .urlutils import any_path_re


def patch_djangocms_urls():
    import cms.utils.urlutils as cms_urlutils

    cms_urlutils.any_path_re = any_path_re
