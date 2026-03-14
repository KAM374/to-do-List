from flask import Flask

app = Flask(__ToDoList__)
@app.route('/')

tasks = []
print("To-Do List")
 
while True:

  i=0
  i=i+1
  action = input("Type 'add', 'delete', 'quit': ")

  if action == "add":
    task = input("enter a task: ")
    tasks.append(task)
    
  elif action == "delete":
    num = int(input("enter the task number to delete: "))
    tasks.pop(num-1)
    print("Your To-Do List \n",  tasks)
    
  elif  action == "quit":
    print("Your To-Do List \n",  tasks)
     
if __ToDoList__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)
