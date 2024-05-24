# GenAI Zurich Workshop

## Build a RAG with Prem Platform

> Currently the platform is not open-source, but we plan to release it open-source in the future.

1. Upload the documents in a Prem Repository
2. Test the Assistant from the Lab
3. Launch the Best Model and configurations
4. Integrate Prem in your Product with our official SDKs

## Deploy a Model in your Infrastructure with Prem Operator 

0. Create a Paperspace instance and Install `kind` and `kubectl`

```bash
# Install kubectl
sudo apt update
sudo snap install kubectl --classic
kubectl version --client

# Install kind
# For AMD64 / x86_64
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-amd64
# For ARM64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# Install Helm
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod +x get_helm.sh
./get_helm.sh
helm version
```

1. Clone the prem-operator repository

```bash
git clone https://github.com/premAI-io/prem-operator.git
```

2. Create a cluster with Kind

```bash
kind create cluster --name genai-zurich
```

2. Check if the cluster has been created and configure the default context

```bash
kind get clusters
kubectl cluster-info --context kind-genai-zurich
```

3. Install Prem Operator

```bash
helm install latest oci://registry-1.docker.io/premai/prem-operator-chart
```

4. Deploy the Phi-2 + Elia CPU example and exec Elia in a terminal session

```bash
cd ./prem-operator
kubectl apply -f examples/elia-tui.yaml
kubectl exec -it deployments/elia elia
```

5. Delete the cluster when you are done experimenting

```bash
kind delete cluster --name kind-genai-zurich 
```

## Build a RAG with Prem 1B Chat

> PLACEHOLDER FOR ROHIT