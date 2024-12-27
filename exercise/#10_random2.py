import random
cards = [str(i) for i in range(2,11)]
cards.extend(list("JQKA"))
#print(cards)

allCards = []
for s in "♣♦♥♠":
    for c in cards:
        allCards.append(s+c)
random.shuffle(allCards)
print("Cards:",allCards)
for i in range(4):
    onPlayer = allCards[i::4]
    onPlayer.sort()
    print("player", i, onPlayer)
