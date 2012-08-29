eloqua-python-request
==================

Eloqua Python Request

## Usage

### Import
	import sys
	sys.path.append('./lib')
	from eloqua_request import EloquaRequest

### GET
	request = EloquaRequest('site', 'user', 'password')
	response = request.get(url, None)

### POST
	request = EloquaRequest('site', 'user', 'password')
	response = request.post(url, data)


### PUT
	request = EloquaRequest('site', 'user', 'password')
	response = request.put(url, data)


### DELETE
	request = EloquaRequest('site', 'user', 'password')
	response = request.delete(url, None)
