from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import *
from django.db.models import Count, Min, Sum, Avg
def dashboard(request,template_name):
    if  request.user.is_authenticated():
        username = request.user
        chart_url1 = "/media/img/nits.png"
        chart_url2 = "/media/img/plc.png"
        chart_url3 = "/media/img/anual_volume.png"
        chart_corr = "/media/img/corr.png"
	chart_url4 = "/media/img/entity.png"
	chart_url5 = "/media/img/e_g.png"
	chart_url6 = "/media/img/month.png"
	chart_url7 = "/media/img/m2.png"
        chart_k = "/media/img/k.png"
        a1 =["Cluster 1",49.284095986548721, 40.159312556773429, 44.283772792891014, 54.185784138688618, 60.293691651397175, 56.876953452872911, 47.91250225726899, 40.532793800204075, 45.786786031543571, 57.842801579589505]
        a2 =["Cluster 2",4.7109472435012485, 3.2735038258827576, 2.2459080276347798, 2.2926823999360693, 2.4983787243805295, 2.3772294492668706, 2.1307434059362329, 2.2219924923653913, 3.0636180761576171, 4.2529219824225066]
        a3 = ["Cluster 3",88.494749163634594, 73.487420357540415, 84.697961257942339, 100.04854923684627, 112.60436173211539, 103.6797771803943, 89.319936852286489, 74.930603233255795, 82.71617918392117, 108.53777652515387]
        a4 = ["Cluster 4",22.905311481743244, 19.925079753434581, 23.688029380818488, 30.783272405998485, 35.628409702232616, 33.29342027189881, 27.133177171195918, 21.593631099281783, 21.982064015361026, 25.498634597581386]
        dic = [a1,a2,a3,a4]
        return render_to_response(template_name,{"username":username,"chart1":chart_url1,"chart2":chart_url2,"chart3":chart_url3,"corr":chart_corr,"chart_k":chart_k,"k":dic,
	"chart4":chart_url4,"chart5":chart_url5	,"chart6":chart_url6,"chart7":chart_url7})

    else:
        return HttpResponseRedirect('/login/')
def second(request,template_name):
    if  request.user.is_authenticated():
        username = request.user
	type1 = Customer2.objects.values("commodityid").annotate(average_score=Avg('plc'))
	type2 = Customer2.objects.values("commodityid").annotate(average_score=Avg('nits'))
	type3 = Customer2.objects.values("commodityid").annotate(average_score=Avg('annualvolume'))
	label = [ str(i['commodityid']) for i in type1]
	data1 = [round(i['average_score'],3) for i in type1]
	data2 = [round(i['average_score'],3) for i in type2]
	data3 = [round(i['average_score'],3) for i in type3]
        return render_to_response(template_name,{"username":username,"data1":data1,"data2":data2,"data3":data3,"label":label})
    else:
        return HttpResponseRedirect('/login/')
def profile(request,template_name):
    if  request.user.is_authenticated():
        username = request.user
        return render_to_response(template_name,{"username":username})
    else:
        return HttpResponseRedirect('/login/')
	
