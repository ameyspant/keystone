import keystone.conf


CONF = keystone.conf.CONF


def list_data():
    return {{'host': CONF.amey.host},{'port': CONF.amey.port}}
