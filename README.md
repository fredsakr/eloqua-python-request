eloqua-python-request
==================

Eloqua Python Request

## Usage

### GET
	import sys
	sys.path.append('./lib')
	from eloqua_request import EloquaRequest
	
	request = EloquaRequest('RDSteveWoods', 'Fred.Sakr', 'Zxcv123%678')
	response = request.get('/assets/emails?search=Demand*&page=1&count=50&depth=minimal', None)
