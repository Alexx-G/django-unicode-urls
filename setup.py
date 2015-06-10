from distutils.core import setup

LONG_DESC = """
Unicode URLS in django."""

setup(
    name='unicode_urls',
    packages=['unicode_urls'],
    version='0.0.1',
    long_description=LONG_DESC,
    description='Unicode urls.',
    author='Alex Gavrisco',
    author_email='a.gavrisco@dekart.com',
    url='',
    download_url='',
    keywords=['django', 'urls', 'unicode', 'cms', 'djangocms', 'django-cms'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Development Status :: Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        ],
    install_requires=[
    ]
    )
