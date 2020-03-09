from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Config(models.Model):

	cnf_title = models.CharField(max_length=150, verbose_name=_('Nickname'), blank=True, null=True)

	cnf_lap_time = models.PositiveIntegerField(verbose_name=_('Pomodoros Time'), default=25)

	cnf_time_short_brake = models.PositiveIntegerField(verbose_name=_('Time Short Brake'), default=5)

	cnf_time_long_brake = models.PositiveIntegerField(verbose_name=_('Time Long Brake'), default=10)

	cnf_created_date = models.DateTimeField(default=timezone.now, verbose_name=_('Creation Date'))
	
	cnf_modified_date = models.DateTimeField(default=timezone.now, verbose_name=_('Modification Date'))

	cnf_creator = models.ForeignKey(User, verbose_name=_('Creator'), on_delete=models.CASCADE)

	
	def __str__(self):
		#return str(self.cnf_lap_time) + " - " + str(self.cnf_time_short_brake) + " - " + str(self.cnf_time_long_brake)
		return str(self.cnf_title)


	class Meta:
	    verbose_name = _('Config')
	    verbose_name_plural = _('Configs')



