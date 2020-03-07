from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


STATUS = ((0,_('Pending')),(1,_('Done')))


class Config(models.Model):


	cnf_lap_time = models.PositiveIntegerField(verbose_name=_('Pomodoros Time'))

	cnf_time_short_brake = models.PositiveIntegerField(verbose_name=_('Time Short Brake'),)

	cnf_time_long_brake = models.PositiveIntegerField(verbose_name=_('Time Long Brake'),)

	cnf_created_date = models.DateTimeField(default=timezone.now, verbose_name=_('Creation Date'))
	
	cnf_modified_date = models.DateTimeField(default=timezone.now, verbose_name=_('Modification Date'))

	cnf_creator = models.ForeignKey(User, verbose_name=_('Creator'), on_delete=models.CASCADE)




	
	def __str__(self):
		return self.cnf_lap_time + " - " + cnf_time_short_brake + " - " + cnf_time_long_brake


	class Meta:
	    verbose_name = _('Config')
	    verbose_name_plural = _('Configs')





