from django.contrib import admin

# Register your models here.
from .models import Project, Projectstatus, Customer, Partner, Projectcategory
from .models import Contract, Customersegment, Contracttype, Momserahterima
# from .models import Lintasartaperson, Order, Scope, Servicelevelagreement
from .models import Lintasartaperson, Order,Contractwithpartner
from import_export.admin import ImportExportModelAdmin

# @admin.register(Project)
class CustomerAdmin(ImportExportModelAdmin):
	pass

admin.site.register(Project);
admin.site.register(Projectcategory);
admin.site.register(Customer,CustomerAdmin);
admin.site.register(Customersegment);
admin.site.register(Partner);
admin.site.register(Order);
admin.site.register(Contract);
admin.site.register(Contracttype);
admin.site.register(Lintasartaperson);
admin.site.register(Momserahterima);
# admin.site.register(Contractwithpartner);
admin.site.register(Projectstatus);