import requests
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
products=product_data['products']
count=0
for product in products:
 if product['category']=='beauty':
   count=count+1
print('no of products:',count)