
__version__ = '0.2.1'


from encomp.settings import SETTINGS

if SETTINGS.type_checking:

    from typeguard.importhook import install_import_hook

    # installs the @typechecked decorator on all functions imported after this
    install_import_hook('encomp')
