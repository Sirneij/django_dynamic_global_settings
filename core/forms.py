from django import forms

from .models import GenericSettings


class GenericSettingsForm(forms.ModelForm):
    vpn_providers = forms.ChoiceField(
        choices=GenericSettings.VPN_PROVIDERS,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = GenericSettings
        fields = [
            "vpn_providers",
        ]
