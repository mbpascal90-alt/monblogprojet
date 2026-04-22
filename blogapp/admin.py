from django.contrib import admin
from blogapp.models import Article

# Enregistrer votre modèle ici

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','auteur','date_creation')
    list_filter = ('date_creation',)
    search_fields = ('titre', 'contenu')

admin.site.register(Article, ArticleAdmin)
