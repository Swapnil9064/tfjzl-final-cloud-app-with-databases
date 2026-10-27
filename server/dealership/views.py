from django.http import JsonResponse
from .models import Dealer, CarMake
def dealer_dict(d):
 return {"id":d.id,"full_name":d.full_name,"city":d.city,"state":d.state,"address":d.address,"zip":d.zip,"lat":d.lat,"long":d.long,"short_name":d.short_name,"website":d.website,"phone":d.phone}
def all_dealers(request):
 return JsonResponse([dealer_dict(d) for d in Dealer.objects.all().order_by("id")], safe=False)
def dealer_by_id(request, dealer_id):
 try: d=Dealer.objects.get(pk=dealer_id)
 except Dealer.DoesNotExist: return JsonResponse({"error":"Dealer not found"},status=404)
 return JsonResponse(dealer_dict(d))
def dealers_by_state(request, state):
 return JsonResponse([dealer_dict(d) for d in Dealer.objects.filter(state__iexact=state)],safe=False)
def dealer_reviews(request, dealer_id):
 try: d=Dealer.objects.get(pk=dealer_id)
 except Dealer.DoesNotExist: return JsonResponse({"error":"Dealer not found"},status=404)
 return JsonResponse([{"id":r.id,"name":r.name,"review":r.review,"sentiment":r.sentiment} for r in d.reviews.all()],safe=False)
def car_makes(request):
 return JsonResponse([{"id":m.id,"name":m.name,"description":m.description,"models":[{"id":x.id,"name":x.name,"year":x.year} for x in m.models.all()]} for m in CarMake.objects.prefetch_related("models")],safe=False)
