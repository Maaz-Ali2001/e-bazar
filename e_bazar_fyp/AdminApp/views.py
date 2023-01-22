from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from . import utils
from bson import ObjectId
class Verification:
    def home(self,request):
        if request.method=='POST':
            status= request.POST['status']
            return render(request,'Verification/status_change.html',context={'status_home':status})
        else:
            database = utils.connect_database('E-Bazar')
            status_collec = database['status']
            status_items= status_collec.find({})
            status_lst = []
            for status in status_items:
                status_lst.append(status['name'])

            return render(request, 'Verification/home.html', context={'status_home': status_lst})

    def status_change(self,request,status_type):
        if request.method=='POST':
            status_change=request.POST['status']
            status_change_lst= status_change.split(',')
            status = status_change_lst[0]
            vendor_id = ObjectId(status_change_lst[1])
            database= utils.connect_database('E-Bazar')
            status_collec = database['status']
            status_id = status_collec.find({'name': status})
            for id in status_id:
                status_id = id['_id']
            data= database["Vendors"]
            data.update_one({'_id':vendor_id},{'$set': {'status': status_id}})
            return redirect('status_change',status_type= status_type)
        else:
            database= utils.connect_database('E-Bazar')
            main_vendor= database['Vendors']
            vendorsdict_statustype={}
            database_names= utils.get_database_names()
            sep_vendors=[] # seperate databses vendors list
            # start seperate databses vendors list
            for dat_nam in database_names:
                check= dat_nam[:6]
                if check=='vendor':
                    sep_vendors.append(dat_nam)
            # End seperate databses vendors list
            get_data= main_vendor.find({})
            index=0
            for vendor in get_data:
                status_collec = database["status"]
                all_status= status_collec.find({})
                status_lst = []
                check=False
                for i in all_status:
                    if i['_id']== ObjectId(vendor['status']):
                        if i['name']==status_type:
                            check=True
                    else:
                        status_lst.append(i['name'])
                if check==True:
                    vendor_database= vendor['database_name']
                    vendordb_sep= utils.connect_database(vendor_database)
                    vendorinfo_sep= vendordb_sep['Information']
                    vendorinfo_sep= vendorinfo_sep.find({})
                    for atts in vendorinfo_sep:
                        vendorinfo_sep_dict= atts
                    vendorinfo_sep_dict['_id']= vendor['_id']
                    vendorinfo_sep_dict['email']= vendor['email']
                    vendorinfo_sep_dict['phone']= vendor['phone']
                    vendorsdict_statustype[index]= vendorinfo_sep_dict
                    index+=1
            return render(request,"Verification/status_change.html",{"vendors":vendorsdict_statustype,'status_lst':status_lst,'status_type':status_type})

    def verify(self,request):
        if request.method=="POST":
            pass
