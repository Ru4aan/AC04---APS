from multiprocessing import Pool
import random

def num_aleatorio():
     lista_nums = []
     for i in range(10):
          num = random.randrange(1, 10000)
          lista_nums.append(num)
     return lista_nums

def eh_primo(n):
     for i in range(3, int(n**0.5+1), 2):
          if n % i == 0:
               print(n, ' não eh primo!')
               return False
     print(n, 'eh primo!')
     return True

if __name__ == '__main__':
     numeros = num_aleatorio()
     pool = Pool()
     pool.map(eh_primo, numeros)
     