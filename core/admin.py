from django.contrib import admin

from .models import Usuario
from .models import Publico
from .models import Area
from .models import Curso

admin.site.register(Usuario)
admin.site.register(Publico)
admin.site.register(Area)
admin.site.register(Curso)