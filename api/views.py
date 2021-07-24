from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from jsonschema import ValidationError

from api.models import Path

NOT_FOUND_RESPONSE = {
    'message': 'We could not find a mock for the endpoint requested'
}


@csrf_exempt
def router(request, endpoint):
    requested_endpoint = '/' + endpoint

    for path in Path.objects.all():
        try:
            path.validate_body(request.body)
        except ValidationError as err:
            return JsonResponse(data={'ERROR': err.message}, status=400)

        if (path.matches(requested_endpoint) and
                request.method == path.http_method):
            return JsonResponse(data=path.mockresponse.body,
                                status=path.mockresponse.status)

    return JsonResponse(data=NOT_FOUND_RESPONSE, status=404)
