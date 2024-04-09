# Model
class TodoModel:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def get_todos(self):
        return self.todos


# View
class TodoView:
    def show_todos(self, todos):
        print("Todos:")
        for idx, todo in enumerate(todos, start=1):
            print(f"{idx}. {todo}")

    def get_input(self):
        return input("Enter todo: ")


# Controller
class TodoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_todo(self, todo):
        self.model.add_todo(todo)

    def get_todos(self):
        return self.model.get_todos()

    def show_todos(self):
        todos = self.get_todos()
        self.view.show_todos(todos)

    def run(self):
        while True:
            self.show_todos()
            todo = self.view.get_input()
            self.add_todo(todo)


# Main
if __name__ == "__main__":
    model = TodoModel()
    view = TodoView()
    controller = TodoController(model, view)
    controller.run()
