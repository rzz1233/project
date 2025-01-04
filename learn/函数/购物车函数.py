goodList = [{'name':'笔记本电脑','price':8000}, {'name':'鼠标', 'price':100}]
cartList = []
collectSet = set()
print("**" * 50)
print("\t\t购物车，有以下操作：\n"
      "\t\t\t1. 加入购物车\n"
      "\t\t\t2. 收藏商品\n"
      "\t\t\t3. 删除购物车商品\n"
      "\t\t\t4. 去结算\n"
      "\t\t\t5. 清空购物车\n"
      "\t\t\t6. 查看购物车\n"
      "\t\t\t7. 添加新商品\n"
      "\t\t\tq. 退出")
print("**" * 50)

def add_cart():
    goods = {}
    name = input("请选择你添加的商品：")
    number = input("请输入你要该添加商品的数量：")
    for good in goodList:
        if name == good['name']:
            if number == "":
                goods['name'] = good['name']
                goods['price'] = good['price']
                goods['number'] = 1
            else:
                goods['name'] = good['name']
                goods['price'] = good['price']
                goods['number'] = int(number)
    if cartList == []:
        cartList.append(goods)
    else:
        for cart in cartList:
            if cart['name'] == goods['name']:
                cart['number'] = cart['number'] + int(number)
                break
        else:
            cartList.append(goods)
def coll_cart():
    name = input("请选择你收藏的商品：")
    for good in goodList:
        if name == good['name']:
            collectSet.add(name)
    print("收藏：", collectSet)
def del_cart():
    if len(cartList) == 0:
        print("购物车为空。")
    else:
        name = input("请选择要删除的商品：")
        for cart in cartList:
            if cart['name'] == name:
                cartList.remove(cart)
def buy():
    sum = 0
    name = input("请输入你要结算的商品：")
    if len(cartList) == 0:
        print("购物车是空的，快去添加吧。")
    else:
        for good in cartList:
            if name == good['name']:
                number = input("请输入你要结算的数量：")
                if number == "":
                    sum += good['price'] * good['number']
                elif int(number) > 0 and int(number) <= int(good['number']):
                    sum += good['price'] * int(number)
                    a = good['number'] - int(number)
                    good['number'] = a
                    print("花费：",sum)
                    if good['number'] == 0:
                        cartList.remove(good)
                elif int(number) > int(good['number']):
                    print("购物车中该商品没有这么多数量")
            elif name == "":
                for good in cartList:
                    price = good["price"]
                    number = good["number"]
                    sum += price * number
                print("花费：",sum)
                cartList.clear()
def clear():
    cartList.clear()
def looklook_cart():
    print("❤"*50)
    if len(cartList) == 0:
        print("您的购物车为空")
    else:
        print("您的购物车：")
        for a in range(len(cartList)):
            print(cartList[a]['name'],"->","$", cartList[a]['price'], "->",cartList[a]['number'],"个")
    print("❤"*50)
def add_good():
    goods = {}
    name = input("请输入要添加的新商品名称：")
    price = int(input("请输入要添加的新商品价格："))
    goods['name'] = name
    goods['price'] = price
    if goods not in goodList:
        goodList.append(goods)
def q():
    print("再见")

while True:
    print("<>"*50)
    print("\t\t商品列表：")
    for i in range(len(goodList)):
        print("\t\t\t", goodList[i]['name'], "：", "$", goodList[i]['price'])
    print("<>" * 50)
    choice = input("选择你要进行的操作：")
#添加
    if choice == '1':
        add_cart()
# 收藏
    if choice == '2':
        coll_cart()
# 删除
    if choice == '3':
        del_cart()
#结算
    if choice == '4':
        buy()

# 清空
    if choice == '5':
        clear()
# 查看
    if choice == '6':
        looklook_cart()
# 添加商品
    if choice == '7':
        add_good()
#退出
    if choice == 'q':
        q()
        break