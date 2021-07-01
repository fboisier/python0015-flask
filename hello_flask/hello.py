from flask import Flask, render_template    # Importar Flask para que permita crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

# flask ocupa Jinja2  para el uso de templates. 

@app.route('/')          # El decorador "@" asocia la ruta con la función siguiente
def hello_world():
    return 'Hello World!'  # Retorna la cadena 'Hello World!' como respuesta

# declaraciones de importacia, tal vez algunas otras rutas
@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>') # para una ruta '/hello/____' cualquier cosa despues de '/hello/' se pasa como una variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name


@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


# @app.route('/home')
# def home():
#     # En lugar de devolver una cadena, 
#     # devolvemos el resultado del metodo render_template , pasando el nombre de nuestro archivo HTML
#     return render_template('index.html')  

@app.route('/home')
def index():
    return render_template("index.html", phrase="hello", times=5)	# observa los 2 nuevos argumentos nombrados!

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info, users = users)

if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuración