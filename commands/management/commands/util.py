import MySQLdb


def connect(user, passwd, host, port, basename=None):
    info = dict(
        user=user,
        passwd=passwd,
        host=host,
        port=int(port),
        autocommit=True,
        charset="utf8",
    )
    if basename is not None:
        info['db'] = basename

    db = MySQLdb.connect(**info)
    return db.cursor()
