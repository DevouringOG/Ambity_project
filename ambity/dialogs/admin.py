import django.contrib.admin
import dialogs.models


django.contrib.admin.site.register(dialogs.models.Contact)
django.contrib.admin.site.register(dialogs.models.Operator)
django.contrib.admin.site.register(dialogs.models.Conversation)
django.contrib.admin.site.register(dialogs.models.Transcription)
django.contrib.admin.site.register(dialogs.models.DialogCard)
