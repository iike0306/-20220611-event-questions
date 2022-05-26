for num in range(1, 101):
    string = ''

    # ここから記述
    if num%15 == 0: #「15の倍数である」
        string = 'FizzBuzz'

    elif num%3 == 0: #「15の倍数でない」かつ「3の倍数である」
        string = 'Fizz'
        
    elif num%5 == 0: #「15の倍数でない」かつ「5の倍数である」
        string = 'Buzz'
        
    else: #「それ以外」
        string = str(num)
    # ここまで記述

    print(string)
