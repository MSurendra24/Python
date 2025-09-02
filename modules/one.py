import requests
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
print(type(product_data))
products=product_data['products']
for product in products:
    print(product['title'],product['price'])
    
    