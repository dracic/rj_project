from django.db import models
from django.urls import reverse


class UŠP(models.Model):
    ušp_id = models.CharField(max_length=2, unique=True)
    ušp_naziv = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.ušp_naziv

    class Meta:
        ordering = ["ušp_id"]
        verbose_name = "Uprava šuma podružnica"
        verbose_name_plural = "UŠP"

class GJ(models.Model):
    VRSTE_ELABORATA = (
        ('Program', 'Program'),
        ('Osnova', 'Osnova'),
    )

    ušp = models.ForeignKey(UŠP, related_name='gjs')
    gj_id = models.CharField(max_length=3, unique=True)
    gj_naziv = models.CharField(max_length=100)
    godina = models.PositiveSmallIntegerField(null=False, blank=False)
    vrsta_elaborata = models.CharField(max_length=10, choices=VRSTE_ELABORATA, default='Osnova')
    obraslo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    neobraslo_proizvodno = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    neobraslo_neproizvodno = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    neplodno = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    povrsina = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    drvna_zaliha_debljinski_razredi = models.PositiveIntegerField(default=0)
    drvna_zaliha_dobni_razredi = models.PositiveIntegerField(default=0)
    drvna_zaliha = models.PositiveIntegerField(default=0, editable=False)
    prirast_debljinski_razredi = models.PositiveIntegerField(default=0)
    prirast_dobni_razredi = models.PositiveIntegerField(default=0)
    prirast = models.PositiveIntegerField(default=0, editable=False)
    oos_povrsina = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    oos_zaliha = models.PositiveIntegerField(default=0)
    gp_povrsina = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gp_zaliha = models.PositiveIntegerField(default=0)
    pp_povrsina = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pp_zaliha = models.PositiveIntegerField(default=0)
    etat_povrsina = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    etat_zaliha = models.PositiveIntegerField(default=0, editable=False)

    def save(self):
        self.povrsina = int(self.obraslo + self.neobraslo_proizvodno + self.neobraslo_neproizvodno + self.neplodno) 
        self.drvna_zaliha = int(self.drvna_zaliha_debljinski_razredi + self.drvna_zaliha_dobni_razredi)
        self.prirast = int(self.prirast_debljinski_razredi + self.prirast_dobni_razredi)
        self.etat_povrsina = int(self.oos_povrsina + self.gp_povrsina + self.pp_povrsina)
        self.etat_zaliha = int(self.oos_zaliha + self.gp_zaliha + self.pp_zaliha)
        super(GJ, self).save()

    def get_absolute_url(self):
        return reverse("gj_detail",kwargs={'pk':self.pk})

    def __str___(self):
        return self.gj_naziv


    class Meta:
        ordering = ["ušp", "gj_id"]
        verbose_name = "Gospodarska jedinica"
        verbose_name_plural = "Gospodarske jedinice"



