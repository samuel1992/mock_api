from jsoneditor.forms import JSONEditor

from django.contrib import admin

from django.db import models

from api.models import Path, MockResponse


class MockResponseInlines(admin.TabularInline):
    model = MockResponse
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditor},
    }


class PathAdmin(admin.ModelAdmin):
    inlines = [MockResponseInlines]

    formfield_overrides = {
        models.JSONField: {'widget': JSONEditor},
    }


admin.site.register(Path, PathAdmin)
