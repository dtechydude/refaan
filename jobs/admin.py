from django.contrib import admin
from .models import Post #Category

class PostAdmin(admin.ModelAdmin):
    model = Post
    # fields =
    list_display = ('author', 'title', 'date_posted')
    list_filter = ['author']
    search_fields = ['question_text']
    prepopulated_fields = {'slug': ('title',)}  # prepopulating the slug

admin.site.register(Post, PostAdmin)
#admin.site.register(Category)
