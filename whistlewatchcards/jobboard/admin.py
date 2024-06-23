from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Club, Assignor, Referee, Job, Application, Assignment, AssignorClub

admin.site.register(User, UserAdmin)
admin.site.register(Club)
admin.site.register(Assignor)
admin.site.register(AssignorClub)
admin.site.register(Referee)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Assignment)
