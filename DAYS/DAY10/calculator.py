
def add(n1, n2):
  return n1 + n2
def mul(n1, n2):
  return n1 * n2
def sub(n1, n2):
  return n1 - n2
def div(n1, n2):
  return n1 / n2

operators= {
  '+':add,
  '-':sub,
  '/':div,
  '*':mul
}

def calculator():
    first_num = float(input('Enter your first number\n'))

    should_accumulate = True

    while should_accumulate:

      for symbol in operators:
        print(symbol)
      operation = input('pick an operation: \n')
      second_num = float(input('Enter your second number\n'))


      def calculation(n1, n2):
        for key in operators:
          if key == operation:
            return operators[key](n1,n2)


      result = calculation(first_num, second_num)
      print(f'Your result is {result}')

      choice = input('Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation ? \n').lower()

      if choice == 'y':
        first_num = result
      else:
        should_accumulate = False
        print('\n' * 20)
        calculator()

calculator()
