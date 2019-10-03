def fibonacci(number):
  if number == 1:
    return 2
  else return fibonacci(number - 1) + fibonacci(number - 2)
  
if __name__ == '__main__':
  print('Started')
  fibonacci(10)
