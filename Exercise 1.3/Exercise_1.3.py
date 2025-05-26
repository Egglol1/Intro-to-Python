recipes_list = []
ingredients_list = []
def take_recipe():
  name = input('What\'s the name of this recipe? ')
  cooking_time = int(input('How long does it take to cook? (In minutes, please) '))
  ingredients = []
  i = int(input('How many ingredients are in this recipe? '))
  for each in range(i):
    element = input('Enter Ingredient Name: ')
    ingredients.append(element)
  recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
  return recipe

n = input('How many recipes would you like to enter? ')
for i in n:
  recipe = take_recipe()
  for i in recipe.get('ingredients'):
    if i not in ingredients_list:
      ingredients_list.append(i)
  recipes_list.append(recipe)

for recipe in recipes_list:
  if len(recipe.get('ingredients')) < 4 and recipe.get('cooking_time') < 10:
    recipe['difficulty'] = 'Easy'
  elif len(recipe.get('ingredients')) >= 4 and recipe.get('cooking_time') < 10:
    recipe['difficulty'] = 'Medium'
  elif len(recipe.get('ingredients')) < 4 and recipe.get('cooking_time') >= 10:
    recipe['difficulty'] = 'Intermediate'
  elif len(recipe.get('ingredients')) >= 4 and recipe.get('cooking_time') >= 10:
    recipe['difficulty'] = 'Hard'

  print('Recipe:', recipe.get('name') + '\n' \
        + 'Cooking Time (min):', str(recipe.get('cooking_time')) + '\n' \
        +  'Ingredients:', str(recipe.get('ingredients')) + '\n' \
          + 'Difficulty Level:', recipe.get('difficulty'))
  
ingredients_list.sort()
print('All Ingredients: ' + '\n' + '~~~~~~~~~~~~~~~~~~~~')
for ingredient in ingredients_list:
  print(ingredient)