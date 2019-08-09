from django.shortcuts import render, get_object_or_404, redirect
from .models import Building
from django.utils import timezone
from .forms import BuildingPost

# Create your views here.
def complete(request):
    return render(request, 'complete.html')

def place(request):
    buildings = Building.objects
    return render(request, 'place.html',{'buildings':buildings})

def place_detail(request,building_id):
    #공간등록 게시글 상세페이지
    building_detail = get_object_or_404(Building,pk=building_id)
    return render(request, 'place_detail.html',{'building_details':building_detail})

def create(request):
    building=Building(room_img=request.FILES['room_img']) 
    building.address=request.POST['address']
    building.tele_num=request.POST['tele_num']
    building.room_name=request.POST['room_name']
    building.pub_date=timezone.datetime.now()
    building.save()
    return redirect('/register/'+str(building.id))

# def delete(request,building_id):
#     building = Building(id=building_id)
#     building.delete
#     return redirect('home/')
    






