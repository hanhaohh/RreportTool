from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
import urllib2
import json
from django.db.models import Count
from django.shortcuts import render_to_response  
import classify
def chutu(request):
	return render_to_response("chutu.html")
def bia(request):
	return render_to_response("bia656.html")
def net3(request):
	return render_to_response("net3.html")
def map(request):
	return render_to_response("us.html")

def about(request):
	return render_to_response("home.html")
def prediction(request):
    news = request.GET['news']
    #prediction = classify.cl(news)
    prediction ="1"	
    if prediction=="1":
        return render_to_response("prediction.html",{"prediction":prediction,"img":"http://th05.deviantart.net/fs71/PRE/f/2011/288/9/e/troll_face_by_rober_raik-d4cwjh0.png"})
    if prediction=="-1":
        return render_to_response("prediction.html",{"prediction":prediction,"img":"http://th08.deviantart.net/fs71/PRE/f/2011/290/d/9/emotion_meme_by_rober_raik-d4d3z9p.png"})
    if prediction=="0":
        return render_to_response("prediction.html",{"prediction":prediction,"img":"http://th04.deviantart.net/fs71/PRE/f/2011/288/d/6/poker_face_2_by_rober_raik-d4cxlfn.png"})
def d3(request):
	return render_to_response("barchat.html")
def main(request):
	return render_to_response("main.html")
def rfm	(request):
	return render_to_response("rfm.html")
def stock(request):
	return render_to_response("stock.html")
def home_1 (request):
	return render_to_response("index.html")
