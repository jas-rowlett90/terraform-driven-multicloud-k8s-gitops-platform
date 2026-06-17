# Architecture

## Overview

This project is a production-inspired Kubernetes reliability and GitOps platform built to demonstrate infrastructure provisioning, declarative application delivery, observability, and reliability automation across a multi-cloud design.

The platform uses Terraform for cloud infrastructure, Kubernetes for container orchestration, Kustomize for environment overlays, ArgoCD for GitOps delivery, Prometheus and Grafana for monitoring, and Python automation for reliability validation.

## Architecture Diagram

![Architecture Diagram](screenshots/architecture-diagram.png)

## Platform Flow

1. Application code is stored in GitHub.
2. Docker is used to containerize the Flask application.
3. Kubernetes manifests define the application deployment and service.
4. Kustomize overlays manage environment-specific configuration.
5. ArgoCD watches the Git repository and reconciles Kubernetes state.
6. Terraform folders define AKS and EKS infrastructure.
7. Prometheus collects cluster and workload metrics.
8. Grafana visualizes metrics from Prometheus.
9. Python automation validates cluster reliability and generates a JSON health report.

## Core Components

### Flask Application

A lightweight Flask app serves as the workload deployed into Kubernetes.

### Kubernetes

Kubernetes provides orchestration for the application, monitoring tools, and GitOps-managed resources.

### Kustomize

Kustomize supports reusable Kubernetes manifests with overlays for environment-specific deployment configuration.

### ArgoCD

ArgoCD implements GitOps by continuously comparing the desired state in GitHub with the live Kubernetes cluster state.

### Terraform

Terraform provides infrastructure-as-code structure for both AKS and EKS environments.

### Prometheus

Prometheus provides metrics collection for the Kubernetes environment.

### Grafana

Grafana connects to Prometheus and provides dashboard-based visualization.

### Python Reliability Automation

A Python script checks Kubernetes pod and deployment health, detects reliability issues, writes a JSON report, and returns a non-zero exit code when unhealthy resources are found.

## Design Decisions

### Lightweight Monitoring

This project uses standalone lightweight Prometheus and Grafana Helm deployments instead of kube-prometheus-stack because the local development environment has limited resources.

### Separate AKS and EKS Terraform Folders

The AKS and EKS Terraform configurations are separated to show multi-cloud infrastructure design while keeping each cloud provider's configuration clear and maintainable.

### GitOps-Driven Delivery

ArgoCD was selected to demonstrate declarative deployment, drift detection, and continuous reconciliation from GitHub to Kubernetes.

## Reliability Layer

The reliability layer includes:

- Prometheus metrics collection
- Grafana visualization
- Python health checks
- JSON reliability reporting
- Kubernetes pod and deployment validation

Together, these components demonstrate how platform teams can monitor workloads and automate operational checks.
