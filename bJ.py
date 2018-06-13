import random

koloda = [2,3,4,5,6,7,8,9,10,2,3,4,11] * 4
sirCount = 0
croupierCount = 0
sir = True
croupier = False

print("\n$$$ blackJacl в хате $$$\n")
random.shuffle(koloda)
print("*Крупье тусует колоду*\n")
print("- У Вас, 0 очков сударь, Ваш ход\n")

while sir:
    choise = input("Изволите еще карту ?(y/n)\n")
    if choise == 'y':
        current = koloda.pop()
        print("Ваша карта достоинством в %d\n" %current)
        sirCount += current
        if sirCount > 21:
            print('Сударь, вы попали на очко, очки и тапочки...\n')
            sir = False
            croupier = False
        if sirCount < 21:
            print('Вы набрали %d очков\n' %sirCount)
        if sirCount == 21:
            print('21 ! Вы в почете у Братвы\n')
            sir = False
            croupier = True
    if choise == 'n':
        print('Вы набрали %d очков' %sirCount)
        sir = False
        croupier = True

print ("*Крупье играет*\n")

while croupier:
    croupierCurrent = koloda.pop()
    croupierCount += croupierCurrent

    if croupierCount > 21:
        print('Крупье набрал %d очков и попал на очко, очки и тапочки...\n' %croupierCount)
        croupier = False
    if croupierCount < 21:
        if croupierCount < sirCount:
            print('Крупье набрал %d очков\n' %croupierCount)
        else:
            print('Крупье набрал %d очков. У Вас мыло упало, сударь...\n' %croupierCount)
            croupier = False
    if croupierCount == 21:
        print('Крупье набрал 21 очко. У Вас мыло упало, сударь...\n')
        croupier = False




