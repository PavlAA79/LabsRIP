import random

def gen_random(num_count, begin, end):
    A =[0]*num_count
    for i in range(num_count):
        A[i] = random.randint(begin, end)
    return A
  
def main():
    print('Задание 2:')
    print(gen_random(5, 1, 3))
    print(gen_random(10, 2, 5))

if __name__ == "__main__":
    main()
