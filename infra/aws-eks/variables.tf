variable "region" {
  description = "AWS region for EKS resources"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "Name of the EKS cluster"
  type        = string
  default     = "eks-k8s-gitops-platform"
}

variable "cluster_version" {
  description = "Kubernetes version for EKS cluster"
  type        = string
  default     = "1.30"
}

variable "vpc_id" {
  description = "Existing VPC ID for EKS deployment"
  type        = string
}

variable "subnet_ids" {
  description = "Existing subnet IDs for EKS worker nodes"
  type        = list(string)
}

variable "node_instance_type" {
  description = "EC2 instance type for EKS worker nodes"
  type        = string
  default     = "t3.small"
}
