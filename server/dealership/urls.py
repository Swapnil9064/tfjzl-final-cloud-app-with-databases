from django.urls import path
from . import views
urlpatterns = [
 path("dealers/", views.all_dealers),
 path("dealers/<int:dealer_id>/", views.dealer_by_id),
 path("dealers/state/<str:state>/", views.dealers_by_state),
 path("dealers/<int:dealer_id>/reviews/", views.dealer_reviews),
 path("carmakes/", views.car_makes),
]
