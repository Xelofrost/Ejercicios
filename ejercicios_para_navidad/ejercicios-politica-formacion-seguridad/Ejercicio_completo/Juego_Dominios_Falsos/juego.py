from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Lista de dominios legítimos
dominios_legitimos = [
    "mercadona.com", "nike.com", "microsoft.com", "google.com", "facebook.com",
    "twitter.com", "amazon.com", "linkedin.com", "instagram.com", "wikipedia.org"
]

# Mapa de caracteres visualmente similares, incluyendo Unicode y ASCII extendido
caracteres_similares = {
    'a': ['@', 'α', 'ɒ', 'á', 'а'],
    'b': ['Ь', 'β', 'в'],
    'c': ['ç', 'с', 'κ'],
    'd': ['ⅾ', 'δ'],
    'e': ['3', 'ε', 'é', 'є'],
    'f': ['ғ', 'φ', 'f'],
    'g': ['G', 'ϲ', 'ғ', 'ց'],
    'h': ['һ', 'η', 'н'],
    'i': ['1', 'і', 'ɪ', 'l'],
    'j': ['ј', 'ʝ'],
    'k': ['к', 'κ', 'к'],
    'l': ['1', 'ι', 'ⅼ', 'л'],
    'm': ['м', 'ɯ','rn'],
    'n': ['и', 'и'],
    'o': ['O', '0'],
    'p': ['р', 'ρ'],
    'q': ['қ', 'q'],
    'r': ['R', 'Я', 'n'],
    's': ['ѕ', '5', '$', 'ѕ'],
    't': ['τ', 'т', 't'],
    'u': ['υ', 'ü', 'u'],
    'v': ['ν', 'v'],
    'w': ['ω', 'w'],
    'x': ['х', 'χ', '×'],
    'y': ['у', 'y'],
    'z': ['ѕ', 'Ζ', 'z'],
    '.': ['⋅', '．', '·'],
    '-': ['–', '—', '−'],
    '_': ['＿', '—', '—']
}

# Función para generar dominios falsos difíciles de distinguir
def generar_dominio_falso(legitimo, nivel):
    falso = list(legitimo)  # Convertir el dominio legítimo a una lista de caracteres
    
    # Número de letras a cambiar depende del nivel
    num_letras_a_cambiar = random.randint(1, max(1, nivel))  # Cambiar entre 1 y nivel letras

    indices_a_cambiar = random.sample(range(len(falso)), num_letras_a_cambiar)  # Seleccionamos índices aleatorios

    # Reemplazar caracteres según los índices seleccionados
    for i in indices_a_cambiar:
        letra = falso[i]
        if letra in caracteres_similares:
            falso[i] = random.choice(caracteres_similares[letra])
    
    return ''.join(falso)

# Generar las opciones para cada ronda
def generar_opciones(legitimo, nivel):
    opciones = [legitimo]  # Empezamos con la opción correcta
    
    # Crear 3 dominios falsos difíciles de distinguir, pero sin repetir el correcto
    while len(opciones) < 4:
        falso = generar_dominio_falso(legitimo, nivel)
        # Evitar que se repita el dominio legítimo o algún falso ya generado
        if falso not in opciones:
            opciones.append(falso)
    
    # Mezclar las opciones para que la respuesta correcta esté en cualquier lugar
    random.shuffle(opciones)
    
    return opciones


# Rondas del juego con incremento de dificultad
rondas = [
    {"ronda": 1, "dominio_legitimo": dominios_legitimos[0], "nivel": 1},
    {"ronda": 2, "dominio_legitimo": dominios_legitimos[1], "nivel": 1},
    {"ronda": 3, "dominio_legitimo": dominios_legitimos[2], "nivel": 2},
    {"ronda": 4, "dominio_legitimo": dominios_legitimos[3], "nivel": 2},
    {"ronda": 5, "dominio_legitimo": dominios_legitimos[4], "nivel": 3},
    {"ronda": 6, "dominio_legitimo": dominios_legitimos[5], "nivel": 3},
    {"ronda": 7, "dominio_legitimo": dominios_legitimos[6], "nivel": 4},
    {"ronda": 8, "dominio_legitimo": dominios_legitimos[7], "nivel": 4},
    {"ronda": 9, "dominio_legitimo": dominios_legitimos[8], "nivel": 5},
    {"ronda": 10, "dominio_legitimo": dominios_legitimos[9], "nivel": 5}
]

# Diccionario para llevar el puntaje del jugador y los dominios incorrectos
puntaje = {"aciertos": 0, "fallos": 0}
dominios_incorrectos = []

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/juego', methods=['GET', 'POST'])
def juego():
    ronda_actual = int(request.args.get('ronda', 1))  # obtenemos la ronda actual
    
    if ronda_actual > len(rondas):  # Si se pasa la ronda 10, el juego terminó
        return render_template('fin.html', puntaje=puntaje, dominios_incorrectos=dominios_incorrectos)  # Redirigir a fin.html

    ronda = rondas[ronda_actual - 1]
    dominio_legitimo = ronda["dominio_legitimo"]
    nivel = ronda["nivel"]

    # Generar las opciones para la ronda actual
    opciones = generar_opciones(dominio_legitimo, nivel)

    if request.method == 'POST':  # Cuando el usuario envía la respuesta
        respuesta = request.form['respuesta']
        if respuesta == dominio_legitimo:
            puntaje["aciertos"] += 1
            resultado = "Correcto"
        else:
            puntaje["fallos"] += 1
            dominios_incorrectos.append(dominio_legitimo)  # Registrar el dominio en que se equivocó
            resultado = "Incorrecto"
        
        # Después de responder, avanzamos a la siguiente ronda
        return redirect(url_for('juego', ronda=ronda_actual + 1))

    # Si es GET, simplemente mostramos la página de la ronda actual
    return render_template('juego.html', ronda=ronda, opciones=opciones, ronda_actual=ronda_actual, puntaje=puntaje)

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    # Reinicia el puntaje y las rondas
    global puntaje, dominios_incorrectos
    puntaje = {"aciertos": 0, "fallos": 0}
    dominios_incorrectos = []  # Limpiar los dominios incorrectos
    return redirect(url_for('inicio'))  # Vuelve al inicio para reiniciar el juego


if __name__ == "__main__":
    app.run(debug=True)
