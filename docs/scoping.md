# Scoping Notifications

Sometimes you have a site that has groups or teams. Perhaps you are using
[pinax-teams](https://github.com/pinax/pinax-teams/). If this is the case you
likely want users who might be members of multiple teams to be able to set
their notification preferences on a per team or group basis.

You will need to to simply override `NoticeSettingsView` to provide your own
scoping object.

## Override NoticeSettingsView

I think it's best if we just demonstrate via code:

    # views.py
    from pinax.notifications.views import NoticeSettingsView
    
    
    class TeamNoticeSettingsView(NoticeSettingsView):
        
        @property
        def scoping(self):
            return self.request.team


Then override the url:

    # urls.py
    from django.conf.urls import patterns, url
    
    from .views import TeamNoticeSettingsView
    
    
    urlpatterns = patterns(
        "",
        ...
        url(r"^notifications/settings/$", TeamNoticeSettingsView.as_view(), name="notification_notice_settings"),
    )
