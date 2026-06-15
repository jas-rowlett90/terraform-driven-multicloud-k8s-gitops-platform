terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = var.cluster_name
  cluster_version = var.cluster_version

  subnet_ids = var.subnet_ids
  vpc_id     = var.vpc_id

  eks_managed_node_groups = {
    default = {
      min_size     = 1
      max_size     = 2
      desired_size = 1

      instance_types = [var.node_instance_type]
    }
  }

  tags = {
    Environment = "portfolio"
    Project     = "terraform-driven-k8s-gitops-platform"
  }
}
