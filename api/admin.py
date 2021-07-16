from django.contrib import admin

from api.models import Path, MockResponse


class MockResponseInlines(admin.TabularInline):
    model = MockResponse


class PathAdmin(admin.ModelAdmin):
    inlines = [MockResponseInlines]


admin.site.register(Path, PathAdmin)
