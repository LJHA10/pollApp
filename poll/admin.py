from django.contrib import admin

from .models import Choice, Question
# Register your models here.

# admin.site.register(Questions)
# admin.site.register(Choise)

class ChoiseInline(admin.TabularInline):
    model =Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiseInline]