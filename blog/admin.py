from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}

  def save_model(self, request, obj, form, change):
    obj.user = request.user
    obj.save()

admin.site.register(Post, PostAdmin)
