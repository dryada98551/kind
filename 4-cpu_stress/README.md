# 驗證 HPA (Horizontal Pod Autoscaler)

## 作業說明

### 在 Kubernetes 中驗證 HPA，可以按照以下步驟操作：

### 1. 建立高 CPU 使用的 Image
首先，創建一個 Python 腳本`cpu_stress.py`來產生高 CPU的程式，接著，創建一個 Dockerfile 來構建映像
### 構建和推送 Docker 映像
使用以下命令來構建並推送 Docker 映像：

```bash
docker build -t your_dockerhub_username/cpu-stress:latest .
docker push your_dockerhub_username/cpu-stress:latest
```

### 2. 部署 Pod 和 HPA

### 使用 Helm 部署
使用 Helm 來部署 Pod 和 HPA。首先，創建一個 Helm chart 或使用現有的 Helm chart 來部署應用
### 部署命令
使用以下命令來部署應用和 HPA：

```bash
cd helm
helm upgrade --install myapp -f values.yaml .
```

### 驗證 HPA
使用以下命令來檢查 HPA 狀態：

```bash
kubectl get hpa
```
這會顯示當前集群中所有 HPA 的狀態，包括目標和當前副本數