from django.db import models

# Create your models here.

class DefendantDocumentType(models.Model):
    doc_type = models.CharField('Category name', max_length=250)   
    description = models.TextField('Description', null=True, blank=True)   
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name = ("defendant doc category")
        verbose_name_plural = ("defendant doc category")

    def __str__(self) -> str:
        return "%s" % (self.id)


class ClaimantDocumentType(models.Model):
    doc_type = models.CharField('Category name', max_length=250)
    description = models.TextField('Description', null=True, blank=True)   
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name = ("claimant doc category")
        verbose_name_plural = ("claimant doc categories")

    def __str__(self) -> str:
        return "%s" % (self.id)