from django.contrib import admin

from .models import Exam, Lop10, Thptqg

class Lop10Inline(admin.StackedInline):
    model = Lop10

class ThptqgInline(admin.StackedInline):
    model = Thptqg

class ExamAdmin(admin.ModelAdmin):

    inlines = [
        Lop10Inline, ThptqgInline,
    ]
    model = Exam
    


admin.site.register(Exam, ExamAdmin)
# admin.site.register(Question)
# admin.site.register(Exam)
