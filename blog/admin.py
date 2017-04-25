from django.contrib import admin
from .models import Post # models파일에 있는 Post객체 사용하겠다.

# Register your models here.

admin.site.register(Post)