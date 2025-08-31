import os 
import sys
import pytest 
from enum import Enum
import requests
from src.models.user_model import User
from src.resources.user_resource import UserList, User
from src.utils.api import user_serializer
import json

@pytest.mark.resources
class TestUserResource:
    def test_get_user_list_content_type(self, client):
        response = client.get("/api/user/")
        assert response.headers["Content-Type"] == "application/json"


    def test_get_user_list_status_code(self, client):
        response = client.get("/api/user/")
        assert response.status_code == 200
            
            
    # TODO: Corrijir comportamento do teste para serializar response
    @pytest.mark.skip
    def test_get_user_list_response(self, client):
        response = client.get("/api/user")
        json_response = user_serializer(response.__dict__)
        assert isinstance(json_response, json)