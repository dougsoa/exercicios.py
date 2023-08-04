import random

extenso = ("zero","um","dois","três","quatro","cinco","seis","sete",
        "oito","nove","dez","onze","doze","treze","catorze","quinze",
        "dezesseis","dezessete","dezoito","dezanove","vinte")

cont = random.randint(1,20)
while True:
    num = cont
    if num >= 0 and num <= 20:
        print(f'O número escolhido randomicamente foi {num}, esse número por extenso é {extenso[num]}')
        break