try:
    VERSION = __import__("pkg_resources").get_distribution(__name__).version
except Exception as e:
    VERSION = "0.0.1"
