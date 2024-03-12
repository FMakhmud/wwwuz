from ckeditor.fields import RichTextField
from django.db import models
from utils.models import BaseModel
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Direction(BaseModel):
    title = RichTextField(max_length=32, verbose_name=_('Title'))
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class SiteType(BaseModel):
    title = models.CharField(max_length=32, verbose_name=_('Title'))

    def __str__(self):
        return self.title


class Site(BaseModel):
    title = models.CharField(max_length=32, verbose_name=_('Title'))
    direction = models.ForeignKey(Direction,
                                  on_delete=models.CASCADE,
                                  verbose_name=_('Direction')
                                  )
    url = models.URLField()
    about = models.TextField(null=True, blank=True)
    types = models.ManyToManyField(SiteType)

    def __str__(self):
        return self.title


class SiteLog(BaseModel):
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, related_name='logs')
    visitor_count = models.IntegerField(default=0)

    # @classmethod
    # def is_available(cls, site, day):
    #     if cls.objects.filter(site=site, created_at__date=day).exists():
    #         return True
    #     return False

    def update_visitor_count(self):
        self.visitor_count += 1
        self.save()
