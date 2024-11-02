"""fighthealthinsurance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import include, path
from django.views.decorators.cache import cache_control, cache_page

from fighthealthinsurance import views
from fighthealthinsurance.followup_emails import (
    FollowUpEmailSenderView,
    ScheduleFollowUps,
)
from fighthealthinsurance.rest_urls import rest_urls

urlpatterns = [
    # Internal-ish-views
    path("ziggy/rest/", include(rest_urls)),
    path("timbit/admin/", admin.site.urls),
    path("timbit/help/followup_sched", ScheduleFollowUps.as_view()),
    path(
        "timbit/help/followup_sender_test",
        staff_member_required(FollowUpEmailSenderView.as_view()),
    ),
    path("error", views.ErrorView.as_view()),
    # These are links we e-mail people so might have some extra junk.
    # So if there's an extra / or . at the end we ignore it.
    path(
        "v0/followup/<uuid:uuid>/<slug:hashed_email>/<slug:follow_up_semi_sekret>",
        views.FollowUpView.as_view(),
        name="followup",
    ),
    path(
        "v0/followup/<uuid:uuid>/<slug:hashed_email>/<slug:follow_up_semi_sekret>.",
        views.FollowUpView.as_view(),
        name="followup-with-a-period",
    ),
    path(
        "v0/followup/<uuid:uuid>/<slug:hashed_email>/<slug:followup_semi_sekret>/",
        views.FollowUpView.as_view(),
        name="followup-with-trailing-slash",
    ),
    # Fax follow up
    # So if there's an extra / or . at the end we ignore it.
    path(
        "v0/faxfollowup/<uuid:uuid>/<slug:hashed_email>",
        views.FaxFollowUpView.as_view(),
        name="fax-followup",
    ),
    path(
        "v0/faxfollowup/<uuid:uuid>/<slug:hashed_email>.",
        views.FaxFollowUpView.as_view(),
        name="fax-followup-with-a-period",
    ),
    path(
        "v0/faxfollowup/<uuid:uuid>/<slug:hashed_email>/",
        views.FaxFollowUpView.as_view(),
        name="fax-followup-with-trailing-slash",
    ),
    # Back to normal stuff
    path(
        "v0/sendfax/<uuid:uuid>/<slug:hashed_email>/",
        views.SendFaxView.as_view(),
        name="sendfaxview",
    ),
    path(
        "v0/stagefax",
        views.StageFaxView.as_view(),
        name="stagefaxview",
    ),
    path("scan", views.ProcessView.as_view(), name="scan"),
    path("server_side_ocr", views.OCRView.as_view(), name="server_side_ocr"),
    path(
        "",
        cache_control(public=True)(cache_page(60 * 60 * 2)(views.IndexView.as_view())),
        name="root",
    ),
    path(
        "about-us",
        cache_control(public=True)(cache_page(60 * 60 * 2)(views.AboutView.as_view())),
        name="about",
    ),
    path("other-resources", views.OtherResourcesView.as_view(), name="other-resources"),
    path("pro_version", views.ProVersionView.as_view(), name="pro_version"),
    path(
        "pro_version_thankyou",
        views.ProVersionThankYouView.as_view(),
        name="pro_version_thankyou",
    ),
    path("process", views.ProcessView.as_view(), name="process"),
    path("privacy_policy", views.PrivacyPolicyView.as_view(), name="privacy_policy"),
    path("share_denial", views.ShareDenialView.as_view(), name="share_denial"),
    path("share_appeal", views.ShareAppealView.as_view(), name="share_appeal"),
    path("remove_data", views.RemoveDataView.as_view(), name="remove_data"),
    path(
        "tos",
        cache_control(public=True)(
            cache_page(60 * 60 * 2)(views.TermsOfServiceView.as_view())
        ),
        name="tos",
    ),
    path("find_next_steps", views.FindNextSteps.as_view(), name="find_next_steps"),
    path("generate_appeal", views.GenerateAppeal.as_view(), name="generate_appeal"),
    path(
        "appeals_json_backend",
        views.AppealsBackend.as_view(),
        name="appeals_json_backend",
    ),
    path("choose_appeal", views.ChooseAppeal.as_view(), name="choose_appeal"),
    path(
        "contact",
        cache_control(public=True)(
            cache_page(60 * 60 * 2)(views.ContactView.as_view())
        ),
        name="contact",
    ),
]
