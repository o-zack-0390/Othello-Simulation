from django.contrib import admin
from .models import Status
from .models import Skill
from .models import Combo_Skill

# Register your models here.
admin.site.register(Status)
admin.site.register(Skill)
admin.site.register(Combo_Skill)