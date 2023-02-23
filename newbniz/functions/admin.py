from django.contrib import admin

from .models import Function, FunctionParameter

# admin.site.register([Function, FunctionParameter])

class FunctionParametersInline(admin.StackedInline):
    model = FunctionParameter
    can_delete = False
    verbose_name_plural = 'functionparameters'

@admin.register(Function)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (FunctionParametersInline,)
