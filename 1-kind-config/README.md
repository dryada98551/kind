# kind create

### 創建一個 Ubuntu 22.04 的虛擬機

### 更新系統並安裝 Docker

```bash

sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker

```

**說明**：這一步安裝並啟動 Docker，使得虛擬機能夠運行容器。

### 增加 inotify 設定

### 編輯 `/etc/sysctl.conf` 文件

```bash

sudo vi /etc/sysctl.conf
```

在文件末尾添加以下內容：

```

fs.inotify.max_user_watches = 524288
fs.inotify.max_user_instances = 512

```

### 應用新的設定

```bash
sudo sysctl -p
```

### 安裝 Kind

```bash
# amd
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
# arm
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

**說明**：這一步下載並安裝 Kind 工具，用於在本地創建和管理 Kubernetes 集群。

### 安裝 kubectl

```bash
sudo snap install kubectl --classic
```

**說明**：這一步安裝 `kubectl`，Kubernetes 的命令行工具，用於與集群進行交互。

### 將使用者添加到 Docker 組

```bash
sudo groupadd docker
sudo usermod -aG docker ${USER}
sudo chown -fR ${USER} ~/.kube
newgrp docker

```

**說明**：將 `jeffhe` 使用者添加到 `docker` 組，以便能夠在不使用 `sudo` 的情況下運行 Docker 命令。更改 `~/.kube` 目錄的所有權，以確保使用者能夠訪問 Kubernetes 配置文件。

### 創建 Kind 配置文件

創建一個名為 `kind-config.yaml` 的文件

**說明**：這個配置文件定義了 Kind 集群的結構，包括 3 個控制平面節點和 2 個工作節點。

### 創建集群並檢查集群信息和節點狀態

```bash

kind create cluster --config kind-config.yaml
kind delete cluster --name kind
kubectl cluster-info --context kind-kind
kubectl get nodes

kubectl label nodes kind-worker disktype=ssd
kubectl get nodes --show-labels

```

**說明**：這些步驟使用 Kind 工具根據配置文件創建 Kubernetes 集群，並檢查集群信息和節點狀態。

![Untitled](../img/img.jpg)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/81c758a8-650d-4bbb-899e-ece50bd38dd6/44d804d7-75b4-4949-8131-af6ed04efd4c/Untitled.png)

### 檢查容器內狀態

在 Kind 工作節點內部檢查 `kubelet` 日誌：

```bash
journalctl -u kubelet -f
```

---

通過以上步驟，你將成功在 Ubuntu 22.04 虛擬機上創建一個包含 3 個控制平面節點和 2 個工作節點的多節點 Kind 集群，並且不需要使用 `sudo` 來運行 `kind` 和 `docker` 命令。如果有任何問題或需要進一步的幫助，請隨時告訴我。

### **創建 Docker Hub secret**

**創建 Docker Hub secret**：

首先，您需要創建一個 Kubernetes secret 來存儲您的 Docker Hub 憑證。您可以使用 `kubectl create secret docker-registry` 命令來創建它：

```bash
kubectl create secret docker-registry my-dockerhub-secret \
  --docker-username=dryada98551 \
  --docker-password=passwd
```

### 安装 Metrics Server

安裝Metrics Server

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

驗證安裝

```bash
kubectl get deployment metrics-server -n kube-system
```

修改 Metrics Server 部署配置

編輯Metrics Server 部署配置

```bash
kubectl edit deployment metrics-server -n kube-system
```

在 `spec.template.spec.containers.args` 部分添加 `--kubelet-insecure-tls` 参数：

```yaml
spec:
  containers:
  - args:
    - --cert-dir=/tmp
    - --secure-port=443
    - --kubelet-insecure-tls
    image: registry.k8s.io/metrics-server/metrics-server:v0.7.1
    name: metrics-server

```
