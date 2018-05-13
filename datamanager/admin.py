from django.contrib import admin
from .models import *
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

# Register your models here.
admin.site.register(Settings)
admin.site.register(SettingType)


class SecurityResource(resources.ModelResource):

    security_type = fields.Field(
        column_name='security_type',
        attribute='security_type',
        widget=ForeignKeyWidget(SecurityType, 'security_type'))

    security_class = fields.Field(
        column_name='security_class',
        attribute='security_class',
        widget=ForeignKeyWidget(SecurityClass, 'security_class'))

    class Meta:
        model = Security
        fields = ('id','name','symbol','security_type','security_class','benchmark','management_expense_ratio','admission_date','fetch_data')



class SecurityTypeResource(resources.ModelResource):

    class Meta:
        model = SecurityType

class SecurityClassResource(resources.ModelResource):

    class Meta:
        model = SecurityClass


class SecurityDividendResource(resources.ModelResource):
    security = fields.Field(
        column_name='symbol',
        attribute='security',
        widget=ForeignKeyWidget(Security, 'symbol'))

    class Meta:
        model = SecurityDividend
        fields = ('id','franking_percentage','notes','payable_date','dividend_per_share','ex_dividend_date','dividend_date','symbol','dividend_type')

class SecurityAdmin(ImportExportModelAdmin):
    resource_class = SecurityResource
    pass

class SecurityDividendAdmin(ImportExportModelAdmin):
    resource_class = SecurityDividendResource
    pass

class SecurityTypeAdmin(ImportExportModelAdmin):
    resource_class =  SecurityTypeResource
    pass

class SecurityClassAdmin(ImportExportModelAdmin):
    resource_class =  SecurityClassResource
    pass


admin.site.register(Security, SecurityAdmin)
admin.site.register(SecurityType, SecurityTypeAdmin)
admin.site.register(SecurityClass, SecurityClassAdmin)
admin.site.register(SecurityDividend, SecurityDividendAdmin)
admin.site.register(SecurityDailyPrice)
