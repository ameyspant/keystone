import keystone.conf
from keystone.common import controller
from keystone.common import wsgi
from oslo_log import log
from keystone.identity import controllers

from keystone.common import dependency



LOG = log.getLogger(__name__)
CONF = keystone.conf.CONF

@dependency.requires('identity_api', 'assignment_api')
class Amey(controller.V3Controller):
    collection_name = 'amey_api'
    member_name = 'myapi'
    def __init__(self):
        super(Amey, self).__init__()

    @controller.protected()
    def list_data(self, request):
        user_id = request.auth_context.get('user_id')

        ref = self.identity_api.get_user(user_id)
        roles = self.assignment_api.list_role_assignments(user_id=user_id,effective=True)
        user_refs = self.assignment_api.list_projects_for_user(user_id)
        domain_refs = self.assignment_api.list_domains_for_user(user_id)
        data = {'user': ref,'project': user_refs,'domain':domain_refs,'role':roles}
        return wsgi.render_response(body=data)

        #data =  {'user': self.v3_to_v2_user(ref)}
        #return wsgi.render_response(body=data)
        #return wsgi.render_response(body = data)
LOG.debug("Debug")



