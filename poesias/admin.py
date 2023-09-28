# Register your models here.

from django.contrib import admin
import poesias.models as models
from django.utils.html import mark_safe

admin.site.register(models.Autor)
admin.site.register(models.Categoria)
admin.site.register(models.Poesia)
admin.site.register(models.Venda)

@admin.register(models.Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao',)
    list_filter = ('autor', 'categorias',)
    search_fields = ('titulo', 'autor', 'categorias',)
    readonly_fields = ('imagem_preview',)

    def imagem_preview(self, obj):
        return mark_safe(f'<img src="{obj.imagem.url}" width="50" />')