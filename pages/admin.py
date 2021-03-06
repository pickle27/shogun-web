
# Import objetts.
from pages.models import NavBar
from pages.models import ShogunPage
from pages.models import Article
from pages.models import New

from django.contrib import admin

# HTML Editor
class ArticleOptions(admin.ModelAdmin):
	class Media:
		js = ('../static/js/tiny_mce/tiny_mce.js',
			  '../static/js/editors/textfield.js')

class NewOptions(admin.ModelAdmin):
	class Media:
		js = ('../static/js/tiny_mce/tiny_mce.js',
			  '../static/js/editors/textfield.js')

# Objects editable by admin.
admin.site.register(NavBar)
admin.site.register(ShogunPage)
admin.site.register(Article, ArticleOptions)
admin.site.register(New, NewOptions)
