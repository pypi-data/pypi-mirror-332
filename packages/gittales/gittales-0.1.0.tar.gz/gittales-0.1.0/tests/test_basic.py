def test_cli_imports():
    """Make sure we can import our CLI module."""
    try:
        from gittales import cli

        assert cli is not None
    except ImportError:
        assert False, "Failed to import the CLI module"


def test_version():
    """Check that we have a version defined."""
    from gittales import __version__

    assert __version__ is not None
    assert isinstance(__version__, str)
