from django.db import models
from django.utils.safestring import mark_safe

class Shop(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.name
    
    def imege_tag(self):
        return mark_safe('<img src="/mediafile/%s" width="100" height="100" />' % (self.imege))
    
    imege_tag.short_description='imege'

    