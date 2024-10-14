from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()
NULLABLE = {"null": True, "blank": True}


class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ф.И.О. клиента")
    email = models.EmailField(max_length=50, verbose_name="почта", unique=True)
    comment = models.TextField(verbose_name="комментарии", **NULLABLE)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Message(models.Model):
    subject = models.CharField(verbose_name="Тема", max_length=255)
    body = models.TextField(verbose_name="Сообщение", **NULLABLE)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages", **NULLABLE
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Mailing(models.Model):
    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = "Создана"
    STARTED = "Запущена"
    COMPLETED = "Заверщена"

    STATUS_CHOICES = [
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
        (COMPLETED, "Заверщена"),
    ]
    start_time = models.DateTimeField(verbose_name="время начала рассылки")
    end_time = models.DateTimeField(verbose_name="время окончания рассылки")
    periodicity = models.CharField(
        max_length=50, choices=PERIODICITY_CHOICES, verbose_name="периодичность"
    )
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=CREATED, verbose_name="статус"
    )
    topic_letter = models.CharField(max_length=100, verbose_name="тема письма")
    body_letter = models.TextField(verbose_name="тело письма")

    customers = models.ManyToManyField(Customer, verbose_name="клиенты рассылки")

    def __str__(self):
        return f"Mailing {self.topic_letter} - {self.status}"

    def start_mailing(self):
        self.actual_start_time = timezone.now()
        self.status = "started"
        self.save()

    def complete_mailing(self):
        self.actual_end_time = timezone.now()
        self.status = "completed"
        self.save()

    class Meta:
        verbose_name = "настройка рассылки"
        verbose_name_plural = "настройки рассылок"


class MailingAttempt(models.Model):
    STATUS_CHOICES = [("success", "Успешно"), ("failed", "Не успешно")]

    mailing = models.ForeignKey(
        Mailing, related_name="attempts", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    server_response = models.TextField(**NULLABLE)

    def __str__(self):
        return f"Attempt {self.id} - {self.status}"
