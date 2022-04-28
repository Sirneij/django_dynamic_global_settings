from django.core.cache import cache
from django.db import models


class SettingsBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SettingsBaseModel, self).save(*args, **kwargs)
        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)


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
