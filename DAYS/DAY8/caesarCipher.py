
#* caesarCipher


alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't',  'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_or_decode, original_text, shift_amount):
  output_text = ""
  if encode_or_decode == 'decrypt':
      shift_amount *= -1 #!to make the code work as decode else it will work as encode only

  for letter in original_text:
    if letter in alphabets:#? make sure if user enters a number/symbol/space
      shifted_position = alphabets.index(letter) + shift_amount
      shifted_position %= len(alphabets) #? make sure we are always in the range 0-25. it prevent index out of bound error
      output_text += alphabets[shifted_position]
    else:
      output_text += letter
  print(f'Here is the {encode_or_decode} result: {output_text}')



#? to restart cipher program

should_continue = True

while should_continue:
  direction=input('Select whether you want to \'encrypt\' or \'decrypt\' your message ?\n')
  text = input('Type your message:\n').lower()
  shift=int(input('Type the shift number:\n'))

  caesar(encode_or_decode = direction, original_text = text, shift_amount = shift)

  restart = input('Type \'yes\' if you want to go again. Otherwise, Type \'no\' ?\n ').lower()
  if restart == 'no':
    should_continue = False
    print('Goodbye')






