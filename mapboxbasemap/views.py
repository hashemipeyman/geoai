from django.shortcuts import render


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiaGFzaGVtaXBleW1hbiIsImEiOiJja2tvMW8xMmYxenJqMnZ0ZHEwcm9uZW9uIn0.pUtfPgFF3IkJ2L8-CIuMhw'
    return render(request, 'default.html',
                  { 'mapbox_access_token': mapbox_access_token })
