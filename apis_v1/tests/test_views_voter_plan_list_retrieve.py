# apis_v1/test_views_voter_plan_list_retrieve.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.urls import reverse
from django.test import TestCase
import json

class WeVoteAPIsV1TestsVoterPlanListRetrieve(TestCase):
    databases = ["default", "readonly"]

    def setUp(self):
        self.generate_voter_device_id_url = reverse("apis_v1:deviceIdGenerateView")
        self.voter_create_url = reverse("apis_v1:voterCreateView")
        self.voter_plan_list_save_url = reverse("apis_v1:voterPlanSaveView")
        self.voter_plan_list_retrieve_url = reverse("apis_v1:voterPlanListRetrieveView")

    def test_retrieve_with_no_voter_device_id(self):
        """Without a cookie, we don't expect valid response"""
        response = self.client.get(self.voter_plan_list_retrieve_url)
        json_data = json.loads(response.content.decode())

        # Without a cookie, we don't expect valid response
        self.assertEqual('status' in json_data, True, "status expected in the json response, and not found")
        self.assertEqual('voter_device_id' in json_data, True,
                         "voter_device_id expected in the voterPlanListRetrieveView json response, and not found")

        self.assertEqual(
            json_data['status'], 'VALID_VOTER_DEVICE_ID_MISSING ',  # Space needed
            "status: {status} (VALID_VOTER_DEVICE_ID_MISSING expected), "
            "voter_device_id: {voter_device_id}".format(
                status=json_data['status'], voter_device_id=json_data['voter_device_id']))

    def test_retrieve_with_voter_device_id(self):
        """Test the various cookie states :return:"""
        # Generate the voter_plan_list_retrieve_url cookie
        response = self.client.get(self.voter_plan_list_retrieve_url)
        json_data = json.loads(response.content.decode())

        # Make sure we got back a voter_device_id we can use
        self.assertEqual('voter_device_id' in json_data, True,
                         "voter_device_id expected in the voterPlanListRetrieveView json response")

        # Now put the voter_device_id in a variable we can use below
        voter_device_id = json_data['voter_device_id'] if 'voter_device_id' in json_data else ''