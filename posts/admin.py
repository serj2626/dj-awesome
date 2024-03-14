from django.contrib import admin
from .models import Post, Tag, Comment, Reply


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post)'''

    list_display = ('title',  'body', 'url_image')
    filter_horizontal = ('tags',)

    # add func return image[:30]
    def url_image(self, obj):
        return str(obj.image)[:26]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    '''Admin View for Tag)'''

    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment)'''

    list_display = ('author', 'post', )


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    '''Admin View for Reply)'''

    list_display = ('author', 'parent_comment', 'created')
