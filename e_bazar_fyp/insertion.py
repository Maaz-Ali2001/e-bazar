from pymongo import MongoClient
connection_string="mongodb+srv://fypecommerce:maazali786@cluster0.ycmix0k.mongodb.net/test"
client=MongoClient(connection_string)
database=client["E-Bazar"]
dbconnection=database["Categories"]
categories_list=[
    {
        'name':'Groceries & Pets',
        'parent':'/',
        'category':'/Groceries & Pets'
    },
    {
        'name': 'Health & Beauty',
        'parent': '/',
        'category': '/Health & Beauty'
    },
    {
        'name': "Men's Fashion",
        'parent': '/',
        'category': "/Men's Fashion"
    },
    {
        'name': "Women's Fashion",
        'parent': '/',
        'category': "/Women's Fashion"
    },
    {
        'name': 'Mother & Baby',
        'parent': '/',
        'category': '/Mother & Baby'
    },
    {
        'name': 'Home & Lifestyle',
        'parent': '/',
        'category': '/Home & Lifestyle'
    },
    {
        'name': 'Electronic Accessories',
        'parent': '/',
        'category': '/Electronic Accessories'
    },
    {
        'name': 'TV & Hone Appliances',
        'parent': '/',
        'category': '/TV & Hone Appliances'
    },
    {
        'name': 'Sports & Outdoors',
        'parent': '/',
        'category': '/Sports & Outdoors'
    },
    {
        'name': 'Watches, Bags & Jewellery',
        'parent': '/',
        'category': '/Watches, Bags & Jewellery'
    },
    {
        'name': 'Automotive & Motorbikes',
        'parent': '/',
        'category': '/Automotive & Motorbikes'
    },
    {
        'name': 'Beverages',
        'parent': '/Groceries & Pets',
        'category': '/Groceries & Pets/Beverages'
    },
    {
        'name': 'Coffee',
        'parent': '/Groceries & Pets/Beverages',
        'category': '/Groceries & Pets/Beverages/coffee'
    },
    {
        'name': 'Fragrances',
        'parent': '/Health & Beauty',
        'category': '/Health & Beauty/Fragrances'
    },
    {
        'name': 'Men Fragrances',
        'parent': '/Health & Beauty',
        'category': '/Health & Beauty/Men Fragrances'
    },
    {
        'name': 'Shoes',
        'parent': "Men's Fashion",
        'category': "/Men's Fashion/Sneakers"
    },
    {
        'name': 'Muslim Wear',
        'parent': "/Women's Fashion",
        'category': "/Women's Fashion/Muslim Wear"
    },
    {
        'name': 'Scarves',
        'parent': "/Women's Fashion/Muslim Wear",
        'category': "/Women's Fashion/Muslim Wear/Scarves"
    },





]
dict=[
{'name': 'electronics', 'parent': '/', 'category': '/electronics'},
{'name': 'embedded', 'parent': '/electronics', 'category': '/electronics/embedded'},
{ 'name': 'Electronics', 'parent': '/', 'category': '/Electronics'},
{'name': 'Audio', 'parent': '/Electronics', 'category': '/Electronics/Audio'},
{ 'name': 'Arcade Equipment', 'parent': '/Electronics', 'category': '/Electronics/Arcade Equipment'},
{ 'name': 'Circuit Boards & Components', 'parent': '/Electronics', 'category': '/Electronics/Circuit Boards & Components'},
{ 'name': 'Communications', 'parent': '/Electronics', 'category': '/Electronics/Communications'},
{ 'name': 'Computers', 'parent': '/Electronics', 'category': '/Electronics/Computers'},
{ 'name': 'Electronics Accessories', 'parent': '/Electronics', 'category': '/Electronics/Electronics Accessories'},
{ 'name': 'Audio & Video Receiver Accessories', 'parent': '/Electronics/Audio', 'category': '/Electronics/Audio/Audio & Video Receiver Accessories'},
{ 'name': 'Headphone & Headset Accessories', 'parent': '/Electronics/Audio', 'category': '/Electronics/Audio/Headphone & Headset Accessories'},
{ 'name': 'Microphone Stands', 'parent': '/Electronics/Audio', 'category': '/Electronics/Audio/Microphone Stands'},
{ 'name': 'Basketball Arcade Games', 'parent': '/Electronics/Arcade Equipment', 'category': '/Electronics/Arcade Equipment/Basketball Arcade Games'},
{ 'name': 'Pinball Machines', 'parent': '/Electronics/Arcade Equipment', 'category': '/Electronics/Arcade Equipment/Pinball Machines'},
{ 'name': 'Video Game Arcade Cabinets', 'parent': '/Electronics/Arcade Equipment', 'category': '/Electronics/Arcade Equipment/Video Game Arcade Cabinets'},
{ 'name': 'Arcade Equipment', 'parent': '/Electronics/Circuit Boards & Components', 'category': '/Electronics/Circuit Boards & Components/'},
{ 'name': 'Capacitors', 'parent': '/Electronics', 'category': '/Electronics/Arcade Equipment/Capacitors'},
{ 'name': 'Electronic Oscillators', 'parent': '/Electronics/Circuit Boards & Components', 'category': '/Electronics/Circuit Boards & Components/Electronic Oscillators'},
{ 'name': 'Resistors', 'parent': '/Electronics/Circuit Boards & Components', 'category': '/Electronics/Circuit Boards & Components/Resistors'},
{'name': 'Satellite Phones', 'parent': '/Electronics/Communications', 'category': '/Electronics/Communications/Satellite Phones'},
{'name': 'Computer Servers', 'parent': '/Electronics/Computers', 'category': '/Electronics/Computers/Computer Servers'},
{'name': 'Desktop Computers', 'parent': '/Electronics/Computers', 'category': '/Electronics/Computers/Desktop Computers'},
{'name': 'Laptops', 'parent': '/Electronics/Computers', 'category': '/Electronics/Computers/Laptops'},
]
dbconnection.insert_many(categories_list)
