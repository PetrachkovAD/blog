from django.db import models


class Blog(models.Model):
    headerArticale = models.CharField(max_length=50)
    articale = models.TextField()
    cutArtical = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    autor = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    isReady = models.BooleanField()
    description = models.CharField(max_length=50)
    keyWords = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return u"{}".format(self.headerArticale)

    def __str__(self):
        return self.headerArticale

    def publish(self):
        self.isReady = True
        self.save()
