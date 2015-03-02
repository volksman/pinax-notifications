# pinax-notifications

Many sites need to notify users when certain events have occurred and to allow
configurable options as to how those notifications are to be received.

The project aims to provide a Django app for this sort of functionality. This
includes:

* Submission of notification messages by other apps
* Notification messages on signing in
* Notification messages via email (configurable by user)
* Ability to supply your own backends notification channels


!!! note "Originally django-notification"
    This app was originally named `django-notification` but was renamed to
    bring a common package name like `notification` under the `pinax` namespace
    to avoid conflicts with other like named packages.
    
    In addition, we wanted to take the opportunity to rename it to the plural
    form, `notifications` to be in line with the convention we've adopted
    across the ecosystem.

!!! note "Pinax Ecosystem"
    This app was developed as part of the Pinax ecosystem but is just a Django app
    and can be used independently of other Pinax apps.
    
    To learn more about Pinax, see <http://pinaxproject.com/>


## Quickstart

Install the development version:

    pip install pinax-notifications

Add `pinax-notifications` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        "pinax.notifications",
        # ...
    )

Add entry to your `urls.py`:

    url(r"^notifications/", include("pinax.notifications.urls"))
