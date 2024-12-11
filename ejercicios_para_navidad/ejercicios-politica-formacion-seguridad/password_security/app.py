from flask import Flask, render_template, request

app = Flask(__name__)

# Función para evaluar la seguridad de la contraseña
def evaluar_contrasena(password):
    score = 0

    # Asegurarse de que no esté vacía
    if len(password) >= 8:
        score += 1  # Larga

    if any(c.isdigit() for c in password):
        score += 1  # Contiene números

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1  # Contiene minúsculas y mayúsculas

    if any(c in '!@#$%^&*()_+' for c in password):
        score += 1  # Contiene caracteres especiales

    return score

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    score = 0
    result = ""
    
    # Si se ha enviado el formulario
    if request.method == 'POST':
        password = request.form['password']
        score = evaluar_contrasena(password)
        
        # Determinamos el mensaje según la seguridad de la contraseña
        if score == 0:
            result = "La contraseña es muy débil."
        elif score == 1:
            result = "La contraseña es débil."
        elif score == 2:
            result = "La contraseña es aceptable."
        elif score == 3:
            result = "La contraseña es fuerte."
        else:
            result = "La contraseña es muy fuerte."

    return render_template('index.html', password=password, score=score, result=result)

if __name__ == "__main__":
    app.run(debug=True)
