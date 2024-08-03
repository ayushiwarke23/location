from django.contrib import admin
from django.urls import path
from locapp.views import daily, thane, borivali

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",daily, name="daily"),
    path("thane",thane, name="thane"),
    path("borivali", borivali, name="borivali"),
]
