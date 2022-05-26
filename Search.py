def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    ok, ng = -1, len(sorted_array) #target_numberはsorted_array[ok]以上sorted_array[ng]未満とする
    def is_ok(i):
        return sorted_array[i] <= target_number
    while abs(ok-ng) > 1: #okとngの差が1となるまで二分探索
        mid = (ok+ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    if sorted_array[ok] == target_number: #解の候補okが解であるか確認
        return ok
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
