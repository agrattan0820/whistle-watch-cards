from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("ping", views.current_datetime, name="ping"),
    path("signin", views.signin, name="signin"),
    path("create-account", views.create_account, name="create-account"),
    path("job/<uuid:job_id>", views.JobDetailView.as_view(), name="job-details"),
    path("job/<uuid:job_id>/apply", views.job_apply, name="job-apply"),
]
