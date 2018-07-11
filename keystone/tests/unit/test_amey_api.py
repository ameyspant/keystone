# Copyright 2016 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import uuid

import testtools
import keystone.conf
from testtools import testcase
from testtools import matchers
from keystone import exception
from keystone.amey_api import myapi
from keystone.tests import unit
from keystone.tests.unit import test_v3
from keystone.tests.unit import test_v3_auth
import json

CONF = keystone.conf.CONF


class TestAmey(test_v3.RestfulTestCase):

    def ameysetUp(self):
        super(TestAmey, self).setUp()

    def test_amey_validate_list_data(self):
        auth_data = self.build_authentication_request(
            user_id=uuid.uuid4().hex,
            password=self.user['password'],
            project_id=self.project_id)
        r = self.get('/amey_api/myapi')
        self.assertIn('project',r.result)
        self.assertIn('domain',r.result)
        self.assertIn('role',r.result)
        self.assertIn('user',r.result)

