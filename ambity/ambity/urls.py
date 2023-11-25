import django.contrib.admin
import django.urls

import dialogs.urls


urlpatterns = [
    django.urls.path(
        "admin/",
        django.contrib.admin.site.urls,
    ),
    django.urls.path(
        "dialogs/",
        django.urls.include(dialogs.urls)
    )
]
