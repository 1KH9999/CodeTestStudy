Money=int(input())
price=list(map(int,input().split()))

def BNP(Money,price):
    stock=0
    for today in price:
        if Money > today:
            stock += Money//today
            Money = Money%today

    revenue=stock*price[13]+Money

    return revenue

def Timing(Money,price):
    stock=0
    for i in range(3,14):
        if price[i]<price[i-1] and price[i-1]<price[i-2] and price[i-2] < price[i-3]:
            if Money >= price[i]:
                stock += Money//price[i]
                Money = Money%price[i]
        elif price[i]>price[i-1] and price[i-1]>price[i-2] and price[i-2] > price[i-3]:
            if stock>0:
                Money+=price[i]*stock
                stock=0

    revenue=stock*price[13] + Money
    return revenue

def winner(Money,price):
    J=BNP(Money,price)
    S=Timing(Money,price)
    if S>J:
        return 'TIMING'
    elif S<J:
        return 'BNP'
    elif S==J:
        return 'SAMESAME'
    
print(winner(Money,price))
    

    

