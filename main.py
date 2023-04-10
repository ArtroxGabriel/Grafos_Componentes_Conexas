trash = input()  # trash: variavel descartavel
trash = input()
trash, NumIndices = input().split("n = ")
NumIndices = int(NumIndices)
trash = input()
print(NumIndices)

status = True

while status:
  try:
    user_input = input("Enter some input: ")
  except EOFError:
    status = False
