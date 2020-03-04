from django.contrib import admin

from .models import Question, TestCase, ExpectedOutput


admin.site.register(Question)
admin.site.register(TestCase)
admin.site.register(ExpectedOutput)
