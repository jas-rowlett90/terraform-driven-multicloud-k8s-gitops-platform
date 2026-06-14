from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "This app was created for the Terraform-Driven Multi-Cloud Kubernetes Reliability & GitOps Platform project. There are no specifics to this application or additional functions input in to this function as a result.",
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
