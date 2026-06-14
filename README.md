# AWS EKS Kubernetes — Containerized Flask App

Flask CRUD app containerized with Docker and deployed on AWS EKS (Elastic Kubernetes Service).

## Architecture
Browser → EKS LoadBalancer → Kubernetes Pods (Docker) → RDS PostgreSQL

## AWS Services Used
- **EKS** — Managed Kubernetes cluster
- **ECR** — Container registry for Docker image
- **RDS** — PostgreSQL database
- **Docker** — App containerization
- **kubectl** — Kubernetes CLI
- **eksctl** — EKS cluster management

## What the App Does
- Add student records (name + score)
- View all records from RDS PostgreSQL
- Delete records
- Runs as 2 replica pods for high availability

## Key Files
- `app.py` — Flask application
- `Dockerfile` — Container build instructions
- `deployment.yaml` — Kubernetes Deployment + Service manifest
- `requirements.txt` — Python dependencies

## Deployment Steps
1. Build Docker image on EC2
2. Push to ECR
3. Create EKS cluster with eksctl
4. Deploy with kubectl apply -f deployment.yaml

## Resume Keywords
Docker, Kubernetes, EKS, ECR, kubectl, eksctl, Flask, RDS PostgreSQL
