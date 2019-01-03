from django.contrib import admin

# Register your models here.
from .models import Project, Projectstatus, Customer, Partner
from .models import Contract, Customersegment, Contracttype, Projectcategory
# from .models import Lintasartaperson, Order, Scope, Servicelevelagreement
from .models import Lintasartaperson, Order

admin.site.register(Project)
admin.site.register(Projectstatus)
admin.site.register(Customer)
admin.site.register(Customersegment)
admin.site.register(Partner)
admin.site.register(Projectcategory)
admin.site.register(Order)
admin.site.register(Contract)
admin.site.register(Contracttype)
admin.site.register(Lintasartaperson)
# admin.site.register(Servicelevelagreement)
