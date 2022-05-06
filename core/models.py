from typing import Any

from django.contrib.postgres.fields import ArrayField
from django.db import models


def get_default_vpn_provider() -> list[str]:
    """Return a list of providers."""
    return [gvp[0] for gvp in GenericSettings.VPN_PROVIDERS]


def get_from_email() -> list[str]:
    """Return a list of email addresses."""
    return [gea[0] for gea in GenericSettings.FROM_EMAIL_ADDRESSES]


class GenericSettings(models.Model):
    VPN_PROVIDER_ACCESS = 'Access'
    VPN_PROVIDER_CYBERGHOST = 'CyberGhost'
    VPN_PROVIDER_EXPRESSVPN = 'ExpressVPN'

    VPN_PROVIDERS = [
        (VPN_PROVIDER_ACCESS, 'Access'),
        (VPN_PROVIDER_CYBERGHOST, 'CyberGhost'),
        (VPN_PROVIDER_EXPRESSVPN, 'ExpressVPN'),
    ]

    ADMIN_FROM_EMAIL = 'admin@dynamic_settings.com'
    USER_FROM_EMAIL = 'user@dynamic_settings.com'
    AUDIT_FROM_EMAIL = 'audit@dynamic_settings.com'
    EDITOR_FROM_EMAIL = 'editor@dynamic_settings.com'
    ACCOUNT_FROM_EMAIL = 'account@dynamic_settings.com'

    FROM_EMAIL_ADDRESSES = [
        (ADMIN_FROM_EMAIL, 'From email address for admins'),
        (USER_FROM_EMAIL, 'From email address for users'),
        (AUDIT_FROM_EMAIL, 'From email address for auditors'),
        (EDITOR_FROM_EMAIL, 'From email address for editors'),
        (ACCOUNT_FROM_EMAIL, 'From email address for accounts'),
    ]

    default_vpn_provider = ArrayField(
        models.CharField(max_length=20), default=get_default_vpn_provider
    )
    default_from_email = ArrayField(
        models.CharField(max_length=50), default=get_from_email
    )

    def save(self, *args, **kwargs):  # type: ignore
        """Save object to the database. All other entries, if any, are removed."""
        self.__class__.objects.exclude(id=self.id).delete()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """String representation of the model."""
        return f'GenericSettings for {self.id}'

    @classmethod
    def load(cls) -> Any:
        """Load the model instance."""
        obj, _ = cls.objects.get_or_create(id=1)
        return obj
