from django.shortcuts import render,redirect
from . import utils
from bson.objectid import ObjectId
from django.http import HttpResponse
from bson.objectid import ObjectId
from datetime import datetime
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

    def string_nested_list_to_list(self,string_cart):
        string_cart = string_cart[2:-2]
        string_cart = string_cart.split('],[')
        cart_list = []
        for item in string_cart:
            item = item.replace("'", "")
            item = item.split(",")
            cart_list.append(item)
        return cart_list

    def add_to_cart(self,request):
        if request.method=='POST':
            string_cart = request.COOKIES.get('cart')
            if string_cart==None:
                cart_list=[]
            else:
                cart_list= self.string_nested_list_to_list(string_cart)

            flag=False
            productid = request.POST['addtocart']
            for item in cart_list:
                if productid == item[0]:
                    untis= int(item[1])
                    untis+=1
                    item[1]= untis
                    flag=True
            if flag==False:
                cart_list.append([productid,1])

            rend= redirect('productdetail')
            rend.set_cookie('cart',cart_list,max_age=120)
            return rend
        else:
            string_cart = request.COOKIES.get('cart')
            if string_cart==None:
                cart_list='No items in cart'
                return render(request, 'Homepage/cart.html', {'empty':cart_list})
            else:
                cart_list= self.string_nested_list_to_list(string_cart)
                cart_contextlist=[]
                databaseName = 'vendor23423525252'
                con = utils.connect_database(databaseName, 'Products')
                total_amount= 0
                for product in cart_list:
                    productid= ObjectId(product[0])
                    product_attributes = con.find({'_id': productid})
                    for i in product_attributes:
                        product_attributes=i
                    product_attributes['units']=product[1]
                    price= int(product_attributes['Price'])
                    sub_total= int(product_attributes['units'])*price
                    total_amount+=sub_total
                    product_attributes['subtotal']=sub_total
                    cart_contextlist.append(product_attributes)

                return render(request,'Homepage/cart.html',{'Products':cart_contextlist,'total_amount':total_amount })

    def register(self,request):
        if request.method == 'POST':
            full_name = request.POST['full_name']
            email = request.POST['email']
            password = request.POST['password']
            address = request.POST['address']
            phone = request.POST['phone']


            customer_database= utils.connect_database("E-Bazar","Customer")
            customers_find= customer_database.find({"email":email})


            if customers_find.count()==0:
                customer_detail={'name':full_name,'email':email,'password':password,'phone':phone,'address':address}
                customer_id= customer_database.insert_one(customer_detail)
                customer_id= customer_id.inserted_id
                rend= redirect('cart')
                rend.set_cookie('customer_id', customer_id, max_age=120)
                return rend
            else:
                return render(request, 'register/register.html', {
                    'error_message': "Email is already taken, use different email !",
                })

        return render(request, 'register/register.html')

    def order(self,request):
        customer_id=request.COOKIES.get('customer_id')
        print(customer_id)
        if customer_id is None:
            return render(request,'register/register.html')
        else:

            customer_id= customer_id
            order_database= utils.connect_database("E-Bazar","Orders")

            string_cart = request.COOKIES.get('cart')
            if string_cart==None:
                cart_list='No items in cart'
                return render(request, 'Homepage/cart.html', {'empty':cart_list})
            else:
                cart_list= self.string_nested_list_to_list(string_cart)
                cart_contextlist=[]
                order_dict={}
                order_dict['Products']=[]
                databaseName = 'vendor23423525252'
                con = utils.connect_database(databaseName, 'Products')
                total_amount= 0
                for product in cart_list:
                    productid= ObjectId(product[0])
                    product_attributes = con.find({'_id': productid})
                    for i in product_attributes:
                        product_attributes=i
                    units= int(product[1])
                    product_attributes['units']=units
                    price= int(product_attributes['Price'])
                    sub_total= int(product_attributes['units'])*price
                    total_amount+=sub_total
                    productid = str(productid)
                    order_dict['Products'].append({productid:units,'subtotal':sub_total})

                now = datetime.now()
                order_dict['total']= total_amount
                order_dict['customer_id']=customer_id
                order_dict['cluster_id']=None
                order_dict['date']= now

                order_database.insert_one(order_dict)

                return render(request,'Homepage/Homepage.html')

# Create your views here.



