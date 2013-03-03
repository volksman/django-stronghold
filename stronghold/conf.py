from django.conf import settings
from django.core.urlresolvers import reverse


if settings.DEBUG:
    # In Debug mode we serve the media urls as public by default
    # We should also serve the login/logout pages as public if we can easily
    # determin their URLs

    login = False
    logout = False

    if settings.LOGIN_URL and settings.LOGOUT_URL:
        login = settings.LOGIN_URL
        logout = settings.LOGOUT_URL
    else:
        if 'django.contrib.auth' in settings.INSTALLED_APPS:
            login = reverse('login')
            logout = reverse('logout')

    STRONGHOLD_PUBLIC_URLS = [
        r'^%s.+$' % settings.STATIC_URL,
        r'^%s.+$' % settings.MEDIA_URL,
    ]

    if login:
        STRONGHOLD_PUBLIC_URLS.append(r'^%s$' % login)

    if logout:
        STRONGHOLD_PUBLIC_URLS.append(r'^%s$' % logout)

else:
    # make no such assumptions in production
    STRONGHOLD_PUBLIC_URLS = ()


STRONGHOLD_PUBLIC_URLS = getattr(settings,
                                 'STRONGHOLD_PUBLIC_URLS',
                                 STRONGHOLD_PUBLIC_URLS)
