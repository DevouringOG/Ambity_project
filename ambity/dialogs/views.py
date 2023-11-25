import django.views.generic
import dialogs.models


class DialogListView(django.views.generic.ListView):
    template_name = "dialogs/list.html"
    model = dialogs.models.DialogCard
    context_object_name = "items"

    def get_queryset(self):
        return super().get_queryset()


class DialogDetailView(django.views.generic.DetailView):
    template_name = "dialogs/detail.html"
    model = dialogs.models.DialogCard
    context_object_name = "item"

    def get_queryset(self):
        return super().get_queryset()
