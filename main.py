import random


print("数当てゲームへようこそ!")


while True:
    # 新しいゲームを始めるごとにランダムな数を生成
    num = random.randint(1, 100)
    count = 0

    while True:
        count += 1
        user_num = int(input("あなたの予想は?:"))

        if user_num == num:
            print(f"おめでとうございます!正解です!{count}回目の予想で当てました!")
            break
        elif user_num < num:
            print("もっと大きい数字です!")
        else:
            print("もっと小さい数字です!")

    # ユーザーにもう一回プレイするかを尋ねる
    user_select = input("もう一回プレイしますか?(yes/no): ").lower()
    if user_select == "yes":
        continue
    elif user_select == "no":
        print("ゲームを終了します。また遊んでくださいね!")
        break
    else:
        print("無効な入力です。ゲームを終了します。")
        break
