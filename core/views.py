from django.http.response import JsonResponse
from django.shortcuts import render

from .models import GenericSettings


def index(request):
    """App's entry point."""
    generic_settings = GenericSettings.load()
    context = {
        'generic_settings': generic_settings,
        'vpn_providers': GenericSettings.VPN_PROVIDERS,
        'email_providers': GenericSettings.FROM_EMAIL_ADDRESSES,
    }
    return render(request, 'index.html', context)


def change_settings(request):
    """Route that handles post requests."""
    if request.method == 'POST':
        provider_type = request.POST.get('provider_type')
        if provider_type:
            if provider_type.lower() == 'vpn':
                generic_settings = GenericSettings.load()
                vpn_provider = request.POST.get('default_vpn_provider')
                default_vpn_provider = generic_settings.default_vpn_provider
                # put the selected otp provider at the begining.
                default_vpn_provider.insert(
                    0,
                    default_vpn_provider.pop(default_vpn_provider.index(vpn_provider)),
                )
                generic_settings.save(update_fields=['default_vpn_provider'])

                response = JsonResponse({'success': True})

            elif provider_type.lower() == 'email':
                generic_settings = GenericSettings.load()
                selected_email_provider = request.POST.get('default_from_email')
                default_email_provider = generic_settings.default_from_email
                # put the selected sms provider at the begining.
                default_email_provider.insert(
                    0,
                    default_email_provider.pop(
                        default_email_provider.index(selected_email_provider)
                    ),
                )
                generic_settings.save(update_fields=['default_from_email'])

                response = JsonResponse({'success': True})

            return response

        return JsonResponse({'success': False})
    return JsonResponse({'success': False})
