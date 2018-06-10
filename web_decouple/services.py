from decouple import config
from urllib.parse import urlencode


def get_url(service, url_name, query_params: dict=None):
    service_code = get_service_code(service)

    service_base_url = config(service_code)

    url_code = service_code + '/' + url_name
    url = service_base_url + config(url_code)

    if query_params:
        url += '?' + urlencode(query_params)

    return url


def get_token(service):
    token_code = get_service_code(service) + '.token'
    return config(token_code)


def get_service_code(service):
    return 'srv.' + service


def get_data(service, key, cast=str):
    service_code = get_service_code(service)

    data_key = service_code + "#" + key

    return config(data_key, cast=cast)
