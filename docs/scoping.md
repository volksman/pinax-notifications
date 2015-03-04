# Scoping Notifications

Sometimes you have a site that has groups or teams. Perhaps you are using
[pinax-teams](https://github.com/pinax/pinax-teams/). If this is the case you
likely want users who might be members of multiple teams to be able to set
their notification preferences on a per team or group basis.

You will need to:

* Create a custom model for settings
* Override NoticeSettingsView


## Custom Model for Settings

First thing you need to do is subclass `pinax.notifications.models.NoticeSettingBase`
and add whatever attributes needed to provide the scoping. For example, to
scope by a `pinax-teams` team:

    # models.py
    from pinax.notifications.models import NoticeSettingsBase
    
    class TeamNoticeSetting(NoticeSettingsBase):
        team = models.ForeignKey(Team, null=True)
        
        @classmethod
        def get_lookup_kwargs(cls, user, notice_type, medium, scoping):
            return {
                "user": user,
                "notice_type": notice_type,
                "medium": medium,
                "team": scoping
            }

Then add the setting to use this custom model:

    # settings.py
    PINAX_NOTIFICATIONS_SETTING_MODEL = "mysite.TeamNoticeSetting"


## Override NoticeSettingsView

Next, let's override the method on `pinax.notifications.views.NoticeSettingsView`
that handles the lookup of the `setting` for each notice type and channel.

    # views.py
    from pinax.notifications.views import NoticeSettingsView
    
    class TeamNoticeSettingsView(NoticeSettingsView):
        
        def setting_for_user(self, notice_type, medium_id):
            return self.SettingModel.for_user(
                self.request.user,
                notice_type,
                medium_id,
                scoping=self.request.team
            )

Then override the url:

    # urls.py
    from django.conf.urls import patterns, url
    
    from .views import TeamNoticeSettingsView
    
    
    urlpatterns = patterns(
        "",
        ...
        url(r"^notifications/settings/$", TeamNoticeSettingsView.as_view(), name="notification_notice_settings"),
    )
