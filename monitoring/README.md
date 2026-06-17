# Lightweight Monitoring

This project uses lightweight Prometheus and Grafana Helm deployments instead of kube-prometheus-stack due to local resource constraints while still demonstrating production-inspired Kubernetes monitoring practices.

## Purpose

The monitoring stack provides:

- Prometheus metrics collection
- Grafana visualization and dashboards
- Kubernetes workload monitoring
- Reliability and observability foundations
- Resume-ready monitoring experience

---

## Create Monitoring Namespace

```bash
kubectl create namespace monitoring
```

---

## Prometheus Configuration

File: `monitoring/prometheus-values.yaml`

```yaml
alertmanager:
  enabled: false

prometheus-pushgateway:
  enabled: false

kube-state-metrics:
  enabled: false

prometheus-node-exporter:
  enabled: false

server:
  persistentVolume:
    enabled: false

  resources:
    requests:
      cpu: 100m
      memory: 256Mi

    limits:
      cpu: 300m
      memory: 512Mi
```

Install Prometheus:

```bash
helm install prometheus prometheus-community/prometheus \
  --namespace monitoring \
  -f monitoring/prometheus-values.yaml
```

---

## Grafana Configuration

File: `monitoring/grafana-values.yaml`

```yaml
persistence:
  enabled: false

adminUser: admin
adminPassword: admin

resources:
  requests:
    cpu: 100m
    memory: 128Mi

  limits:
    cpu: 300m
    memory: 256Mi
```

Install Grafana:

```bash
helm install grafana grafana/grafana \
  --namespace monitoring \
  -f monitoring/grafana-values.yaml
```

---

## Access Prometheus

Port-forward:

```bash
kubectl port-forward -n monitoring svc/prometheus-server 9090:80
```

Open:

```text
http://localhost:9090
```

---

## Access Grafana

Port-forward:

```bash
kubectl port-forward -n monitoring svc/grafana 3000:80
```

Open:

```text
http://localhost:3000
```

Default login:

```text
Username: admin
Password: admin
```

---

## Configure Grafana Data Source

Add Prometheus as a data source.

Prometheus URL:

```text
http://prometheus-server.monitoring.svc.cluster.local
```

Save and test the connection.

---

## Basic Validation

Verify Prometheus and Grafana are running:

```bash
kubectl get pods -n monitoring
kubectl get svc -n monitoring
```

Expected output:

```text
grafana                             Running
prometheus-server                   Running
```

---

## Dashboard Validation

Example Prometheus query:

```promql
up
```

Successful results confirm:

- Grafana connectivity
- Prometheus availability
- Metrics collection
- Monitoring stack health

---

## Architecture Position

This monitoring layer sits on top of:

- Terraform
- EKS
- AKS
- Kubernetes
- Kustomize
- ArgoCD
- GitOps

and provides the observability foundation for the Python Reliability Automation phase of the project.

---

## Project Status

Completed:

- Phase 1 Planning
- Phase 2 GitHub Structure
- Phase 3 Flask Application
- Phase 4 Dockerization
- Phase 5 Minikube
- Phase 6 Kubernetes Deployment
- Phase 7 Kustomize Overlays
- Phase 8 Terraform AKS/EKS
- Phase 9 ArgoCD GitOps
- Phase 10 Monitoring

Next:

- Phase 11 Python Reliability Automation
