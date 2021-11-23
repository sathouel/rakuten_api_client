import json

from rakuten_api_client.utils import urljoin

class ResourcePool:
    def __init__(self, endpoint, session, params={}):
        """Initialize the ResourcePool to the given endpoint. Eg: products"""
        self._endpoint = endpoint
        self._session = session
        self._params = params

    def get_url(self):
        return self._endpoint

class ListableResource(ResourcePool):
    def fetch_list(self, params={}):
        joined_params = self._params.update(params)
        res = self._session.get(self._endpoint, params=joined_params)
        return res

# Pools

class CategoryMapResource(ListableResource):
    pass

class ProductTypesResource(ListableResource):
    pass

class ProductTypesTemplateResource(ListableResource):
    pass

class GenericImportFileResource(ListableResource):
    pass

class GenericImportReportResource(ListableResource):
    pass

class AcceptSaleResource(ListableResource):
    pass

class GetNewSalesResource(ListableResource):
    pass

# class CreatableResource:
#     def create_item(self, item, files=None):
#         if files:
#             self._session.headers.pop('Content-Type')
#             self._session.headers.pop('Accept')
#             print(self._session.headers)
#             res = self._session.post(self._endpoint, files=files, data=item)
#         else:
#             res = self._session.post(self._endpoint, data=json.dumps(item))
#         return res

# class GettableResource:
#     def fetch_item(self, code):
#         url = urljoin(self._endpoint, code)
#         res = self._session.get(url)
#         return res        

# class SearchableResource:
#     def search(self, query):
#         params = {
#             'query': query
#         }
#         res = self._session.get(self._endpoint, params=params)
#         return res

# class UpdatableResource:
#     def update_create_item(self, item, code=None):
#         if code is None:
#             code = item.get('id')
#         url = urljoin(self._endpoint, code) if code else self._endpoint
#         res = self._session.put(url, data=json.dumps(item))
#         return res

# class DeletableResource:
#     def delete_item(self, code):
#         url = urljoin(self._endpoint, code)
#         res = self._session.delete(url)
#         return res
