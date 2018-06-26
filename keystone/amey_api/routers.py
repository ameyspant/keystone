from keystone.amey_api import myapi
from keystone.common import wsgi


class Routers(wsgi.RoutersBase):

    def append_v3_routers(self, mapper, routers):
        amey_controller = myapi.Amey()

        self._add_resource(
            mapper, amey_controller,
            path='/amey_api/myapi',
            get_action='list_data')
