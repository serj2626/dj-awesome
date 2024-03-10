from posts.models import Tag

def all_tags(request):
    return {'tags': Tag.objects.all()}