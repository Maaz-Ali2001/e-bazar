from django.shortcuts import render, redirect
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
        print("ïn add products")
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



        context = {'Product_details': product,
                   'Variations': variation,
                   'Caution': 'Note: ' + product["Caution_warning"],
                   'var_values': variation_values,
                   'range': range(1,int(product["Quantity"])+1)}

        return render(request,'Homepage/product_detail.html',context)

    def add_to_cart(self, request):
        print("in add to cart")
        if request.method == 'POST':
            try:
                string_cart = request.COOKIES.get('cart')
                string_cart = string_cart[2:-2]
                string_cart = string_cart.split('],[')
                cart_list = []
                for item in string_cart:
                    item = item.replace("'", "")
                    item = item.split(",")
                    cart_list.append(item)
                print(cart_list)
            except:
                cart_list = []

            if cart_list is None:
                cart_list = []

            flag = False
            productid = request.POST['addtocart']
            for item in cart_list:
                if productid == item[0]:
                    untis = int(item[1])
                    untis += 1
                    item[1] = untis
                    flag = True
            if flag == False:
                cart_list.append([productid, 1])

            context = {'cart_list': cart_list}
            # rend= render(request,'Homepage/cart.html',context)
            rend = redirect('productdetail',product_id=productid)
            rend.set_cookie('cart', cart_list)
            return rend
        else:
            cart_list = []
            string_cart = request.COOKIES.get('cart')
            if string_cart == None:
                cart_list = 'No items in cart'
                return render(request, 'Homepage/cart.html', {'empty': cart_list})
            else:
                string_cart = string_cart[2:-2]
                string_cart = string_cart.split('],[')
                for item in string_cart:
                    item = item.replace("'", "")
                    item = item.split(",")
                    cart_list.append(item)
                cart_contextlist = []
                databaseName = 'vendor23423525252'
                con = utils.connect_database(databaseName, 'Products')
                for product in cart_list:
                    productid = ObjectId(product[0])
                    product_attributes = con.find({'_id': productid})
                    for i in product_attributes:
                        product_attributes = i
                    product_attributes['units'] = product[1]
                    price = int(product_attributes['Price'])
                    sub_total = int(product_attributes['units']) * price
                    product_attributes['subtotal'] = sub_total
                    cart_contextlist.append(product_attributes)
                print(cart_contextlist)

                return render(request, 'Homepage/cart.html', {'Products': cart_contextlist})






