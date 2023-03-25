from procedural import funcao_nomeada
from requests import get

funcao_nomeada()

r = get('http://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))