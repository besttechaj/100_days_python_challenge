# function with output

def format_name(fname, lname):
  formated_fname = fname.title()
  formated_lname = lname.title()
  return f"{formated_fname} {formated_lname}"
result = format_name("shiVAni", "SHARMA")
# print(result)


def func_01(text):
  return text + ' '+ text

def func_02(text2):
  return text2.title()

output = func_02(func_01("SHIVANI123"))
# print(output)


## multiple return value

def format_name(fname, lname):
  if fname == '' or lname == '':
    return 'You did not provide valid inputs'
  formated_fname = fname.title()
  formated_lname = lname.title()
  return f"{formated_fname} {formated_lname}"

print(format_name(input('What is your first name ? \n'), input('What is your last name ?\n')))


#! DocStrings : A docstring is a special string used to document a function, class, or module. It is placed as the first statement inside the definition and is written using triple quotes (""" """ or ''' '''). Docstrings help explain what the code does and how to use it. Docstring can be used for multi line comments

def greet(name):
    """
    This function returns a greeting message for the given name.
    """
    return f"Hello, {name}!"
print(greet.__doc__)


