from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

engine = create_engine('mysql://cf-python:password@localhost/task_database')
Base = declarative_base()

class Recipe(Base):
  __tablename__ = 'final_recipes'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50))
  ingredients = Column(String(255))
  cooking_time = Column(Integer)
  difficulty = Column(String(20))

  def __repr__(self):
    return '<Recipe ID: ' + str(self.id) + '-' + self.name + '-' + self.difficulty + '>'
  
  def __str__(self):
    return '-'*5 + '\n Recipe: ' + self.name +  '\n Ingredients: ' + self.ingredients + '\n Cooking Time: ' + str(self.cooking_time) + '\n Difficulty: ' + self.difficulty + '\n'
  
  def calc_difficulty(self):
    split_ingredients = self.ingredients.split(', ')
    if len(split_ingredients) < 4 and int(self.cooking_time) < 10:
      self.difficulty = 'Easy'
    elif len(split_ingredients) >= 4 and int(self.cooking_time) < 10:
      self.difficulty = 'Medium'
    elif len(split_ingredients) < 4 and int(self.cooking_time) >= 10:
      self.difficulty = 'Intermediate'
    elif len(split_ingredients) >= 4 and int(self.cooking_time) >= 10:
      self.difficulty = 'Hard'

  def return_ingredients_as_list(self):
    if (self.ingredients == ''):
      return []
    else:
      return self.ingredients.split(', ')
  
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_recipe():
  name_input = input('What\'s the name of this recipe? ')
  while len(name_input) > 50:
    name_input = input('Please enter a name shorter than 50 characters. ')
  cooking_time_input = input('How long does it take to cook? (In minutes, please) ')
  while not cooking_time_input.isalnum():
    cooking_time_input = input('Please only enter numeric characters for cooking time. ')
  ingredients_input = []
  i = int(input('How many ingredients are in this recipe? '))
  for each in range(i):
    element = input('Enter Ingredient Name: ')
    ingredients_input.append(element)
  ingredients_string = ", ".join(ingredients_input)
  recipe_entry = Recipe(
    name = name_input,
    cooking_time = cooking_time_input,
    ingredients = ingredients_string
  )
  recipe_entry.calc_difficulty(int(cooking_time_input), ingredients_input)
  session.add(recipe_entry)
  session.commit()
  print('Recipe Added!')

def view_all_recipes():
  all_recipes = session.query(Recipe).all()
  if all_recipes == []:
    print('The database is empty!')
    return None
  else:
    for recipe in all_recipes:
      print(recipe)

def search_by_ingredients():
  if session.query(Recipe).count() == 0:
    print('There are no entries in the Recipe table!')
    return None
  else:
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    i = 0
    for each in results:
      temp = each[0].split(', ')
      for element in temp:
        if element not in all_ingredients:
          all_ingredients.append(element)
          print(element + ': ' + str(i))
          i += 1
    selection = input('Which ingredient would you like to search for? (Please enter the numbers associated separated by spaces) ')
    choices = selection.split(' ')
    search_ingredients = []
    for choice in choices: 
      if not choice.isalnum():
        print('Please enter a number for your choice')
        return None
      elif int(choice) > len(all_ingredients):
        print('You\'ve searched for an ingredient that does not exit!')
        return None
      else:
        search_ingredients.append(all_ingredients[int(choice)])
    conditions = [
        Recipe.ingredients.like(f"%{ingredient}%") for ingredient in search_ingredients
    ]
    searched = session.query(Recipe).filter(*conditions).all()
    for recipe in searched:
      print(recipe)

def edit_recipe():
  if session.query(Recipe).count() == 0:
    print('No recipes exist in the database! Make some!')
    return None
  else:
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    for each in results:
      print(each)
    pick_recipe = int(input('Pick a recipe by its id number. '))
    for recipe in results:
      if pick_recipe == recipe[0]:
        recipe_to_edit = session.query(Recipe).filter(Recipe.id.like(pick_recipe)).one()
        print('Name: ' + recipe_to_edit.name + ' - 1')
        print('Ingredients: ' + recipe_to_edit.ingredients + ' - 2')
        print('Cooking Time: ' + str(recipe_to_edit.cooking_time) + ' - 3')
        attribute_to_edit = input('Enter the number of the attribute you wish to change. ')
        if attribute_to_edit == '1':
          name_change = input('Enter the new name of this recipe. ')
          while len(name_change) > 50:
            name_change = input('Please enter a name that is less than 50 characters. ')
          session.query(Recipe).filter(Recipe.id.like(pick_recipe)).update({Recipe.name: name_change})
          session.commit()
          print('Recipe updated!')
        elif attribute_to_edit == '2':
          ingredients_input = []
          i = int(input('How many ingredients are in this recipe? '))
          for each in range(i):
            element = input('Enter Ingredient Name: ')
            ingredients_input.append(element)
          ingredients_string = ", ".join(ingredients_input)
          session.query(Recipe).filter(Recipe.id.like(pick_recipe)).update({Recipe.ingredients: ingredients_string})
          recipe_to_edit.calc_difficulty()
          session.commit()
          print('Recipe updated!')
        elif attribute_to_edit == '3':
          c_t_change = input('Enter the new cooking time of this recipe. ')
          while not c_t_change.isalnum():
            c_t_change = input('Please only use numeric characters for cooking time. ')
          session.query(Recipe).filter(Recipe.id.like(pick_recipe)).update({Recipe.cooking_time: c_t_change})
          recipe_to_edit.calc_difficulty()
          session.commit()
          print('Recipe updated!')
        else:
          print('Your input does not match the choices given.')
          return None
    else:
      return None
      
def delete_recipe():
  if session.query(Recipe).count() == 0:
    print('There are no recipes in the database!')
    return None
  else:
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    for each in results:
      print(each)
    pick_id = int(input('Pick a recipe TO DELETE by its id number. '))
    for each in results:
      if pick_id == each[0]:
        id_to_delete = session.query(Recipe).filter(Recipe.id.like(pick_id)).one()
        recipe_name = id_to_delete.name
        yorn = input('Are you sure that you want to delete ' + recipe_name + '? (Type "Yes" or "No") ')
        if yorn == 'Yes':
          session.delete(id_to_delete)
          session.commit()
          print('Recipe deleted!')
        else:
          print('Recipe NOT deleted!')
          return None
    else:
      return None
      
choice = ''
while choice != 'quit':
  print('What would you like to do?')
  print('1. Create a new recipe')
  print('2. View all recipes')
  print('3. Search for a recipe by ingredient')
  print('4. Update an existing recipe')
  print('5. Delete a recipe')
  print('Type "quit" to exit the program.')
  choice = input('Your choice: ')

  if choice == '1':
    create_recipe()
  elif choice == '2':
    view_all_recipes()
  elif choice == '3':
    search_by_ingredients()
  elif choice == '4':
    edit_recipe()
  elif choice == '5':
    delete_recipe()
  elif choice == 'quit':
    None
  else:
    print('Your input does not match any of the given numbers, try again.')

session.close()