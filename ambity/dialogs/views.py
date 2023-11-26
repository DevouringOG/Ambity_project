import django.views.generic
import dialogs.models
import requests
import django.urls
import django.shortcuts
import re

import dialogs.transcription


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


class CreateDialogView(django.views.View):

    def get(self, request, *args, **kwargs):
        response_data = requests.get("http://hackathon.ambity.ru/api/contact").json()

        transcripted_dialog = dialogs.transcription.transcript(response_data["contact_audio"])

        operator_transcription=list(map(lambda x: x.text, filter(lambda x: x.speaker == "B", transcripted_dialog)))
        print(operator_transcription)
        contact_transcription=list(map(lambda x: x.text, filter(lambda x: x.speaker == "A", transcripted_dialog)))
        print(contact_transcription)

        contact_full_name = contact_transcription[1][len("Меня зовут") + 1:].rstrip() # не надёжный хардкод (доработать)

        contact_model = dialogs.models.Contact(
            full_name=contact_full_name,
            phone=response_data["client_phone"],
        )
        operator_model = dialogs.models.Operator(
            full_name=response_data["operator_fio"].split(",")[0],
        )
        transcription_model = dialogs.models.Transcription(
            operator_transcription=operator_transcription,
            contact_transcription=contact_transcription,
        )
        conversation_model = dialogs.models.Conversation(
            transcription=transcription_model,
            contact_audio="http://hackathon.ambity.ru/hackathon/public/audio/zapis418.mp3",
        )
        dialog_model = dialogs.models.DialogCard(
            call_date=response_data["call_date"],
            contact=contact_model,
            operator=operator_model,
            conversation=conversation_model,
        )

        contact_model.save()
        operator_model.save()
        transcription_model.save()
        conversation_model.save()
        dialog_model.save()

        return django.shortcuts.redirect(
            django.urls.reverse_lazy("dialogs:dialog_detail", args=[dialog_model.pk])
        )
