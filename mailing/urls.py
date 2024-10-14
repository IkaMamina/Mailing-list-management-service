from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (
    MailingListView,
    MailingCreateView,
    MailingUpdateView,
    MailingDeleteView,
    HomePageView,
    MailingDetailView,
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
    MailingAttemptListView,
    MailingAttemptDetailView,
    MailingAttemptCreateView,
    MailingAttemptUpdateView,
    MailingAttemptDeleteView,
    ContactView,
    RunMailingCommandView,
    RunMailingHardCommandView,
)

app_name = MailingConfig.name

urlpatterns = [
    path("", cache_page(3)(HomePageView.as_view()), name="index"),
    path("customers", CustomerListView.as_view(), name="customer_list"),
    path("customers/<int:pk>/", CustomerDetailView.as_view(), name="customer_detail"),
    path("customers/create/", CustomerCreateView.as_view(), name="customer_create"),
    path(
        "customers/<int:pk>/update/",
        CustomerUpdateView.as_view(),
        name="customer_update",
    ),
    path(
        "customers/<int:pk>/delete/",
        CustomerDeleteView.as_view(),
        name="customer_delete",
    ),
    path("messages", MessageListView.as_view(), name="message_list"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("messages/create/", MessageCreateView.as_view(), name="message_create"),
    path(
        "messages/<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"
    ),
    path(
        "messages/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"
    ),
    path("mailings", MailingListView.as_view(), name="mailing_list"),
    path("mailings/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailings/create/", MailingCreateView.as_view(), name="mailing_create"),
    path(
        "mailings/<int:pk>/update", MailingUpdateView.as_view(), name="mailing_update"
    ),
    path(
        "mailings/<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing_delete"
    ),
    path(
        "mailings/<int:mailing_id>/attempts/",
        MailingAttemptListView.as_view(),
        name="mailing_attempt_list",
    ),
    path(
        "mailings/<int:mailing_id>/attempts/<int:pk>/",
        MailingAttemptDetailView.as_view(),
        name="mailing_attempt_detail",
    ),
    path(
        "mailings/<int:mailing_id>/attempts/create/",
        MailingAttemptCreateView.as_view(),
        name="mailing_attempt_create",
    ),
    path(
        "mailings/<int:mailing_id>/attempts/<int:pk>/update/",
        MailingAttemptUpdateView.as_view(),
        name="mailing_attempt_update",
    ),
    path(
        "mailings/<int:mailing_id>/attempts/<int:pk>/delete/",
        MailingAttemptDeleteView.as_view(),
        name="mailing_attempt_delete",
    ),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path(
        "mailings/<int:mailing_id>/run/",
        RunMailingCommandView.as_view(),
        name="run_mailing_command",
    ),
    path(
        "mailings/<int:mailing_id>/run/hard/",
        RunMailingHardCommandView.as_view(),
        name="run_mailing_hard_command",
    ),
]
