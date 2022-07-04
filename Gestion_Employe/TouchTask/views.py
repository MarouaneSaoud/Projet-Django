from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response  import JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import decorators
from rest_framework.decorators import api_view
from django.db import connections
import json
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
### projet##
@csrf_exempt
def projet_api(request , id=0):
    if request.method == 'GET':
        projets = Projet.objects.all()
        projetserilizer = Projetserilizer(projets, many=True)
        return JsonResponse(projetserilizer.data )

    elif request.method == "POST":
        projet_data = JSONParser().parse(request)
        projets_serializer = Projetserilizer(data = projet_data)
        if projets_serializer.is_valid():
            projets_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "PUT":
        projet_data = JSONParser().parse(request)
        projet=Projet.objects.get(id_projet=projet_data['id_projet'])
        projet_serializer =Projetserilizer(projet,data=projet_data)
        if projet_serializer.is_valid():
            projet_serializer.save()
            return JsonResponse("update Succesfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        projet =Projet.objects.get(id_projet=id)
        projet.delete()
        return JsonResponse('deleted' , safe=False)



### equipe ##
@csrf_exempt
def equipe_api(request , id=0):
    if request.method == 'GET':
        equipes = Equipe.objects.all()
        equipeserilizer =Equipeserilizer(equipes, many=True)
        return JsonResponse(equipeserilizer.data )

    elif request.method == "POST":
        equipe_data = JSONParser().parse(request)
        equipes_serializer = Equipeserilizer(data = equipe_data)
        if equipes_serializer.is_valid():
            equipes_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "PUT":
        equipe_data = JSONParser().parse(request)
        equipe=Equipe.objects.get(id_Equipe=equipe_data['id_Equipe'])
        equipe_serializer =Equipeserilizer(equipe,data=equipe_data)
        if equipe_serializer.is_valid():
            equipe_serializer.save()
            return JsonResponse("update Succesfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        equipe =Equipe.objects.get(id_Equipe=id)
        equipe.delete()
        return JsonResponse('deleted' , safe=False)


### chefservice ##
@csrf_exempt
def chefservice_api(request , id=0):
    if request.method == 'GET':
        chef_services = Chef_Service.objects.all()
        chefserviceserilizer =Chef_Serviceserilizer(chef_services, many=True)
        return JsonResponse(chefserviceserilizer.data )
    elif request.method == "POST":
        chefservice_data = JSONParser().parse(request)
        chefservice_serializer = Chef_Serviceserilizer(data=chefservice_data)
        if chefservice_serializer.is_valid():
            chefservice_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "PUT":
        chef_services_data = JSONParser().parse(request)
        chef_service = Chef_Service.objects.get(Matricule=chef_services_data['Matricule'])
        chef_service_serializer = Chef_Serviceserilizer(chef_service, data=chef_services_data)
        if chef_service_serializer.is_valid():
            chef_service_serializer.save()
            return JsonResponse("update Succesfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        chef_service = Chef_Service.objects.get(Matricule=id)
        chef_service.delete()
        return JsonResponse('deleted', safe=False)

### employe ##
@csrf_exempt
def employe_api(request , id=0):
    if request.method == 'GET':
        employes = Employe.objects.all()
        employesserilizer = Employeserilizer(employes, many=True)
        return JsonResponse(employesserilizer.data)
    elif request.method == "POST":
        employe_data = JSONParser().parse(request)
        employeserilizer = Employeserilizer(data=employe_data)
        if employeserilizer.is_valid():
            employeserilizer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "PUT":
        employe_data = JSONParser().parse(request)
        employe = Employe.objects.get(Matricule=employe_data['Matricule'])
        employe_serializer = Employeserilizer(employe, data=employe_data)
        if employe_serializer.is_valid():
            employe_serializer.save()
            return JsonResponse("update Succesfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        employe = Employe.objects.get(Matricule=id)
        employe.delete()
        return JsonResponse('deleted', safe=False)


### tache ##
@csrf_exempt
def tache_api(request , id=0):
    if request.method == 'GET':
        tache = Tache.objects.all()
        tacheserilizer =Tacheserilizer(tache, many=True)
        return JsonResponse(tacheserilizer.data)
    elif request.method == "POST":
        tache_data = JSONParser().parse(request)
        tacheserilizer = Tacheserilizer(data=tache_data)
        if tacheserilizer.is_valid():
            tacheserilizer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "PUT":
        tache_data = JSONParser().parse(request)
        tache = Tache.objects.get(id_tache=tache_data['id_tache'])
        tache_serializer = Tacheserilizer(tache, data=tache_data)
        if tache_serializer.is_valid():
            tache_serializer.save()
            return JsonResponse("update Succesfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        tache = Tache.objects.get(id_tache=id)
        tache.delete()
        return JsonResponse('deleted', safe=False)


@csrf_exempt
def top_employe_do_tache (request):
    if request.method == 'GET':
        cursor = connections['default'].cursor()
        cursor.execute("SELECT COUNT(e.Matricule) as cpt , MAX(t.id_tache) as max , e.Nom , e.Prenom from touchtask_employe e , touchtask_tache t where e.Matricule=t.Employe_id and t.Etat='fin' GROUP BY e.Matricule ORDER BY cpt DESC LIMIT 1 ")
        objs = cursor.fetchall()
        json_data = []
        for obj in objs :
            json_data.append({ "count": obj[0] ,"Matricule": obj[1],"NOM": obj[2],"Prenom": obj[3]})
        return JsonResponse(json_data, safe=False)

@csrf_exempt
def get_employe(request ,name):
    if request.method == 'GET':
        cursor = connections['default'].cursor()
        cursor.execute("Select * from touchtask_employe where Nom='%s'"%name)
        objs = cursor.fetchall()
        json_data = []
        for obj in objs:
            json_data.append({"Matricule": obj[0], "nom": obj[1], "Prenom": obj[2]})
        return JsonResponse(json_data, safe=False)
@csrf_exempt
def get_Taches_Etat_fin(request ):
    if request.method == 'GET':
        cursor = connections['default'].cursor()
        cursor.execute("SELECT touchtask_tache.* , touchtask_projet.NomProjet , touchtask_employe.Nom , touchtask_employe.Prenom FROM touchtask_tache , touchtask_employe , touchtask_projet where touchtask_tache.Employe_id=touchtask_employe.Matricule and touchtask_tache.Projet_id=touchtask_projet.id_projet and touchtask_tache.Etat='fin' ORDER by touchtask_tache.Projet_id")
        objs = cursor.fetchall()
        json_data = []
        for obj in objs:
            json_data.append({"id_tache ": obj[0], "nom_tache": obj[1], "description": obj[2] , "date_lancement ": obj[3],"Etat ": obj[4],"employe_id ": obj[5],"Projet_id ": obj[6],"Nom_projet ": obj[7],"Nom_employe ": obj[8],"Prenom_employe ": obj[9]})
        return JsonResponse(json_data, safe=False)
@csrf_exempt
def get_Taches_Etat_En_attente(request):
    if request.method == 'GET':
        cursor = connections['default'].cursor()
        cursor.execute("SELECT touchtask_tache.* , touchtask_projet.NomProjet , touchtask_employe.Nom , touchtask_employe.Prenom FROM touchtask_tache , touchtask_employe , touchtask_projet where touchtask_tache.Employe_id=touchtask_employe.Matricule and touchtask_tache.Projet_id=touchtask_projet.id_projet and touchtask_tache.Etat='En attente' ORDER by touchtask_tache.Projet_id")
        objs = cursor.fetchall()
        json_data = []
        for obj in objs:
            json_data.append({"id_tache": obj[0], "nom_tache": obj[1], "description": obj[2] , "date_lancement": obj[3],"Etat": obj[4],"employe_id": obj[5],"Projet_id": obj[6],"Nom_projet": obj[7],"Nom_employe": obj[8],"Prenom_employe": obj[9]})
        return JsonResponse(json_data, safe=False)

@csrf_exempt
def get_Taches_Etat_En_cour(request):
    if request.method == 'GET':
        cursor = connections['default'].cursor()
        cursor.execute("SELECT touchtask_tache.* , touchtask_projet.NomProjet , touchtask_employe.Nom , touchtask_employe.Prenom FROM touchtask_tache , touchtask_employe , touchtask_projet where touchtask_tache.Employe_id=touchtask_employe.Matricule and touchtask_tache.Projet_id=touchtask_projet.id_projet and touchtask_tache.Etat='en cours' ORDER by touchtask_tache.Projet_id")
        objs = cursor.fetchall()
        json_data = []
        for obj in objs:
            json_data.append({"id_tache": obj[0], "nom_tache": obj[1], "description": obj[2] , "date_lancement": obj[3],"Etat": obj[4],"employe_id": obj[5],"Projet_id": obj[6],"Nom_projet": obj[7],"Nom_employe": obj[8],"Prenom_employe": obj[9]})
        return JsonResponse(json_data, safe=False)
@csrf_exempt
def UPDATE_Taches_Etat_En_cour(request , id):
    if request.method == 'PUT':
        cursor = connections['default'].cursor()
        cursor.execute("update touchtask_tache set Etat='EN COURS' where id_tache=%s"%id)
        return JsonResponse("update Succesfully", safe=False)
@csrf_exempt
def UPDATE_Taches_FIN(request , id):
    if request.method == 'PUT':
        cursor = connections['default'].cursor()
        cursor.execute("update touchtask_tache set Etat='FIN' where id_tache=%s"%id)
        return JsonResponse("update Succesfully", safe=False)
@csrf_exempt
def get_equipe_join_chefservice(request):
    if request.method == 'GET':
        cursor = connections['default'].cursor()
        cursor.execute("SELECT touchtask_equipe.* , touchtask_chef_service.Nom , touchtask_chef_service.Prenom  from touchtask_equipe , touchtask_chef_service  where touchtask_chef_service.Matricule =touchtask_equipe.chef_service_id ")
        objs = cursor.fetchall()
        json_data = []
        for obj in objs:
            json_data.append({"id_Equipe": obj[0], "Nom_Equipe": obj[1], "date_creation": obj[2] , "chef_Service_id": obj[3],"Nom": obj[4],"Prenom": obj[5]})
        return JsonResponse(json_data, safe=False)
@csrf_exempt
def Progress_Projet(request):
    if request.method == 'GET':
        cursor = connections['default'].cursor()
        cursor.execute("SELECT COUNT(*) as count_fin , p.id_projet as idp, p.NomProjet , @x:= (SELECT COUNT(*)  from touchtask_tache t , touchtask_projet  p where t.Projet_id =p.id_projet and p.id_projet=idp  ) as count_total FROM touchtask_tache t , touchtask_projet p WHERE t.Projet_id=p.id_projet AND Etat='FIN' GROUP by p.NomProjet")
        objs = cursor.fetchall()
        json_data = []
        for obj in objs:
            json_data.append({"count_fin": obj[0], "id_projet": obj[1], "NomProjet": obj[2],"count_Total":obj[3] })
        return JsonResponse(json_data, safe=False)
@csrf_exempt
def tache_projet_employe(request):
    if request.method == 'GET':
        cursor = connections['default'].cursor()
        cursor.execute("SELECT t.* , p.NomProjet , e.Nom , e.Prenom FROM touchtask_tache t , touchtask_projet p , touchtask_employe e where t.Employe_id = e.Matricule and t.Projet_id=p.id_projet ORDER by p.date_creation DESC")
        objs = cursor.fetchall()
        json_data = []
        for obj in objs:
            json_data.append({"id_tache": obj[0], "Nom_tache": obj[1], "Description": obj[2],"date_Lancement":obj[3],"Etat":obj[4],"Employe_id":obj[5] ,"Projet_id":obj[6],"Nom_Projet":obj[7],"Nom":obj[8],"prenom":obj[9] })
        return JsonResponse(json_data, safe=False)
@csrf_exempt
def get_employe_inEquipe(request,id):
    if request.method == 'GET':
        cursor = connections['default'].cursor()
        cursor.execute("SELECT e.* , eq.Nom_Equipe FROM touchtask_employe e , touchtask_equipe eq WHERE e.Equipe_id=eq.id_Equipe and  Equipe_id=%s"%id)
        objs = cursor.fetchall()
        json_data = []
        for obj in objs:
            json_data.append({"Matricule":obj[0] , "Nom":obj[1] , "Prenom":obj[2], "Date_Recructement":obj[3], "Salaire":obj[4] , "Nom_equipe":obj[8] })
        return JsonResponse(json_data, safe=False)
@csrf_exempt
def get_employe_by_equipe(request,id):
    if request.method == 'GET':
        cursor = connections['default'].cursor()
        cursor.execute("select e.Matricule , e.Nom , e.Prenom , e.Equipe_id from touchtask_employe e , touchtask_projet p , touchtask_equipe eq WHERE e.Equipe_id=p.Equipe_id and p.Equipe_id=eq.id_Equipe and p.id_projet=%s"%id)
        objs = cursor.fetchall()
        json_data = []
        for obj in objs:
            json_data.append({"Matricule":obj[0] , "Nom":obj[1],"Prenom":obj[2],"equipe":obj[3] })
        return JsonResponse(json_data, safe=False)

