from django.http.response import JsonResponse
from django.shortcuts import render

from .forms import GenericSettingsForm
from .models import GenericSettings


def index(request):
    generic_settings = GenericSettings.load()
    context = {"generic_settings": generic_settings}
    return render(request, "index.html", context)


def change_settings(request):
    form = GenericSettingsForm()
    if request.method == "POST":
        vpn_providers = request.POST.get("vpn_providers")
        generic_settings = GenericSettings.load()
        generic_settings.vpn_providers = vpn_providers
        default_vpn_provider = generic_settings.default_vpn_provider
        default_vpn_provider.insert(
            0, default_vpn_provider.pop(default_vpn_provider.index(vpn_providers))
        )
        generic_settings.save(update_fields=["vpn_providers", "default_vpn_provider"])
        return JsonResponse({"success": True})
    context = {"form": form}
    return render(request, "change_settings.html", context)
