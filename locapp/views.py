from django.shortcuts import render
from folium import *

def daily(request):
	return render(request, "daily.html")

def thane(request):
	loc = [19.1872, 72.9739]
	f = Figure(width=800, height=800)
	th = Map(location=loc, zoom_start=20).add_to(f)
	Marker(loc, tooltip="Kamal Classes Thane").add_to(th)
	th_html = th._repr_html_()
	return render(request,"thane.html",{"msg":th_html})	

def borivali(request):
	loc = [19.22800, 72.85768]
	f = Figure(width=800, height=800)
	bo = Map(location=loc, zoom_start=20).add_to(f)
	Marker(loc, tooltip="Kamal Classes Borivali").add_to(bo)
	bo_html = bo._repr_html_()
	return render(request,"borivali.html",{"msg":bo_html})	