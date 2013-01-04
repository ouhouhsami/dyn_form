from django import forms


class DynamicForm(forms.Form):
    """ Dynamic Form """
    def __init__(self, config, *args, **kwargs):
        super(DynamicForm, self).__init__(*args, **kwargs)
        # here we add fields
        for key in config:  # list comprehension better
            self.fields[key] = config[key]
