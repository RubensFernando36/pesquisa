from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuração do banco de dados
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Glaysirf36!",
    database="pesquisa"
)

@app.route('/add_participant', methods=['POST'])
def add_participant():
    data = request.json
    cursor = db.cursor()
    sql = "INSERT INTO participantes (nome, idade, sexo, estado, escolaridade, estado_civil, tem_filhos) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (data['nome'], data['idade'], data['sexo'], data['estado'], data['escolaridade'], data['estado_civil'], data['tem_filhos'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Participant added successfully!"}), 201

@app.route('/get_participants', methods=['GET'])
def get_participants():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM participantes")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
