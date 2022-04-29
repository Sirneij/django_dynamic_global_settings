from django.contrib.postgres.fields import ArrayField
from django.db import models


def get_default_vpn_provider() -> list:
    return ["Access", "CyberGhost", "ExpressVPN"]


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
    ACCESS = "Access"
    CYBERGHOST = "CyberGhost"
    EXPRESSVPN = "ExpressVPN"

    VPN_PROVIDERS = [
        (ACCESS, "Access"),
        (CYBERGHOST, "CyberGhost"),
        (EXPRESSVPN, "ExpressVPN"),
    ]

    vpn_providers = models.CharField(
        max_length=20, choices=VPN_PROVIDERS, default=ACCESS
    )
    default_vpn_provider = ArrayField(
        models.CharField(max_length=20), default=get_default_vpn_provider
    )
