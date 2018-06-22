from oslo_config import cfg
from keystone.conf import utils

host = cfg.StrOpt('host',
                  default='localhost',
                  help=utils.fmt('IP/hostname to listen on.'))
port = cfg.PortOpt('port',
                    default=5672,
                    help=utils.fmt('Port number to listen on.'))

GROUP_NAME = __name__.split('.')[-1]
ALL_OPTS = [
    host,
    port,
]



def register_opts(conf):
    conf.register_opts(ALL_OPTS, group=GROUP_NAME)

def list_opts():
    return {GROUP_NAME: ALL_OPTS}
