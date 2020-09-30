from django.db import models


class VatCodes(models.Model):
    vat_code = models.CharField(max_length=3, blank=False, null=False, primary_key=True)
    description = models.CharField(max_length=10)
    tax_perc = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Vat Code"
        verbose_name_plural = "Vat Codes"


class PaymentMethods(models.Model):
    description = models.CharField(max_length=20)

    class Meta:
        verbose_name = "payment method"
        verbose_name_plural = "payment methods"


class Suppliers(models.Model):
    company_name = models.CharField(max_length=100, blank=False, null=False)
    vat_number = models.CharField(max_length=11)
    cf_number = models.CharField(max_length=16)
    address = models.CharField(max_length=100)
    cap = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    prov = models.CharField(max_length=10)
    country_state = models.CharField(max_length=10, null=True, blank=True)
    gg_valuta = models.IntegerField()
    sds_path = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #standard data
    vat_perc = models.ForeignKey('VatCodes', on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "supplier"
        verbose_name_plural = "suppliers"

    def __str__(self):
        return self.company_name


class ChemProds(models.Model):
    supplier = models.ForeignKey('Suppliers', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    solvent = models.BooleanField()
    perc_solv = models.IntegerField()
    wet_dep = models.BooleanField()
    fin_dep = models.BooleanField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "chemical product"
        verbose_name_plural = "chemical products"

    def __str__(self):
        return self.description


class PriceLists(models.Model):
    product = models.ForeignKey('ChemProds', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "price list"
        verbose_name_plural = "price lists"


class InvoiceHeaders(models.Model):
    inv_number = models.CharField(max_length=20, blank=False, null=False)
    inv_date = models.DateField()
    supplier = models.ForeignKey('Suppliers', on_delete=models.CASCADE)


    class Meta:
        verbose_name = "invoice header"
        verbose_name_plural = "invoice headers"

    def __str__(self):
        return ({self.inv_date}, {self.inv_number})


class InvoiceDetails(models.Model):
    invoice = models.ForeignKey('InvoiceHeaders', on_delete=models.CASCADE)
    chem_prod = models.ForeignKey('ChemProds', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    perc_sov = models.IntegerField()

    class Meta:
        verbose_name = "invoice detail"
        verbose_name_plural = "invoice details"



class ChemSubstances(models.Model):
    substance = models.CharField(max_length=200)
    ec_number = models.CharField(max_length=30)
    cas_number = models.CharField(max_length=30)
    selected = models.BooleanField()

    class Meta:
        verbose_name = "chemical substance"
        verbose_name_plural = "chemical substances"

    def __str__(self):
        return self.substance




class SvhcSubstances(models.Model):
    svhc_substance = models.CharField(max_length=200)
    ec_number = models.CharField(max_length=30)
    cas_number = models.CharField(max_length=30)
    inclusion_date = models.DateField()
    inclusion_reason = models.CharField(max_length=100)
    decision_number = models.CharField(max_length=50)

    class Meta:
        verbose_name = "svhc substance"
        verbose_name_plural = "svhc substances"

    def __str__(self):
        return self.svhc_substance


class HazardStatements(models.Model):
    code = models.CharField(max_length=20)
    descritpion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "hazard statement"
        verbose_name_plural = "hazard statements"

    def __str__(self):
        return self.code

class HazardPictograms(models.Model):
    pictogram = models.ImageField()
    description = models.CharField(max_length=30)

    class Meta:
        verbose_name = "hazard pictogram"
        verbose_name_plural = "hazard pictograms"


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    vat_number = models.CharField(max_length=11)
    cf_number = models.CharField(max_length=16)
    address = models.CharField(max_length=100)
    cap = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=100)
    prov = models.CharField(max_length=10, null=True, blank=True)
    country_state = models.CharField(max_length=10)
    logo = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
