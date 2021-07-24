import json
import re

from django.db import models

from openapi_schema_validator import validate

REQUESTS_WITH_BODY = ['POST', 'PUT', 'PATCH']
PATTERNS = {
    '\\{string\\}': '[A-z]+',
    '\\{integer\\}': '[0-9]+'
}


class Path(models.Model):
    HTTP_METHODS = [
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('GET', 'GET'),
        ('PATCH', 'PATCH')
    ]

    endpoint_string = models.CharField(max_length=300)
    http_method = models.CharField(max_length=5, choices=HTTP_METHODS)
    body_schema = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return self.endpoint_string

    def validate_body(self, body):
        if self.http_method in REQUESTS_WITH_BODY:
            validate(json.loads(body), self.body_schema)

    def to_regex(self):
        pattern = re.compile('|'.join(PATTERNS.keys()))
        regex = pattern.sub(lambda m: PATTERNS[re.escape(m.group(0))],
                            self.endpoint_string)
        regex += '$'

        return regex

    def matches(self, endpoint):
        return bool(re.match(self.to_regex(), endpoint))


class MockResponse(models.Model):
    body = models.JSONField()
    status = models.IntegerField()

    path = models.OneToOneField(Path,
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return f'{self.status} -- {self.path.http_method} for {self.path}'
