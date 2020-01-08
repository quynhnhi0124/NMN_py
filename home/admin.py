from django.contrib import admin

from .models import Exam, LOP10, THPTQG

class Lop10Inline(admin.StackedInline):
    model = LOP10

class ThptqgInline(admin.StackedInline):
    model = THPTQG

class ExamAdmin(admin.ModelAdmin):

    inlines = [
        Lop10Inline, ThptqgInline,
    ]
    model = Exam
    


admin.site.register(Exam, ExamAdmin)
# admin.site.register(Question)
# admin.site.register(Exam)
