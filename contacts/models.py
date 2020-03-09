from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


STATUS = ( (0,_('Active')),(2,_('Pending')),(3,_('Done')))


class Contact(models.Model):

	cnt_name = models.CharField(max_length=150, verbose_name=_('Name'), blank=True, null=True)

	cnt_email = models.EmailField(verbose_name=_('Email'),)

	cnt_message = models.TextField(verbose_name=_('Message'),)

	cnt_status = models.PositiveIntegerField(choices=STATUS, verbose_name=_('Status'),)

	cnt_created_date = models.DateTimeField(default=timezone.now, verbose_name=_('Creation Date'))
	
	cnt_modified_date = models.DateTimeField(default=timezone.now, verbose_name=_('Modification Date'))

	cnt_creator = models.ForeignKey(User, verbose_name=_('Creator'), on_delete=models.CASCADE)




	
	def __str__(self):
		return str(self.cnt_name)


	class Meta:
	    verbose_name = _('Contact')
	    verbose_name_plural = _('Contact')





