from flask import Flask, request, jsonify
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metrics
machine_temp = Gauge('machine_temperature', 'Temperature of machine', ['machine_id', 'hospital'])
machine_runtime = Gauge('machine_runtime_hours', 'Runtime hours', ['machine_id', 'hospital'])
machine_status = Gauge('machine_status', 'Status (1=Running, 0=Stopped)', ['machine_id', 'hospital'])
machine_error = Gauge('machine_error_code', 'Error code (numeric)', ['machine_id', 'hospital'])

@app.route('/telemetry', methods=['POST'])
def telemetry():
    data = request.json
    machine_id = data.get('machine_id')
    hospital = data.get('hospital')
    temp = data.get('temperature')
    runtime = data.get('runtime_hours')
    status = 1 if data.get('status') == 'Running' else 0
    error_code = int(data.get('error_code').replace('E', ''))

    # Update Prometheus metrics
    machine_temp.labels(machine_id, hospital).set(temp)
    machine_runtime.labels(machine_id, hospital).set(runtime)
    machine_status.labels(machine_id, hospital).set(status)
    machine_error.labels(machine_id, hospital).set(error_code)

    return jsonify({"message": "Telemetry received"}), 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/')
def index():
    return "Medical Equipment Monitoring Backend is running!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

