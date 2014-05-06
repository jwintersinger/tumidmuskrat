from django.contrib import admin
from blog.models import Post
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
  prepopulated_fields = {'slug': ('title',)}

  def save_model(self, request, obj, form, change):
    obj.user = request.user
    obj.save()

admin.site.register(Post, PostAdmin)
