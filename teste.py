from flask import Flask, request, jsonify
import cx_Oracle
from pymongo import MongoClient

app = Flask(__name__)

# Configurar conexão com Oracle
oracle_conn = cx_Oracle.connect("user/password@host:port/service_name")

# Configurar conexão com MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client['nome_do_banco_mongodb']

@app.route('/update', methods=['POST'])
def update_mongodb():
    data = request.json
    
    # Verificar o tipo de atualização e a coleção correspondente
    collection_name = data.get('collection')
    update_data = data.get('data')
    
    if collection_name and update_data:
        collection = mongo_db[collection_name]
        
        # Exemplo: se estiver atualizando um ponto turístico
        if collection_name == 'ponto_turistico':
            query = {"_id": update_data["_id"]}
            new_values = {"$set": update_data}
            collection.update_one(query, new_values)
            return jsonify({"status": "success"}), 200
        
        # Implementar lógica semelhante para outras coleções
        # ...
    
    return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
