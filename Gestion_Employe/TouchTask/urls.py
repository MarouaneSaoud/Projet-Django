from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/projets',views.projet_api),
    path('api/projets/<int:id>',views.projet_api),
    path('api/projets/progress',views.Progress_Projet),

    path('api/equipes',views.equipe_api),
    path('api/equipes/<int:id>',views.equipe_api),
    path('api/equipes_join_chef_service',views.get_equipe_join_chefservice),
    path('api/equipe_detail/<int:id>',views.get_employe_inEquipe),

    path('api/employes',views.employe_api),
    path('api/employes/<int:id>',views.employe_api),
    path('api/employes/by_equipe/<int:id>',views.get_employe_by_equipe),
    path('api/employes/top_employe',views.top_employe_do_tache),
    path('api/Get_employe/<str:name>', views.get_employe),

    path('api/Chef_services', views.chefservice_api),
    path('api/Chef_services/<int:id>', views.chefservice_api),
    path('api/Chef_services_login', obtain_auth_token),

    path('api/taches',views.tache_api),
    path('api/taches/<int:id>',views.tache_api),
    path('api/taches/Etat/fin',views.get_Taches_Etat_fin),
    path('api/taches/Etat/en_attente',views.get_Taches_Etat_En_attente),
    path('api/taches/Etat/en_cours',views.get_Taches_Etat_En_cour),
    path('api/tache/put/en_cours/<int:id>', views.UPDATE_Taches_Etat_En_cour),
    path('api/tache/put/FIN/<int:id>', views.UPDATE_Taches_FIN),
    path('api/tache/projet_employe', views.tache_projet_employe),





]