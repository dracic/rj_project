from django.contrib import admin
from .models import UŠP, GJ


class UŠPAdmin(admin.ModelAdmin):
    list_display = ('ušp_id', 'ušp_naziv')
    search_fields = ['ušp_id', 'ušp_naziv']
    ordering = ['ušp_id']


class GJAdmin(admin.ModelAdmin):
    list_display = ('ušp', 'gj_id', 'gj_naziv', 'godina', 'vrsta_elaborata', 'obraslo', 
                    'neobraslo_proizvodno', 'neobraslo_neproizvodno', 
                    'neplodno', 'povrsina', 'drvna_zaliha_debljinski_razredi', 
                    'drvna_zaliha_dobni_razredi', 'prirast_debljinski_razredi', 
                    'prirast_dobni_razredi', 'oos_povrsina', 'oos_zaliha', 
                    'gp_povrsina', 'gp_zaliha', 'pp_povrsina', 'pp_zaliha')
    search_fields = ['gj_id', 'gj_naziv']
    ordering = ['ušp', 'gj_id']


admin.site.register(UŠP, UŠPAdmin)
admin.site.register(GJ, GJAdmin)
