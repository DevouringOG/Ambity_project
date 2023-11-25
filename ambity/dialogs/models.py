import django.db.models


class Contact(django.db.models.Model):
    full_name = django.db.models.CharField(
        verbose_name="ФИО",
        max_length=93,
    )
    phone = django.db.models.CharField(
        verbose_name="Телефон",
        max_length=15,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Operator(django.db.models.Model):
    full_name = django.db.models.CharField(
        verbose_name="ФИО",
        max_length=93,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'оператор'
        verbose_name_plural = 'операторы'


class Transcription(django.db.models.Model):
    operator_transcription = django.db.models.TextField()
    contact_transcription = django.db.models.TextField()

    def __str__(self):
        return f"транскрипция для {self.conversation}"

    class Meta:
        verbose_name = 'транскрипция'
        verbose_name_plural = 'транскрипции'


class Conversation(django.db.models.Model):
    transcription = django.db.models.OneToOneField(
        Transcription,
        on_delete=django.db.models.CASCADE,
        related_name="conversation",
    )
    contact_audio = django.db.models.FileField(
        upload_to="conversation_audio/",
    )

    def __str__(self):
        return f"разговор {self.id}"

    class Meta:
        verbose_name = 'разговор'
        verbose_name_plural = 'разговоры'


class DialogCard(django.db.models.Model):
    call_date = django.db.models.DateTimeField(
        verbose_name="Дата и время звонка",
    )
    contact = django.db.models.ForeignKey(
        Contact,
        on_delete=django.db.models.CASCADE,
    )
    operator = django.db.models.ForeignKey(
        Operator,
        on_delete=django.db.models.CASCADE,
    )
    conversation = django.db.models.ForeignKey(
        Conversation,
        on_delete=django.db.models.CASCADE,
    )

    def __str__(self):
        return f"карточка контакта {self.id} - {self.call_date}"

    class Meta:
        verbose_name = 'карточка контакта'
        verbose_name_plural = 'карточки контакта'