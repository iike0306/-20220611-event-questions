def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    fig = True
    latter = 0 #基準値未満の値のindex
    while fig:
        for i in range(len(array)): #先頭からの基準値以上の値の探索
            if array[i] >= pivot:
                former = i #基準値以上の値のindex
                break
        for i in reversed(range(len(array))): #末端からの基準値未満の値の探索
            if array[i] < pivot:
                latter = i
                break
        if former < latter: #先頭からの探索と、末端からの探索がぶつからない
            array[former], array[latter] = array[latter], array[former] #値の交換
        else: #先頭からの探索と、末端からの探索がぶつかる
            fig = False #探索を終了
        
    for i in range(len(array)): #二つのグループに分ける
        if array[i] >= pivot:
            div = i #二つのグループの境のindex
            break
    if div == 0: #基準値が先頭にいる（基準値が最小値）の場合は、基準値とそれ以外のグループに分ける
        array_small = [array[0]] 
        array_large = array[1:]
    else: ##基準値以上のグループ、基準値未満のグループに分ける
        array_small = array[:div]
        array_large = array[div:]    
        
    return sort(array_small)+sort(array_large) #同様の処理を再帰的に繰り返し

    # ここまで記述

if __name__ == '__main__':
    main()
