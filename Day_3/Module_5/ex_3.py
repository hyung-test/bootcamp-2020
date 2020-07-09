# Exercise: Print a Word Provided by the User

def ask_input():
    input_user = input("Provide a word: ")
    t_var=type(input_user)
    return t_var

t_var=ask_input()
print(t_var)
if t_var is type(str()):
  print(t_var)
  input_user = input("Provide a word: ")
  print('yes')
else:
  print(t_var)
  ask_input()
      
print(input_user)

