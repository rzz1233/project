import json
import time
import pickle
def menu():
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
def add_cart(goodList,cartList,name,number):
    goods = {}
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
    if goods != {}:
        if cartList == []:
            cartList.append(goods)
        else:
            for cart in cartList:
                if cart['name'] == goods['name']:
                    cart['number'] = cart['number'] + int(number)
                    break
            else:
                cartList.append(goods)
    else:
        print("没有该商品")
def coll_cart(name,goodList,collectSet):
    for good in goodList:
        if name == good['name']:
            collectSet.add(name)
    print("收藏：", collectSet)
def del_cart(cartList,name):
    if len(cartList) == 0:
        print("购物车为空。")
    else:
        for cart in cartList:
            if cart['name'] == name:
                cartList.remove(cart)
def buy(name,number,cartList):
    sum = 0
    if len(cartList) == 0:
        print("购物车是空的，快去添加吧。")
    else:
        for good in cartList:
            if name == good['name']:
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
    with open("buy.txt","a",encoding="utf-8") as f1:
        a = time.strftime("%Y-%m-%d %H:%M:%S")
        f1.write(f"{a}本次结算的商品是：{name},结算数量是{number},共计{int(sum)}元\n")
def looklook_cart(cartList):
    print("❤"*50)
    if len(cartList) == 0:
        print("您的购物车为空")
    else:
        print("您的购物车：")
        for a in range(len(cartList)):
            print(f"{cartList[a]['name']}：${cartList[a]['price']} 数量：{cartList[a]['number']}个")
    print("❤"*50)
def add_new_good(name, price, goodList):
    goods = {}
    try:
        if price < 0:
            raise ValueError("价格不能是负数")
    except ValueError:
        print("价格不能是负数")
    goods['name'] = name
    goods['price'] = price
    if goods not in goodList:
        goodList.append(goods)
    with open("goodlist.txt", "w",encoding="utf-8") as f:
        # f.write(str(goodList))
        json.dump(goodList,f,ensure_ascii=False)
def main(choice,goodList,cartList,collectSet):
    name = input("请选择商品：")
    if choice == '2':
        coll_cart(name,goodList,collectSet)
    elif choice == '3':
        del_cart(cartList,name)
    elif choice == '7':
        price = int(input("请输入商品价格："))
        add_new_good(name, price, goodList)

    else:
        number = input("请输入商品的数量：")
        if choice == '1':
            add_cart(goodList,cartList,name,number)
        if choice == '4':
            buy(name,number,cartList)
if __name__ == '__main__':
    goodList = [{'name': '笔记本电脑', 'price': 8000}, {'name': '鼠标', 'price': 100}]
    cartList = []
    collectSet = set()
    menu()
    while True:
        print("<>" * 50)
        print("\t\t商品列表：")
        for i in range(len(goodList)):
            print("\t\t\t", goodList[i]['name'], "：", "$", goodList[i]['price'])
        print("<>" * 50)
        choice = input("请输入你的选择：")
        if choice == '5':
            cartList.clear()
        elif choice == '6':
            looklook_cart(cartList)
        elif choice == 'q':
            break
        else:
            main(choice,goodList,cartList,collectSet)