from django.db import models
import logging

logger = logging.getLogger(__name__)

class Article(models.Model):

    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000000, blank=True)
    url = models.CharField(max_length=200, blank=True)
    sort_order = models.PositiveIntegerField(blank=False, null=False)
    
    class Meta(object):
        ordering = ('sort_order',)
        
    def __unicode__(self):
      return self.title