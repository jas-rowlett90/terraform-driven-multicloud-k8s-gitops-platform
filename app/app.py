from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Terraform-Driven Multi-Cloud Kubernetes Reliability & GitOps Platform",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/status")
def status():
    return jsonify({
        "application": "k8s-reliability-demo-app",
        "environment": "local",
        "platform": "kubernetes",
        "gitops": "argocd",
        "monitoring": "prometheus-grafana"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
