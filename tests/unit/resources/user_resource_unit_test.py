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
class TestUserModel:
    
    
    @pytest.mark.skip
    def test_get_user_list(self, client):
        response = client.get("/api/user/")
        response_json = user_serializer(response.json)
        
        assert response_json == ""