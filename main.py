def fib(n):
  if n == 1: return 2
  if n == 0: return 1
  return fib(n-1) + fib(n-2)
  
if __name__ == '__main__':
  print('Started')
  fib(10)
