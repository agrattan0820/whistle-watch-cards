import datetime
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from jobboard.models import Job


class IndexView(ListView):
    model = Job
    template_name = "index.html"


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def signin(request):
    return HttpResponse("Signin page.")


def create_account(request):
    return HttpResponse("Create account page.")


def job_details(request):
    return HttpResponse("Job details page.")

class JobDetailView(DetailView):
    model = Job
    template_name = "job_detail.html"

    def get_object(self, queryset=None):
        return Job.objects.get(id=self.kwargs.get("job_id"))


def job_apply(request):
    return HttpResponse("Job apply page.")
