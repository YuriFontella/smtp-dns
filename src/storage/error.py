import falcon

class StorageError(Exception):
	@staticmethod
	async def handle(req, resp, e, params):
		raise falcon.HTTPBadRequest(description=str(e))