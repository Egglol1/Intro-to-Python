import mysql.connector

conn = mysql.connector.connect(host='localhost',user='cf-python',passwd='password')

cursor = conn.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS task_database')
cursor.execute('USE task_database')
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)''')
def main_menu(conn, cursor):
  
  def create_recipe(conn, cursor):
    name = input('What\'s the name of this recipe? ')
    cooking_time = input('How long does it take to cook? (In minutes, please) ')
    ingredients = []
    i = int(input('How many ingredients are in this recipe? '))
    for each in range(i):
      element = input('Enter Ingredient Name: ')
      ingredients.append(element)
    difficulty = calc_difficulty(int(cooking_time), ingredients)
    ingredients_string = ", ".join(ingredients)
    cursor.execute('INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (\''+name+'\', \''+ ingredients_string+'\', \''+cooking_time+'\', \''+difficulty+'\')')
    conn.commit()
    print('Recipe Added!')

  def calc_difficulty(cooking_time, ingredients):
    if len(ingredients) < 4 and cooking_time < 10:
      return 'Easy'
    elif len(ingredients) >= 4 and cooking_time < 10:
      return 'Medium'
    elif len(ingredients) < 4 and cooking_time >= 10:
      return 'Intermediate'
    elif len(ingredients) >= 4 and cooking_time >= 10:
      return 'Hard'

  def search_recipe(conn, cursor):
    all_ingredients = []
    i = 0
    cursor.execute('SELECT ingredients FROM Recipes')
    results = cursor.fetchall()
    for ingredient in results:
      temp = ingredient[0].split(', ')
      for element in temp:
        if element not in all_ingredients:
          all_ingredients.append(element)
          print('Ingredient: ' + element + ', ' +  str(i))
          i += 1
    try:
      pick = int(input('Pick a number corresponding to the ingredient you want to search. '))
      search_ingredient = all_ingredients[pick]
    except:
      print('Error! Your input may not exist.')
    else:
      cursor.execute('SELECT * FROM Recipes WHERE ingredients LIKE \'%'+search_ingredient+'%\'')
      search = cursor.fetchall()
      print(search)

  def update_recipe(conn, cursor):
    cursor.execute('SELECT * FROM Recipes')
    all_recipes = cursor.fetchall()
    print(all_recipes)
    item_id = input('Enter the id of the recipe to be updated. ')
    column = input('Which column do you wish to modify, name, cooking_time, or ingredients? ')
    new_value = input('What do you wish to change the old value to? ')
    print('UPDATE Recipes SET ' + column + ' = ' + new_value + ' WHERE id = ' + item_id)
    try:
      cursor.execute('UPDATE Recipes SET ' + column + ' = ' + new_value + ' WHERE id = ' + item_id)
    except:
      print('Error! Your input might not be compatiable with the data type of the column you\'ve selected.')
    else:
      #recalculate difficulty in case cooking time or ingredients changes
      cursor.execute('SELECT cooking_time FROM Recipes where id = ' + item_id)
      cooking_time = int(cursor.fetchall()[0][0])
      cursor.execute('SELECT ingredients FROM Recipes where id = ' + item_id)
      ingredients = cursor.fetchall()[0][0].split(', ')
      difficulty = calc_difficulty(cooking_time, ingredients)
      cursor.execute('UPDATE Recipes SET difficulty = \'' + difficulty + '\' WHERE id = ' + item_id)
      conn.commit()
      print('Recipe Updated!')

  def delete_recipe(conn, cursor):
    cursor.execute('SELECT * FROM Recipes')
    all_recipes = cursor.fetchall()
    print(all_recipes)
    item_id = input('Enter the id of the recipe to be deleted. ')
    cursor.execute('DELETE FROM Recipes WHERE id = ' + item_id)
    conn.commit()
    print('Recipe Deleted!')

  choice = ''
  while (choice != 'quit'):
    print('What would you like to do?')
    print('1. Create a new recipe')
    print('2. Search for a recipe by ingredient')
    print('3. Update an existing recipe')
    print('4. Delete a recipe')
    print('Type "quit" to exit the program.')
    choice = input('Your choice: ')

    if choice == '1':
      create_recipe(conn, cursor)
    elif choice == '2':
      search_recipe(conn, cursor)
    elif choice == '3':
      update_recipe(conn, cursor)
    elif choice == '4':
      delete_recipe(conn, cursor)

  conn.commit()
  conn.close()

main_menu(conn, cursor)