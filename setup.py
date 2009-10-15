try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='MapFishSample',
    version='1.3dev',
    description='',
    author='',
    author_email='',
    #url='',
    install_requires=[
        "mapfish>=1.3dev,<=1.3.99",
    ],
    setup_requires=["PasteScript==dev,>=1.6.3dev-r7326"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'mapfishsample': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'mapfishsample': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['MapFish', 'PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = mapfishsample.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
