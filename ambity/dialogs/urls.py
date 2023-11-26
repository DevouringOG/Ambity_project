import django.urls

import dialogs.views


app_name = "dialogs"

urlpatterns = [
    django.urls.path(
        "create_dialog/",
        dialogs.views.CreateDialogView.as_view(),
        name="create_dialog",
    ),
    django.urls.path(
        "",
        dialogs.views.DialogListView.as_view(),
        name="dialog_list",
    ),
    django.urls.path(
        "<pk>/",
        dialogs.views.DialogDetailView.as_view(),
        name="dialog_detail",
    ),
]
