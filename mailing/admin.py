from django.contrib import admin
from mailing.models import Customer, Mailing


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "comment",
    )
    list_filter = (
        "name",
        "email",
    )


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "topic_letter",
        "periodicity",
        "start_time",
        "end_time",
        "status",
    )
    list_filter = (
        "topic_letter",
        "status",
    )
