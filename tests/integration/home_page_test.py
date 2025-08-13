import pytest 
from enum import Enum
from playwright.sync_api import sync_playwright

class RequestMethod(Enum):
    get = 'GET'
    post = 'POST'       
    put = 'PUT'
    delete = 'DELETE'

def verify_request_method(route, request, method: RequestMethod):
    assert request.method == method.value
    route.continue_()

def test_home_page_get(client):
    response = client.get('/')
    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert response.status_code == 200 

def test_home_page_post(client):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.route("**/",  lambda route, request: verify_request_method(route, request, RequestMethod.post))

        response = client.post('http://localhost:5000/')


        assert response.headers['Content-Type'] == 'text/html; charset=utf-8'
        assert response.status_code == 405 
        page.get_by_role("header")
        print(page.content())

def test_home_page_put(client):
    response = client.put('/')
    assert response.status_code == 405 

def test_home_page_delete(client):
    response = client.delete('/')
    assert response.status_code == 405 
