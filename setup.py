try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='MapFishSample',
    version='2.0dev',
    description='',
    author='',
    author_email='',
    #url='',
    install_requires=[
        "mapfish>=2.0dev,<=2.0.99",
        "GeoFormAlchemy>=0.1dev,<=0.1.99",
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'mapfishsample': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'mapfishsample': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    entry_points="""
    [paste.app_factory]
    main = mapfishsample.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
