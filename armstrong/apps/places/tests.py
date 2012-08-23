import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse, resolve

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

from .models import Place

class PlacesTestCase (TestCase):
  def setUp(self):
    self.home = Place(
      address1 = '1206 Halls Bridge',
      address2 = None,
      zipcode = '77573',
      city = 'League City',
      state = 'TX',
      country = 'US',
      coordinate = Point(-95.087372, 29.516589),
      
      pub_date = datetime.datetime.now()
    )
    self.home.save()
    
    self.work = Place(
      address1 = '3657 Briarpark Drive',
      address2 = 'Suite 101',
      zipcode = '77042',
      city = 'Houston',
      state = 'TX',
      country = 'US',
      coordinate = Point(-95.54835, 29.72546),
      
      pub_date = datetime.datetime.now()
    )
    self.work.save()
    
  def tearDown(self):
    self.home.delete()
    self.work.delete()
    
  def test_model (self):
    bay_brook_mall = Point(-95.14820, 29.54211)
    qs = Place.objects.filter(coordinate__distance_lte=(bay_brook_mall, D(mi=5)))
    self.assertEqual(qs.count(), 1)
    self.assertEqual(qs[0].id, self.home.id)
    
    qs = Place.objects.filter(coordinate__distance_lte=(bay_brook_mall, D(mi=30)))
    self.assertEqual(qs.count(), 2)
    