from oslo_config import cfg

from certx.conf import certificate_repository
from certx.conf import default
from certx.conf import flask

CONF = cfg.CONF

certificate_repository.register_opts(CONF)
default.register_opts(CONF)
flask.register_opts(CONF)
