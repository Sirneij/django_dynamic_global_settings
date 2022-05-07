import json
from django.http import HttpRequest

from django.http.response import JsonResponse
from django.shortcuts import render

from .models import GenericSettings


def index(request: HttpRequest):
    """App's entry point."""
    generic_settings = GenericSettings.load()
    context = {
        'generic_settings': generic_settings,
    }
    return render(request, 'index.html', context)


def change_settings(request: HttpRequest) -> JsonResponse:
    """Route that handles post requests."""
    if request.method == 'POST':
        provider_type = request.POST.get('provider_type')
        if provider_type:
            if provider_type.lower() == 'vpn':
                generic_settings = GenericSettings.load()
                reordered_vpn_provider = json.loads(
                    request.POST.get('default_vpn_provider')
                )

                generic_settings.default_vpn_provider = reordered_vpn_provider
                generic_settings.save(update_fields=['default_vpn_provider'])

                response = JsonResponse({'success': True})

            elif provider_type.lower() == 'email':
                generic_settings = GenericSettings.load()
                reordered_email_provider = json.loads(
                    request.POST.get('default_from_email')
                )

                generic_settings.default_from_email = reordered_email_provider
                generic_settings.save(update_fields=['default_from_email'])
                response = JsonResponse({'success': True})

            return response

        return JsonResponse({'success': False})
    return JsonResponse({'success': False})
