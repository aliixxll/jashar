from django.contrib import admin
from settings.models import Setting, AboutUs, Team, News, Contact

# Register your models here.
admin.site.register(Setting)
admin.site.register(AboutUs)
admin.site.register(Team)
admin.site.register(News)
admin.site.register(Contact)