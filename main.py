from flask import Flask
import random


facts_list = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos.",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna.",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo.",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo.",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos.",
    "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos.",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas."
]

app = Flask(__name__)


def gen_pass(length=10):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
    return ''.join(random.choice(caracteres) for _ in range(length))


@app.route("/")
def hello_world():
    return "<h1>Hola, esta es una página que habla sobre la dependencia de la tecnología</h1><br><a href='/random_fact'>¡Ver un dato aleatorio!</a><br><a href='/random_pass'>¡Generar una contraseña aleatoria!</a>"

@app.route("/random_fact")
def random_fact():
    return f'<h3>{random.choice(facts_list)}</h3>'



@app.route("/random_pass")
def random_pass():
    return f"<h3>{gen_pass(10)}</h3>"


app.run(debug=True)
