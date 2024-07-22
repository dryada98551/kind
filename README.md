# kind

## 作業說明

### 1. 使用kind架設Kubernetes叢集

請以[kind](https://kind.sigs.k8s.io/)架設一個包含3個control-plane節點和2個worker節點的Kubernetes叢集。

### 2. 安裝監控工具

在kind的叢集中安裝以下監控工具：

- Prometheus
- Node Exporter
- Kube-State-Metrics

Prometheus將收集Node Exporter和Kube-State-Metrics的效能數據。


### 3. 安裝Grafana

在kind叢集外安裝Grafana，可以使用Docker或Podman進行部署。設定Grafana的Data Source指向Prometheus，並建立以下兩個效能監控儀表板：

#### 3.1 效能監控儀表板(1)

顯示Node的效能監控數據。


#### 3.2 效能監控儀表板(2)

顯示kind叢集的效能監控數據。


#### 3.3 效能監控儀表板說明

請詳細說明以上兩個效能監控儀表板的每個Panel內容。


#### 3.4 觀察CPU Throttling

請說明如何透過建立的監控儀表板觀察CPU Throttling現象。

### 4. 部署容器應用程式

在kind叢集中部署一個容器應用程式，並建立一個HPA (Horizontal Pod Autoscaler)物件，以CPU使用率達到50%為條件，最多擴充到10個Pod。

### 提交方式

將以上操作的方法、使用到的配置檔(yaml, helm等)、說明檔（以Markdown格式呈現圖、內容）上傳到GitHub，並於下週二（7/23）早上9:00前將GitHub網址提交。

