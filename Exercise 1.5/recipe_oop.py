class Recipe():
  all_ingredients = []
  def __init__(self, name, ingredients, cooking_time):
    self.name = name
    self.ingredients = ingredients
    self.cooking_time = cooking_time
    self.calc_difficulty(cooking_time, ingredients)
    
  def get_name(self):
    output = self.name
    return output
  
  def set_name(self):
    self.name = input("Enter the new name of this recipe. ")

  def get_cooking_time(self):
    output = self.cooking_time
    return output
  
  def set_cooking_time(self):
    self.name = input("Enter the new cooking time of this recipe. ")

  def update_all_ingredients(self):
    for ingredient in self.ingredients:
      if not ingredient in all_ingredients:
       all_ingredients += ingredient

  def add_ingredients(self, new_ingredients):
    self.ingredients.extend(new_ingredients)
    self.update_all_ingredients()

  def calc_difficulty(self, cooking_time, ingredients):
    if len(ingredients) < 4 and cooking_time < 10:
      self.difficulty = 'Easy'
    elif len(ingredients) >= 4 and cooking_time < 10:
      self.difficulty = 'Easy'
    elif len(ingredients) < 4 and cooking_time >= 10:
      self.difficulty = 'Easy'
    elif len(ingredients) >= 4 and cooking_time >= 10:
      self.difficulty = 'Easy'
    
  def get_difficulty(self, cooking_time, ingredients):
    self.calc_difficulty(cooking_time, ingredients)

  def search_ingredient(self, ingredient):
    if ingredient in self.ingredients:
      return True
    else:
      return False
    
  def __str__(self):
    output = 'Recipe: ' + self.name + '\nCooking Time: ' + str(self.cooking_time) + '\nDifficulty: ' + self.difficulty + '\nIngredients:\n'
    for ingredient in self.ingredients:
      output += ingredient + '\n'
    return output
  
def recipe_search(data, search_term):
  for recipe in data:
    if recipe.search_ingredient(search_term):
      print(recipe)

recipe1 = Recipe('Tea', ['Tea Leaves', 'Sugar', 'Water'], 5)
recipe2 = Recipe('Coffee', ['Coffee Powder', 'Sugar', 'Water'], 5)
recipe3 = Recipe('Cake', ['Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk'], 50)
recipe4 = Recipe('Banana Smoothie', ['Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes'], 5)

recipes_list = [recipe1, recipe2, recipe3, recipe4]

print(recipe1)

recipe_search(recipes_list, 'Water')
recipe_search(recipes_list, 'Sugar')
recipe_search(recipes_list, 'Bananas')