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
            products=con.find({'Base_product': 'null'})
            for j in products:
                j['id']=j.pop('_id')
                all_products.append(j)
        context={
            'products':all_products
        }
        return render(request,"Homepage/Homepage.html",context)
    # def renProductPage(self,request,product_id):
    #
    #     return render(request, 'product_detail.html',context)


    def productdetail(self,request,product_id):
        database_list = utils.getAllVendors()
        variation = None
        variation_values={}
        for i in database_list:
            con = utils.connect_database(i, 'Products')
            products = con.find({'_id': ObjectId(product_id)})
            for k in products:
                k['id'] = k.pop('_id')
                product=k
            if product['Base_product']=='null':
                if product['Variation'] == True:
                    print('in')

                    variations = con.find({'Base_product': ObjectId(product_id)})
                    for j in variations:
                        j['id'] = j.pop('_id')
                        variation = j
                        for var in product['Variation_type']:
                            variation_values[var]=j[var]


        print(variation)
        context = {'Product_details': product,
                   'Variations': variation,
                   'Caution': 'Note: ' + product["Caution_warning"],
                   'var_values': variation_values,
                   'range': range(1,int(product["Quantity"])+1)}
        print(variation_values)
        return render(request,'Homepage/product_detail.html',context)

    def productVarDetail(self,request,id):
        database_list = utils.getAllVendors()
        variations_list = []
        variation_values={}
        for i in database_list:
            con = utils.connect_database(i, 'Products')
            products = con.find({'_id': ObjectId(id)})
            for k in products:
                k['id'] = k.pop('_id')
                product=k
                variation_values['Color']=k['Color']
                variation_values['Size'] = k['Size']

        print(variation_values)
        context = {'Product_details': product,
                   'Variations': variations_list,
                   'Caution': 'Note: ' + product["Caution_warning"],
                   'var_values': variation_values}
        print(variation_values)
        return render(request,'Homepage/product_detail.html',context)


    def add_to_cart(self,request):

        print(request.POST['addtocart'])
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




