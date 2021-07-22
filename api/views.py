import re

import json

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from jsonschema import ValidationError

from api.models import Path

NOT_FOUND_RESPONSE = {
    'message': 'We could not find a mock for the endpoint requested'
}

PATTERNS = {
    '\\{string\\}': '[A-z]+',
    '\\{integer\\}': '[0-9]+'
}


def endpoint_to_regex(endpoint):
    pattern = re.compile('|'.join(PATTERNS.keys()))
    regex = pattern.sub(lambda m: PATTERNS[re.escape(m.group(0))], endpoint)
    regex += '$'

    return regex


@csrf_exempt
def router(request, endpoint):
    requested_endpoint = '/' + endpoint
    re_endpoint = endpoint_to_regex(endpoint)

    for path in Path.objects.all():
        re_endpoint = endpoint_to_regex(path.endpoint_string)
        match = re.match(re_endpoint, requested_endpoint)

        try:
            path.validate_body(json.loads(request.body))
        except ValidationError as err:
            return JsonResponse(data={'ERROR': err.message}, status=400)

        if match and request.method == path.http_method:
            return JsonResponse(data=path.mockresponse.body,
                                status=path.mockresponse.status)

    return JsonResponse(data=NOT_FOUND_RESPONSE, status=404)
