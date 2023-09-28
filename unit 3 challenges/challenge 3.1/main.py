def linear_search_product(productList,targetProduct):
    indices=[]
    for index,product in enumerate(productList):
     if  product == targetProduct:
          indices.append(index)

    return indices

product =["Soup","boot","OIL","Soup","loafer","sandal","Soup"]
target = "Soup"

result = linear_search_product(product,target)

print(result)
