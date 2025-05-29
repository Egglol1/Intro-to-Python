import pickle
recipe = {
  'Name': 'Tea',
  'Ingredients': 'Tea Leaves, Water, Sugar',
  'Cooking Time': '5 minutes',
  'Difficulty': 'Easy'
}

with open('recipe_binary.bin', 'wb') as my_file:
  pickle.dump(recipe, my_file)


with open('recipe_binary.bin', 'rb') as loaded_file:
  loaded_recipe = pickle.load(loaded_file)

print('Recipe - ')
print('Name: ' + loaded_recipe['Name'])
print('Ingredients: ' + loaded_recipe['Ingredients'])
print('Cooking Time: ' + loaded_recipe['Cooking Time'])
print('Difficulty: ' + loaded_recipe['Difficulty'])