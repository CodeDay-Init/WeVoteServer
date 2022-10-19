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
        response = self.client.get(self.voter_plan_list_retrieve_url)
        json_data = json.loads(response.content.decode())

    def test_retrieve_with_voter_device_id(self):
        response = self.client.get(self.voter_plan_list_retrieve_url)
        json_data = json.loads(response.content.decode())
        voter_device_id = json_data['voter_device_id'] if 'voter_device_id' in json_data else ''
