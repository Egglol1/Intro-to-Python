numbers = []
i = 50
while i <= 100:
  numbers.append(str(i) + '\n')
  i += 1

with open('number_list.txt', 'w') as my_file:
  my_file.writelines(numbers)