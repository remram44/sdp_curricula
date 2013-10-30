from django.db import models
import logging

logger = logging.getLogger(__name__)

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    url = models.CharField(max_length=200, blank=True)
    #image = models.ImageField(upload_to="article_img", help_text=""" Upload jpg or png files """)
    
    def __unicode__(self):
      return self.title