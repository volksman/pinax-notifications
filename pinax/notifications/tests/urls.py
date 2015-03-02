try:
    from django.conf.urls import patterns, include, url
except ImportError:
    from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns(
    "",
    url(r"^account/", include("account.urls")),
    url(r"^notifications/", include("pinax.notifications.urls")),
)
