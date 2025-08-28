import os 
import sys
import pytest 
from enum import Enum
from src.models.user_model import User 


@pytest.mark.models
class TestUserModel:
    
    def test_create_user(self):
        assert 1 == 1
    
    def test_get_first_name(self, create_default_user):
        first_name = create_default_user.first_name
        assert first_name == "Lucas"

    def test_get_last_name(self, create_default_user):
        last_name = create_default_user.last_name
        assert last_name == "Moura"

    def test_get_email(self, create_default_user):
        email = create_default_user.email
        assert email == "lucas.moura@email.com"

    
    def test_get_password(self, create_default_user):
        password = create_default_user.password 
        assert password == "32322916aA!"
        

    def test_get_full_name(self, create_default_user):
        full_name = create_default_user.full_name
        assert full_name == "Lucas Moura"
        
    def test_update_first_name(self, create_default_user):
        assert create_default_user.first_name == "Lucas"
        create_default_user.first_name = "Pietro"
        assert create_default_user.first_name == "Pietro"
    
    def test_update_last_name(self, create_default_user):
        assert create_default_user.last_name == "Moura"
        create_default_user.last_name = "Jean"
        assert create_default_user.last_name == "Jean"
        
    def test_update_email_name(self, create_default_user):
        assert create_default_user.email == "lucas.moura@email.com"
        create_default_user.email = "teste@teste.com"
        assert create_default_user.email == "teste@teste.com"
        
    def test_update_id_name(self, create_default_user):
        create_default_user.password = "123123"
        assert create_default_user.password == "123123"