import requests
from lib.requestHandle import RequestHandler
from kw_handle.kw_login.kw_login import kw_login_getToken

def kw_goods_list(token):
    url = "http://127.0.0.1:8000/goods/"

    request_handler=RequestHandler()

    res=RequestHandler.request_get(url)

