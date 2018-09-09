import sys
from urllib.parse import urlencode

import os
from decouple import AutoConfig, undefined


class WebConfig(AutoConfig):

    def get_url(self, service, url_name=None, base_url=None, query_params: dict=None, url_kwargs: dict=None):
        service_code = self.get_service_code(service)

        if base_url is None:
            service_base_url = self(service_code)
        else:
            service_base_url = base_url

        if url_name:
            url_code = service_code + '/' + url_name
            url = service_base_url + self(url_code)
        else:
            url = service_base_url

        if url_kwargs:
            url = url.format(**url_kwargs)

        if query_params:
            url += '?' + urlencode(query_params)

        return url

    def get_token(self, service):
        token_code = self.get_service_code(service) + '.token'
        return self(token_code)

    def get_service_code(self, service):
        return 'srv.' + service

    def get_data(self, service, key, cast=undefined, default=undefined):
        service_code = self.get_service_code(service)

        data_key = service_code + "@" + key

        return self(data_key, cast=cast, default=default)

    def _caller_path(self):
        # SUPERMAGIC! Get the caller's module path.
        frame = sys._getframe()
        path = os.path.dirname(frame.f_back.f_back.f_back.f_code.co_filename)
        return path

config = WebConfig()
