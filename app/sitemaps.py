# blog/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Post  # 適切なモデルをインポート
from django.shortcuts import resolve_url

class BaseSitemap(Sitemap):
    def items(self):
        items = [
            'app:index',
        ]
        return items
    
    def location(self, obj):
        return resolve_url(obj)
    
    def changefreq(self, obj):
        return 'always'
    
    def priority(self, obj):
        if obj == 'app:index':
            return 1
        else:
            return 0.1


   