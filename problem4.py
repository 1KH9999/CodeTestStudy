A,B=map(int,input().split())
def cardrank(A,B):
  if A!=B:
    ggeut=(A+B)%10
    return (0,ggeut)
  else: 
    ddaeng=A
    return (1,ddaeng)

def win_probability(myA,myB):
  count=0
  cards = [i for i in range(1, 11)] * 2 
  cards.remove(myA)
  cards.remove(myB)
  myrank=cardrank(myA,myB)
  for i in range(len(cards)):
      for j in range(i + 1, len(cards)):  
          enemyA = cards[i]
          enemyB = cards[j]
          enemyrank = cardrank(enemyA, enemyB)
          if myrank>enemyrank:
            count+=1
  probability = count / 153  
  return round(probability, 3)

doi_win=win_probability(A,B)
print(f"{doi_win:.4f}")
      
#18c2 로 153 가지로 조합이 가능함