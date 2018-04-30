



def sum_recu(n):
    if n > 0:
        return n + sum_recu( n - 1 )
    else:
        return 0

print("递归求和：",sum_recu(4))

def func(n):
    print('a', end='\t')

    if n<= 1:
        return

    func(n-1)

    print('b', end='\t')

func(3)
