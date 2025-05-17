from datetime import date

date.today()
# 日付を取得
current_day = date.today()
print(current_day)
# 商品コードを入力
item_code = int(input("商品コードを入力してください"))
# 入庫数を入力
item_in = int(input("入庫数を入力してください"))
# 出庫数を入力
item_out = int(input("出庫数を入力してください"))
# 入出庫データーを作成する
item_dic = {current_day: {"item_code": item_code, "nyuko": item_in, "syukko": item_out}}
print(item_dic)
