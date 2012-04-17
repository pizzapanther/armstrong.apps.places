from django.contrib import admin
from django.utils.translation import ugettext as _

from armstrong.core.arm_content.admin import fieldsets

from .models import Place

class PlaceAdmin (admin.ModelAdmin):
  fieldsets = (
      (None, {
          'fields': ('title', 'slug', 'summary'),
      }),
      
      (_('Location'), {
          'fields': ('address1', 'address2', ('city', 'state'), ('zipcode', 'country')),
      }),

      fieldsets.TAXONOMY,
      fieldsets.PUBLICATION,
      fieldsets.AUTHORS,
  )
  
admin.site.register(Place, PlaceAdmin)
