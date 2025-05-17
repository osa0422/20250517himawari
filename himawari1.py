# 商品データーを定義
item_dic = {
    1: {"item_name": "apple", "stock": 50, "price": 70},
    2: {"item_name": "orange", "stock": 10, "price": 30},
    3: {"item_name": "banana", "stock": 0, "price": 120},
}

# 商品コードの入力
item_code = int(input("商品コードを入力してください"))

# 商品データーに入力された商品コードが存在するか判定
if item_code in item_dic:
    # 入力された商品コードの在庫の値を入力
    stock = int(input("在庫の値を入力して下さい"))
    # 入力された在庫の値で商品データーを更新
    item_dic[item_code]["stock"] = stock
    print(item_dic)
else:
    print("入力された商品コードが存在しません")
