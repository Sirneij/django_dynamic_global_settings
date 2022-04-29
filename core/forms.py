from django import forms

from .models import GenericSettings


class GenericSettingsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GenericSettingsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-select"

    class Meta:
        model = GenericSettings
        fields = ["vpn_providers"]
