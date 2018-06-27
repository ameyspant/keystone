import keystone.conf
from keystone.common import controller
from keystone.common import wsgi
from oslo_log import log




LOG = log.getLogger(__name__)
CONF = keystone.conf.CONF


class Amey(controller.V3Controller):
    collection_name = 'amey_api'
    member_name = 'myapi'
    def __init__(self):
        super(Amey, self).__init__()

    @controller.protected()
    def list_data(self, request):
        #return ('amey')
        #data = dict()
        #data[0] = "amey"
        data={'host': CONF.amey.host,'port': CONF.amey.port}
        return wsgi.render_response(body=data)
        #return wsgi.render_response(body = data)
LOG.debug("Debug")



