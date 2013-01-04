from django.db import models
from forms import DynamicForm
from django import forms  # ulgy ugly, see below


class Category(models.Model):
    """
    Category form model, used to organize the different custom forms
    """
    name = models.CharField(max_length=30)
    description = models.TextField()


class CustomForm(models.Model):
    """
    Custom Form model, used to create our dynamic forms
    """
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title

    def _get_form(self):
        # as we work at row level, it's not a bad practise
        # to add model property
        dict = {}
        for cff in self.customformfield_set.all():
            # ugly: a mapping dict is in fact needed
            # and we must use get_field_value !
            dict[cff.label] = eval(cff.field)
        return DynamicForm(dict)
    form = property(_get_form)


class CustomFormField(models.Model):
    """
    Custom Form Field model, used to specify a field of a custom form
    """
    FIELD_CHOICES = (
        ('forms.CharField(max_length=100)', 'forms.CharField(max_length=100)'),
        ('forms.EmailField()', 'forms.EmailField()'),
        ('forms.BooleanField()', 'forms.BooleanField()'),
        # ugly too, see above with mapping idea
    )
    custom_form = models.ForeignKey(CustomForm)
    label = models.CharField(max_length=30)
    field = models.CharField(max_length=50, choices=FIELD_CHOICES)
    required = models.BooleanField()  # not used so far
    help_text = models.CharField(max_length=30, null=True, blank=True)  # not used so far
