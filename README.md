# Book Catalog API – CI/CD & Kubernetes Deployment

## 📖 Project Overview

This project implements a **Django REST API** for managing a book catalog.  
It includes:

- **CRUD endpoints** for books
- **Book model** with:
  - `title`
  - `author`
  - `isbn`
  - `published_date`
  - `created_at`
- **Validation** via Django REST Framework serializers

- **Automated CI/CD** pipeline using GitHub Actions:
  - Build
  - Test (pytest)
  - Dockerize
  - Push to registry
  - Deploy to Kubernetes via ArgoCD
- **Kubernetes deployment** using a custom Helm chart

The project is designed for both **local development** (using Docker Compose) and **production** in Kubernetes.

---

## 📌 API Usage Examples

Base URL for local dev:
```
http://localhost:8000/api/books/
```

Base URL for production:
```
http://localhost:8081/api/books/
```

### 1️⃣ List all books
```bash
curl -X GET http://localhost:8000/api/books/
```

### 2️⃣ Create a new book
```bash
curl -X POST http://localhost:8000/api/books/   -H "Content-Type: application/json"   -d '{
    "title": "Django Unleashed",
    "author": "Andrew Pinkham",
    "isbn": "9780134177280",
    "published_date": "2024-01-01"
  }'
```

### 3️⃣ Get a book by ID
```bash
curl -X GET http://localhost:8000/api/books/1/
```

### 4️⃣ Update a book (PUT)
```bash
curl -X PUT http://localhost:8000/api/books/1/   -H "Content-Type: application/json"   -d '{
    "title": "Django Updated",
    "author": "Jane Doe",
    "isbn": "9781234567897",
    "published_date": "2024-06-01"
  }'
```

### 5️⃣ Delete a book
```bash
curl -X DELETE http://localhost:8000/api/books/1/
```

---

## 💻 Local Build and Run Instructions

### Prerequisites
- Docker & Docker Compose installed
- Python 3.13+ (only if running locally without Docker)

### Steps
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-dir>
   ```

2. Start services:
   ```bash
   docker-compose up --build
   ```

3. Access the API:
   - API: [http://localhost:8000/api/books/](http://localhost:8000/api/books/)
   - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

4. Run migrations manually (optional – `entrypoint.sh` does this automatically):
   ```bash
   docker-compose exec app python manage.py migrate
   ```

---

## ⚙️ CI/CD Pipeline Explanation

The **GitHub Actions** workflow:

1. **Trigger**:
   - On pushes to `main`
   - On pull requests

2. **Steps**:
   - Checkout code
   - Install Python dependencies
   - Run Django checks and tests
   - Build Docker image
   - Push to GitHub Container Registry (GHCR)
   - Deploy to Kubernetes using Helm/ArgoCD

3. **Secrets/Inputs**:
   - `GITHUB_TOKEN` – for pushing to GHCR
   - `KUBECONFIG_B64` – base64 encoded kubeconfig for deployment
   - `K8S_NAMESPACE` – namespace for deployment

---

## ☸ Kubernetes & Helm Setup Instructions

### 1️⃣ Prerequisites
- Kubernetes cluster (local or cloud)
- `kubectl` configured to access the cluster
- `helm` installed

### 2️⃣ Helm Chart Structure
Located in `books-catalog-chart/`:
- **Deployment** – Runs the Django app
- **Service** – Exposes it internally
- **Ingress** – (Optional) routes external traffic
- **ConfigMap/Secret** – Holds environment variables
- **Migration Job** – Runs `python manage.py migrate` on install/upgrade

### 3️⃣ Deployment Steps
1. Deploy postgres from OCI repository using custom `values.yaml` (for username, password, db):
   ```bash
   helm install books-postgres oci://registry-1.docker.io/bitnamicharts/postgresql -f ./postgres/values.yaml
   ```

2. Deploy tha app:
   ```bash
   helm install bookcatalog ./books-catalog-chart
   ```

2. Verify pods:
   ```bash
   kubectl get pods
   ```

3. Access the API:
   - If Ingress is enabled, visit `http://<host>/api/books/`
   - If not, use `kubectl port-forward`:
     ```bash
     kubectl port-forward svc/bookcatalog 8000:8000 -n namespace
     ```

---

## 📜 License
MIT License – you are free to use, modify, and distribute this project.

---

## ✍️ Author
Vadym Tymeichuk – 2025
