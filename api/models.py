from django.db import models


class Path(models.Model):
    HTTP_METHODS = [
        ('post', 'POST'),
        ('post', 'PUT'),
        ('post', 'GET'),
        ('post', 'PATCH')
    ]

    endpoint_string = models.CharField(max_length=300)
    http_method = models.CharField(max_length=5, choices=HTTP_METHODS)

    def __str__(self):
        return self.endpoint_string


class MockResponse(models.Model):
    body = models.JSONField()
    status = models.IntegerField()

    path = models.OneToOneField(Path,
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return f'{self.status} -- {self.path.http_method} for {self.path}'
