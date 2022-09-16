import time
import random
rodada = 0
placar_humano = 0
placar_pc = 0
while rodada < 3:    
    print("=-"*15)
    print("TEST YOUR LUCK ON JOQUENPÔ")
    print("=-"*15)
    jogada = int(input("""Your play options:
    [1] STONE
    [2] PAPER
    [3] SCISSORS
    your move: """))
    cmp = random.randint(1, 3)

    if jogada <1 or jogada >3:
        print("Invalid move")
        break

    if cmp == 1:
        cmp = "STONE"
    elif cmp == 2:
        cmp = "PAPER"
    elif cmp == 3:
        cmp = "SCISSORS"

    if jogada == 1:
        jogada = "STONE"
    elif jogada == 2:
        jogada = "PAPER"
    elif jogada == 3:
        jogada = "SCISSORS"

    print("JO")
    time.sleep(1)
    print("QUEN")
    time.sleep(1)
    print("PÔ")
    time.sleep(1)


    print("You played {} and the computer played {}".format(jogada, cmp))


    if jogada == "STONE" and cmp == "STONE":          #PEDRA
        print("DRAW")
        rodada += 1

    elif jogada == "STONE" and cmp == "PAPER":        #PEDRA
        print("You lost")
        placar_pc +=  1
        rodada += 1

    elif jogada == "STONE" and cmp == "SCISSORS":      #PEDRA
        print("You win")
        placar_humano += 1
        rodada += 1

    #    
    elif jogada == "PAPER" and cmp == "PAPER":        #PAPEL
        print("DRAW")
        rodada += 1

    elif jogada == "PAPER" and cmp == "STONE":        #PAPEL
        print("You win")
        rodada += 1

        placar_humano = + 1
    elif jogada == "PAPER" and cmp == "SCISSORS":      #PAPEL
        print("You lost")
        rodada += 1
        placar_pc +=  1

        #
    elif jogada == "SCISSORS" and cmp == "SCISSORS":    #TESOURA
        print("DRAW")
        rodada += 1

    elif jogada == "SCISSORS" and cmp == "STONE":      #TESOURA
        print("You lost")
        placar_pc +=  1
        rodada += 1

    elif jogada == "SCISSORS" and cmp == "PAPER":      #TESOURA
        print("You win")
        placar_humano +=  1
        rodada += 1

    #    
    elif cmp == "STONE" and jogada == "STONE":        #PEDRA PC
        print("DRAW")
        rodada += 1

    elif cmp == "STONE" and jogada == "PAPER":        #PEDRA PC
        print("You lost")
        placar_pc +=  1
        rodada += 1

    elif cmp == "STONE" and jogada == "SCISSORS":      #PEDRA PC
        print("You win")
        placar_humano +=  1
        rodada += 1

    #    
    elif cmp == "PAPER" and jogada == "PAPER":        #PAPEL PC
        print("DRAW")
        rodada += 1

    elif cmp == "PAPER" and jogada == "STONE":        #PAPEL PC
        print("You win")
        rodada += 1
        placar_humano += + 1

    elif cmp == "PAPER" and jogada == "SCISSORS":      #PAPEL PC
        print("You lost")
        placar_pc +=  1
        rodada += 1

    #    
    elif cmp == "SCISSORS" and jogada == "SCISSORS":    #TESOURA PC
        print("DRAW")
        rodada += 1

    elif cmp == "SCISSORS" and jogada == "PAPER":      #TESOURA PC
        print("You lost")
        placar_pc += 1
        rodada += 1

    elif cmp == "SCISSORS" and jogada == "PEDRA":      #TESOURA PC
        print("You win")
        placar_humano += 1
        rodada += 1





    print("Your score is {} PTS".format(placar_humano))
    print("The computer score is {} PTS".format(placar_pc))



    if rodada == 3:
        if placar_humano > placar_pc or placar_humano == 2:
            print("=-"*15)
            print("\033[32mYOU WIN!!!\033[m")
            print("=-"*15)
        elif placar_pc > placar_humano or placar_pc == 2:
            print("=-"*15)
            print("\033[31mVYOU LOST :(\033[m")
            print("=-"*15)
        elif placar_humano == placar_pc:
            rodada -= 1