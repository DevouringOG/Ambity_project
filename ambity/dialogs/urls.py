import django.urls

import dialogs.views


app_name = "dialogs"

urlpatterns = [
    django.urls.path(
        "",
        dialogs.views.DialogListView.as_view(),
    ),
    django.urls.path(
        "<pk>/",
        dialogs.views.DialogDetailView.as_view(),
    )
]
