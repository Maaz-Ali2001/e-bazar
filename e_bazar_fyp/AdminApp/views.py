from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from . import utils
from bson import ObjectId
class Verification:
    def home(self,request):
        if request.method=='POST':
            status_change=request.POST['status']
            print(status_change)
            status_change_lst= status_change.split(',')
            status = status_change_lst[0]
            vendor_id = ObjectId(status_change_lst[1])
            database= utils.connect_database('E-Bazar')
            status_collec = database['status']
            status_id = status_collec.find({'name': status})
            for id in status_id:
                status_id = id['_id']
            data= database["vendor1"]



            update_data = data.update_one({'_id':vendor_id},
                                                     {'$set': {'status': status_id}})
            return redirect('home')
        else:
            database= utils.connect_database('E-Bazar')
            data= database["vendor1"]
            get_data= data.find({})
            unverified={}
            index=0
            for vendor in get_data:
                #print(vendor)
                id_status= vendor["status"]
                status_collec = database["status"]
                #status= status_collec.find({'_id':ObjectId(id_status)})
                all_status= status_collec.find({})
                status_lst = []
                check=False
                for i in all_status:
                    if i['_id']== ObjectId(id_status):
                        if i['name']=='not verified':
                            check=True
                    status_lst.append(i['name'])
                if check==True:
                    unverified[index]=vendor
                    index+=1



        return render(request,"Verification/home.html",{"vendors":unverified,'status':status_lst})

    def verify(self,request):
        if request.method=="POST":
            pass
