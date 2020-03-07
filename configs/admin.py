from django.contrib import admin

from .models import Config





class ConfigsAdmin(admin.ModelAdmin):

    list_display = ('cnf_lap_time', 'cnf_time_short_brake', 'cnf_time_long_brake', 'cnf_creator',)
    list_filter = ('cnf_lap_time', 'cnf_time_short_brake',)
    ordering = ('cnf_creator',)
    search_fields = ('cnf_creator',)    


    #fields = ['nickname', 'bike_category', 'bike_model', 'bike_serie', 'registration_number', 'manufacturing_year', 'manufacturer', 'engines_type', 'description', 'status', 'status_dry', 'client', 'device' ]

       		

admin.site.register(Config, ConfigsAdmin)
