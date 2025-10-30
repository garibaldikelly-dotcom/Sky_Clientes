# app.py
from flask import Flask, request, jsonify, abort
from pathlib import Path
import json
import uuid

DATA_DIR = Path("/opt/sky_clients")  # en EC2 crea esta carpeta y da permisos
DATA_DIR.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)

def client_file_path(name):
    # normaliza el nombre para filename
    safe = "".join(c for c in name if c.isalnum() or c in (" ", "_", "-")).strip().replace(" ", "_")
    return DATA_DIR / f"{safe}.json"

@app.route("/clients", methods=["GET"])
def list_clients():
    files = list(DATA_DIR.glob("*.json"))
    clients = []
    for f in files:
        try:
            clients.append(json.loads(f.read_text()))
        except Exception:
            pass
    return jsonify(clients), 200

@app.route("/clients/<string:name>", methods=["GET"])
def get_client(name):
    f = client_file_path(name)
    if not f.exists():
        return jsonify({"error":"cliente no encontrado"}), 404
    return jsonify(json.loads(f.read_text())), 200

@app.route("/clients", methods=["POST"])
def create_client():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error":"campo 'name' requerido"}), 400
    name = data["name"]
    f = client_file_path(name)
    if f.exists():
        return jsonify({"error":"cliente ya existe"}), 409
    client = {
        "id": str(uuid.uuid4()),
        "name": name,
        "contact": data.get("contact", {}),
        "address": data.get("address", {}),
        "services": [ data.get("service_description","") ],
        "created_at": data.get("created_at", "")
    }
    f.write_text(json.dumps(client, indent=2))
    return jsonify(client), 201

@app.route("/clients/<string:name>", methods=["PUT"])
def update_client(name):
    f = client_file_path(name)
    if not f.exists():
        return jsonify({"error":"cliente no encontrado"}), 404
    body = request.get_json()
    client = json.loads(f.read_text())
    # permitir update parcial
    if "name" in body:
        client["name"] = body["name"]
    if "contact" in body:
        client["contact"] = body["contact"]
    if "address" in body:
        client["address"] = body["address"]
    if "service_description" in body:
        # agregar al historial de servicios
        client.setdefault("services", []).append(body["service_description"])
    f.write_text(json.dumps(client, indent=2))
    return jsonify(client), 200

@app.route("/clients/<string:name>", methods=["DELETE"])
def delete_client(name):
    f = client_file_path(name)
    if not f.exists():
        return jsonify({"error":"cliente no encontrado"}), 404
    f.unlink()
    return jsonify({"deleted":name}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
