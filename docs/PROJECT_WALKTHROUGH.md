# Project Walkthrough

## Project Name

Terraform-Driven Multi-Cloud Kubernetes Reliability & GitOps Platform

## Project Goal

Build a production-inspired platform that demonstrates Kubernetes, GitOps, infrastructure as code, monitoring, and reliability automation using modern DevOps tooling.

## Technologies Used

- Terraform
- AKS
- EKS
- Kubernetes
- Docker
- Flask
- Kustomize
- ArgoCD
- Prometheus
- Grafana
- Python
- GitHub

## Completed Phases

### Phase 1: Planning

Defined the project goal, target architecture, technology stack, and implementation phases.

### Phase 2: GitHub Structure

Created the repository structure for application code, Kubernetes manifests, Terraform, GitOps configuration, monitoring, automation, and documentation.

### Phase 3: Flask Application

Built a lightweight Flask application to serve as the deployable workload.

### Phase 4: Docker

Containerized the Flask application using Docker.

### Phase 5: Minikube

Used Minikube as the local Kubernetes development environment.

### Phase 6: Kubernetes Deployment

Created Kubernetes manifests to deploy and expose the Flask application.

### Phase 7: Kustomize Overlays

Added Kustomize overlays to support environment-based Kubernetes configuration.

### Phase 8: Terraform AKS/EKS

Added Terraform structure for both Azure AKS and AWS EKS infrastructure.

### Phase 9: ArgoCD GitOps

Implemented ArgoCD to manage Kubernetes application deployment from GitHub.

### Phase 10: Monitoring

Installed lightweight Prometheus and Grafana deployments to provide observability without overloading the local machine.

### Phase 11: Python Reliability Automation

Created a Python reliability script that checks Kubernetes pods and deployments, generates a JSON report, and exits with a failure code when unhealthy workloads are detected.

## Monitoring Validation

Prometheus and Grafana were deployed into the `monitoring` namespace.

Validation commands:

```bash
kubectl get pods -n monitoring
kubectl get svc -n monitoring
```

Grafana was connected to Prometheus using the internal Kubernetes service URL:

```text
http://prometheus-server.monitoring.svc.cluster.local
```

A basic Prometheus query was tested:

```promql
up
```

## Reliability Automation Validation

The reliability automation script is located at:

```text
automation/k8s_reliability_check.py
```

Run the script:

```bash
python3 automation/k8s_reliability_check.py
```

The script generates:

```text
reliability_report.json
```

The report includes:

- Checked namespaces
- Pod health
- Deployment readiness
- Restart counts
- Overall health status

## Screenshots

Screenshots are stored in:

```text
docs/screenshots/
```

Recommended screenshots:

- `architecture-diagram.png`
- `argocd-dashboard.png`
- `grafana-dashboard.png`
- `prometheus-query.png`
- `reliability-report.png`
- `k8s-pods.png`

## Project Outcome

This project demonstrates the ability to design, deploy, monitor, and validate a Kubernetes-based platform using real-world DevOps practices.

Key outcomes:

- Infrastructure-as-code structure for AKS and EKS
- GitOps delivery with ArgoCD
- Kubernetes deployment with Kustomize overlays
- Lightweight observability using Prometheus and Grafana
- Python-based reliability automation
- Portfolio-ready documentation and screenshots
