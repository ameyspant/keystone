import keystone.conf
from keystone.common import controller
from oslo_log import log




LOG = log.getLogger(__name__)
CONF = keystone.conf.CONF


class Amey(controller.V3Controller):
    collection_name = 'amey_api'
    member_name = 'amey'
    def __init__(self):
        super(Amey, self).__init__()
    @controller.protected()
    def list_data(self, request):
        return {{'host': CONF.amey.host},{'port': CONF.amey.port}}

LOG.debug("Debug")
