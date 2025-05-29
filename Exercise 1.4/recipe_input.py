import pickle

def take_recipe():
  name = input('What\'s the name of this recipe? ')
  cooking_time = int(input('How long does it take to cook? (In minutes, please) '))
  ingredients = []
  i = int(input('How many ingredients are in this recipe? '))
  for each in range(i):
    element = input('Enter Ingredient Name: ')
    ingredients.append(element)
  difficulty = calc_difficulty(cooking_time, ingredients)
  recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients, 'difficulty': difficulty}
  return recipe

def calc_difficulty(cooking_time, ingredients):
  if len(ingredients) < 4 and cooking_time < 10:
    return 'Easy'
  elif len(ingredients) >= 4 and cooking_time < 10:
    return 'Medium'
  elif len(ingredients) < 4 and cooking_time >= 10:
    return 'Intermediate'
  elif len(ingredients) >= 4 and cooking_time >= 10:
    return 'Hard'
  
filename = input('Enter the name of the file where your ingredients are stored. ')
try:
  my_file = open(filename, 'rb')
  data = pickle.load(my_file)
except FileNotFoundError:
  print('File not found.')
  data = {
    'recipes_list': [],
    'all_ingredients': []
  }
except:
  print('Some error has occurred.')
  data = {
    'recipes_list': [],
    'all_ingredients': []
  }
else:
  my_file.close()
finally:
  recipes_list = data['recipes_list']
  all_ingredients = data['all_ingredients']

n = int(input('How many recipes would you like to enter? '))
for each in range(n):
  recipe = take_recipe()
  for ingredients in recipe.get('ingredients'):
    if ingredients not in all_ingredients:
      all_ingredients.append(ingredients)
  recipes_list.append(recipe)

all_ingredients.sort()
print('All Ingredients: ' + '\n' + '~~~~~~~~~~~~~~~~~~~~')
for ingredient in all_ingredients:
  print(ingredient)

data['recipes_list'] = recipes_list
data['all_ingredients'] = all_ingredients
my_file = open(filename, 'wb')
pickle.dump(data, my_file)