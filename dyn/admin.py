from django.contrib import admin
from models import CustomFormField, CustomForm, Category
from forms import *


class CustomFormFieldInline(admin.TabularInline):
    """
    Custom Form Field Inline definition
    """
    model = CustomFormField
    extra = 0


class CustomFormAdmin(admin.ModelAdmin):
    """
    Custom Form Admin, with CustomFormField inlines
    """
    model = CustomForm
    inlines = [CustomFormFieldInline, ]

    def change_view(self, request, object_id, form_url='', extra_context=None):
        # we override the change view to return
        # the dynamically created form.
        extra_context = extra_context or {}
        obj = CustomForm.objects.get(id=object_id)
        extra_context['preview_form'] = obj.form
        return super(CustomFormAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)

admin.site.register(CustomForm, CustomFormAdmin)
admin.site.register(Category)
