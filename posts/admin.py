from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post)'''

    list_display =  ('title',  'body', 'url_image' )

    #add func return image[:30]
    def url_image(self, obj):
        return str(obj.image)[:26]