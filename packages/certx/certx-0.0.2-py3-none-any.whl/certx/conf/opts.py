from certx import conf

_opts = [
    ('DEFAULT', conf.default.list_opts()),
    ('certificate_repository', conf.certificate_repository.certificate_repository_opts),
    ('certificate_file_repository', conf.certificate_repository.certificate_file_repository_opts),
    ('flask', conf.flask.opts),
]


def list_opts():
    return _opts
