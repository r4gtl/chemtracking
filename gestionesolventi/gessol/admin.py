from django.contrib import admin

from gessol.models import (ChemProds, ChemSubstances,
                          Company,
                          HazardPictograms, HazardStatements,
                          InvoiceDetails, InvoiceHeaders,
                          PaymentMethods, PriceLists,
                          Suppliers, SvhcSubstances,
                          VatCodes)


admin.site.register(ChemProds)
admin.site.register(ChemSubstances)
admin.site.register(Company)
admin.site.register(HazardPictograms)
admin.site.register(HazardStatements)
admin.site.register(InvoiceDetails)
admin.site.register(InvoiceHeaders)
admin.site.register(PaymentMethods)
admin.site.register(PriceLists)
admin.site.register(Suppliers)
admin.site.register(SvhcSubstances)
admin.site.register(VatCodes)
