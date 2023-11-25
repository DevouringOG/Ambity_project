import django.contrib.admin
import dialogs.models


django.contrib.admin.register(dialogs.models.Contact)
django.contrib.admin.register(dialogs.models.Operator)
django.contrib.admin.register(dialogs.models.DialogCard)
