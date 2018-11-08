from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Deal)
admin.site.register(Incentiveprogram)
admin.site.register(Dealtype)
admin.site.register(Dealobjective)
admin.site.register(Programindustryactivity)
admin.site.register(Programindustrysector)
