import datetime
from django.db import models

class Day(models.Model):
    # name = models.CharField(max_length=10, null=False, unique=True)
    name = models.CharField(max_length=10, unique=True, blank=False, null=False)
    slug = models.CharField(max_length=100, unique=True, blank=False, null=False)
    # Slots

    def __str__(self):
        return self.name


class Slot(models.Model):
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    day = models.ForeignKey(Day, related_name='slots', on_delete=models.CASCADE)

    def __str__(self):
        hhmm_start = self.start.isoformat("minutes")
        hhmm_end = self.end.isoformat("minutes")
        return f'{hhmm_start} - {hhmm_end}'

