import pickle

def display_recipe(recipe):
  print('Name: ' + recipe['name'])
  print('Cooking Time: ' + str(recipe['cooking_time']))
  print('Ingredients: ' + str(recipe['ingredients']))
  print('Difficulty: ' + recipe['difficulty'])

def search_ingredient(data):
  for position, value in enumerate(data['all_ingredients']):
    print('Ingredient ' + str(position) + ': ' + value)
  try:
    pick = int(input('Pick a number corresponding to the ingredient you want to search. '))
    ingredients_w_values = list(enumerate(data['all_ingredients']))
    ingredient_searched = ingredients_w_values[pick][1]
  except:
    print('Some error has occurred. Your input may not exist.')
  else:
    for recipe in data['recipes_list']:
      if ingredient_searched in recipe['ingredients']:
        display_recipe(recipe)

filename = input('What is the name of the file containing your recipes? ')
try:
  my_file = open(filename, 'rb')
  data = pickle.load(my_file)
except:
  print('The file has not been found. :(')
else:
  search_ingredient(data)