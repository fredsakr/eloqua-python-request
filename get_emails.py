import sys
sys.path.append('./lib')
from eloqua_request import EloquaRequest

request = EloquaRequest('site', 'user', 'password')
response = request.get('/assets/emails?search=Demand*&page=1&count=50&depth=minimal', None)
