from certx import app
from certx.common import service
from certx.conf import CONF

from certx.db.sqlalchemy import models as db_model


def start():
    service.prepare_command()

    with app.app_context():
        db_model.init_db()

    app.run(host=CONF.host, port=CONF.port, debug=CONF.flask.debug, threaded=CONF.flask.threaded)


if __name__ == '__main__':
    start()
