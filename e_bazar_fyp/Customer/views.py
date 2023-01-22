from django.shortcuts import render
from . import utils
from bson.objectid import ObjectId
from django.http import HttpResponse
from bson.objectid import ObjectId
class Customer:
    def __init__(self):
        pass

    def renHomePage(self,request):
        database_list=utils.getAllVendors()
        all_products=[]
        for i in database_list:
            con=utils.connect_database(i,'Products')
            products=con.find({'Base product': 'null'})
            for j in products:
                all_products.append(j)
        context={
            'products':all_products
        }
        return render(request,"Homepage/Homepage.html",context)


    def productdetail(self,request):
        databaseName= 'vendor23423525252'
        productid= ObjectId('63c9407c1307b571b56c8ed1')
        con= utils.connect_database(databaseName,'Products')
        product= con.find({'_id':productid})
        for i in product:
            product=i

        del product['_id']
        product['id']= productid

        return render(request,'Homepage/product_detail.html',product)

    def add_to_cart(self,request):
        if request.method=='POST':
            try:
                cart_list=request.COOKIES.get('cart')
                print('iam',cart_list)
            except:
                cart_list=[]

            if cart_list is None:
                cart_list=[]

            productid = request.POST['addtocart']
            cart_list.append(productid)
            context= {'cart_list':cart_list}
            rend= render(request,'Homepage/cart.html',context)
            rend.set_cookie('cart',cart_list)
            return rend
        else:
            try:
                value = request.COOKIES.get('cart')
                print('1')
            except:
                value = request.COOKIES['cart']
            if value== None:
                value='No items in cart'
            return HttpResponse(value)




        return HttpResponse(productid)
        return render(request,'cart.html')

# Create your views here.


