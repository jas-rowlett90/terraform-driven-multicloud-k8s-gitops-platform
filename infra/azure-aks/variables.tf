variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "rg-k8s-gitops-platform"
}

variable "location" {
  description = "Azure region for AKS resources"
  type        = string
  default     = "eastus"
}

variable "cluster_name" {
  description = "Name of the AKS cluster"
  type        = string
  default     = "aks-k8s-gitops-platform"
}

variable "dns_prefix" {
  description = "DNS prefix for the AKS cluster"
  type        = string
  default     = "k8sgitops"
}

variable "node_count" {
  description = "Number of AKS worker nodes"
  type        = number
  default     = 1
}

variable "node_vm_size" {
  description = "VM size for AKS worker nodes"
  type        = string
  default     = "Standard_B2s"
}
