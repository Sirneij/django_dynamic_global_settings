from django.db import models


class SettingsBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SettingsBaseModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class GenericSettings(SettingsBaseModel):
    ACCESS = "AC"
    CYBERGHOST = "CY"
    EXPRESSVPN = "EX"

    VPN_PROVIDERS = [
        (ACCESS, "Access"),
        (CYBERGHOST, "CyberGhost"),
        (EXPRESSVPN, "ExpressVPN"),
    ]

    vpn_providers = models.CharField(
        max_length=2, choices=VPN_PROVIDERS, default=ACCESS
    )
