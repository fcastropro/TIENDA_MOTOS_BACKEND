from django.contrib import admin
from .models import PaymentMethod, Invoice, InvoiceDetail

admin.site.register(PaymentMethod)
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
