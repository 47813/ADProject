from django.contrib import admin
from .models import Video, BorrowHistory

admin.site.register(Video)
admin.site.register(BorrowHistory)