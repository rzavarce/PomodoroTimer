from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


# Create your models here.


STATUS = ((0,_('Pending')),(1,_('Done')))


class Task(models.Model):


	tsk_title = models.CharField(max_length=150, verbose_name=_('Nickname'))

	tsk_description = models.TextField(verbose_name=_('Description'), blank=True, null=True,)

	tsk_config = models.ForeignKey('configs.Config', verbose_name=_('Configuration'), on_delete=models.CASCADE)

	tsk_status = models.PositiveIntegerField(choices=STATUS, verbose_name=_('Status'),)

	tsk_assignted_time = models.PositiveIntegerField(verbose_name=_('Assignated Time'),)

	tsk_created_date = models.DateTimeField(default=timezone.now, verbose_name=_('Creation Date'))
	
	tsk_modified_date = models.DateTimeField(default=timezone.now, verbose_name=_('Modification Date'))

	tsk_creator = models.ForeignKey(User, verbose_name=_('Creator'), on_delete=models.CASCADE)



	
	def __str__(self):
		return self.tsk_title


	class Meta:
	    verbose_name = _('Task')
	    verbose_name_plural = _('Tasks')

