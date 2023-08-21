from django.db import models
from customer.models import Customer
from smart_selects.db_fields import ChainedForeignKey
from django.shortcuts import get_object_or_404
from django.utils import timezone



class Deductions(models.Model):
    unikey = models.CharField(max_length=300)
    payer = models.IntegerField()
    assignment = models.CharField(max_length=200)
    clerks = models.IntegerField()
    type = models.CharField(max_length=2)
    doc_date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    text = models.CharField(max_length=300, blank=True, null=True)
    clearing_doc = models.IntegerField(blank=True, null=True)
    clearing_date = models.DateField(blank=True, null=True)
    reason_code = models.CharField(max_length=3, blank=True)
    dunning_block = models.CharField(max_length=3, blank=True)
    billing_doc = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Deduction {self.pk}"
    
    class Meta:
        verbose_name = 'Deduction'
        verbose_name_plural = '1. Deductions'


class Analysis(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Analysis'
        verbose_name_plural = '2. Analysis'


class RootCause(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'RootCause'
        verbose_name_plural = '3. Rootcauses'

class Action(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE, blank=True, null=True)
    rootcause = ChainedForeignKey(
        RootCause, 
        chained_field='analysis',
        chained_model_field='analysis') #on_delete=models.CASCADE
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Action'
        verbose_name_plural = '4. Actions'

 
class Owner(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = '5. Owners'


class CollectorsInput(models.Model):
    OPTION_COM = [
        ('1st Communication','1st Communication'),
        ('Multiple communications', 'Multiple communications'),
    ]

    unikey = models.CharField(max_length=300, help_text="This is the unique identifier for the deduction.")
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE, blank=True, null=True)
    rootcause =  models.ForeignKey(RootCause, on_delete=models.CASCADE, blank=True, null=True)
    action =  models.ForeignKey(Action, on_delete=models.CASCADE, blank=True, null=True)
    owner =  models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)
    action_date = models.DateField(blank=True, null=True)
    nb_com = models.CharField(max_length=100, choices=OPTION_COM, blank=True)
    proof_com = models.CharField(max_length=50, blank=True)
    comment = models.TextField(max_length=2000,blank=True, null=True)

    def get_collectors_input_by_unikey(unikey_value):
        collectors_input_instance = get_object_or_404(CollectorsInput, unikey=unikey_value)
        deductions_instance = collectors_input_instance.unikey
        return collectors_input_instance, deductions_instance

    class Meta:
        unique_together = ('unikey', 'analysis', 'rootcause', 'action')   
        verbose_name = 'Collector analysis'
        verbose_name_plural = "6. Collector's analysis"

    def __str__(self):
        return self.unikey
   
    def save(self, *args, **kwargs):
        if not self.action_date:
            self.action_date = timezone.now().date()
            
        existing_record = CollectorsInput.objects.filter(unikey=self.unikey, analysis__isnull=False).first()

        if existing_record:
            # If a record with the same unikey and a non-null analysis exists, update it
            # with the new data.
            existing_record.analysis = self.analysis
            existing_record.rootcause = self.rootcause
            existing_record.action = self.action
            existing_record.owner = self.owner
            existing_record.action_date = self.action_date
            existing_record.nb_com = self.nb_com
            existing_record.proof_com = self.proof_com
            existing_record.comment = self.comment
            existing_record.action_date = self.action_date

            existing_record.save()
        else:
            # If no such record exists, save the new data as a new record.
            super().save(*args, **kwargs)

