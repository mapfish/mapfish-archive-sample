try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='MapFishSample',
    version="",
    #description="",
    #author="",
    #author_email="",
    #url="",
    install_requires=["Pylons>=0.9.5"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'mapfishsample': ['i18n/*/LC_MESSAGES/*.mo']},
    entry_points="""
    [paste.app_factory]
    main = mapfishsample.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
