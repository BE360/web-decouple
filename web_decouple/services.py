from decouple import AutoConfig, undefined
from urllib.parse import urlencode


class WebConfig(AutoConfig):

    def get_url(self, service, url_name, query_params: dict=None):
        service_code = self.get_service_code(service)

        service_base_url = self(service_code)

        url_code = service_code + '/' + url_name
        url = service_base_url + self(url_code)

        if query_params:
            url += '?' + urlencode(query_params)

        return url

    def get_token(self, service):
        token_code = self.get_service_code(service) + '.token'
        return self(token_code)

    def get_service_code(self, service):
        return 'srv.' + service

    def get_data(self, service, key, cast=undefined):
        service_code = self.get_service_code(service)

        data_key = service_code + "@" + key

        return self(data_key, cast=cast)


config = WebConfig()
