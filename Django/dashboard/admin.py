from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Deal)
admin.site.register(Incentiveprogram)
admin.site.register(Dealprogram)
admin.site.register(Programbusinessneeds)
admin.site.register(Programcategory)
admin.site.register(Programgeographicfocus)
admin.site.register(Programindustry)
admin.site.register(Programtype)