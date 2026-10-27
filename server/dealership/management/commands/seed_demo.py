from django.core.management.base import BaseCommand
from dealership.models import Dealer, DealerReview, CarMake, CarModel
class Command(BaseCommand):
 def handle(self,*args,**kwargs):
  d,_=Dealer.objects.get_or_create(id=1,defaults={"full_name":"Kansas City Auto Center","city":"Wichita","state":"Kansas","address":"100 Main Street","zip":"67202","lat":37.6872,"long":-97.3301,"short_name":"KC Auto","website":"https://example.com","phone":"555-0100"})
  DealerReview.objects.get_or_create(dealer=d,name="Taylor Morgan",defaults={"review":"Helpful staff and a smooth buying experience.","sentiment":"positive"})
  for make, models in [("Toyota",[("Camry",2023),("Corolla",2022)]),("Honda",[("Civic",2024)])]:
   m,_=CarMake.objects.get_or_create(name=make,defaults={"description":"Automotive manufacturer."})
   for name,year in models: CarModel.objects.get_or_create(make=m,name=name,defaults={"year":year,"dealer":d})
  self.stdout.write(self.style.SUCCESS("Demo data created"))
