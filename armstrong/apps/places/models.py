from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

from armstrong.apps.content.models import Content

class Place (Content):
  address1 = models.CharField(_('Address 1'), max_length=100, blank=True, null=True)
  address2 = models.CharField(_('Address 2'), max_length=100, blank=True, null=True)
  zipcode = models.CharField(_('Zip code'), max_length=30, blank=True, null=True)
  city = models.CharField(max_length=100, blank=True, null=True)
  state = models.CharField(_('State/Province'), max_length=100, blank=True, null=True)
  country = models.CharField(max_length=100, blank=True, null=True)
  
  location = models.PointField()
  
  objects = models.GeoManager()
  