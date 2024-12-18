from django.contrib import admin
from .models import Category, Questions, Quiz, UserQuizScore
# Register your models here.

admin.site.register(Category)
admin.site.register(Questions)
admin.site.register(Quiz)
admin.site.register(UserQuizScore)