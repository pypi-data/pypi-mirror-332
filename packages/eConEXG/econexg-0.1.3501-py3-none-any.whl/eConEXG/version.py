version = "0.1.3501"
__version__ = version
full_version = version

release = "dev" not in version and "+" not in version
short_version = version.split("+")[0]
