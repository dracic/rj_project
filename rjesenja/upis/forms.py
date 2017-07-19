from django import forms
from .models import UŠP, GJ

class GJForm(forms.ModelForm):

    class Meta:
        model = GJ
        fields = ('ušp', 'gj_id', 'gj_naziv', 'godina', 'vrsta_elaborata', 'obraslo', 
                    'neobraslo_proizvodno', 'neobraslo_neproizvodno', 
                    'neplodno', 'drvna_zaliha_debljinski_razredi', 
                    'drvna_zaliha_dobni_razredi', 'prirast_debljinski_razredi', 
                    'prirast_dobni_razredi', 'oos_povrsina', 'oos_zaliha', 
                    'gp_povrsina', 'gp_zaliha', 'pp_povrsina', 'pp_zaliha')