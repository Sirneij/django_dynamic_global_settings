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
        generic_settings.save(update_fields=["vpn_providers"])
        return JsonResponse(
            {
                "success": True,
            }
        )
    context = {"form": form}
    return render(request, "change_settings.html", context)
