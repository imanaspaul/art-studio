import uuid
from django.db import models



class Competition(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Competition name')
    description = models.TextField(verbose_name='Competition description')
    thumnail = models.URLField(verbose_name='Competition thumbnail')
    ended = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Competitions"
        get_latest_by = "-created_at"
        ordering = ['-created_at']

