from django.contrib import admin
from .models import Quiz,Question,Option,Take,Responses
# Register your models here
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Take)
admin.site.register(Responses)
