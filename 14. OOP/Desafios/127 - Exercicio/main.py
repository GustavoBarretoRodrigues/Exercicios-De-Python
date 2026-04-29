from personagem import *

def main():
    p1 = Guerreiro('Kratos', 100)
    p2 = Mago('Luigi', 1000)
    p1.atacar(p2, 40)
    p2.curar(30)

if __name__ == '__main__':
    main()