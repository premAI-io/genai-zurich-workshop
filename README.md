# GenAI Zurich Workshop

## Build a RAG with Prem Platform

> Currently the platform is not open-source, but we plan to release it open-source in the future.

1. Upload the documents in a Prem Repository
2. Test the Assistant from the Lab
3. Launch the Best Model and configurations
4. Integrate Prem in your Product with our official SDKs

We prepared a script in order to interact with the assistant we created through Prem Platform.

```bash
cd ./rag_demo
python chat_saas.py
```

## Deploy a Model in your Infrastructure with Prem Operator

0. Create a Paperspace instance, install Kubernetes (K3s) and various utilities

> You can install the utilities (k3sup, kubectl, helm, etc.) on your local machine if you prefer.
> Below we show installing everything on the remote machine while logged in via SSH

```bash
# Install k3sup
curl -sLS https://get.k3sup.dev | sh
sudo install k3sup /usr/local/bin

# Install k3s
# NOTE: Replace --local with the --ip/--host to install k3s remotely
k3sup install --local --local-path $HOME/.kube/config

# Install kubectl
sudo apt update
sudo snap install kubectl --classic
kubectl version --client

# Check the cluster is configured
kubectl get nodes
# NOTE: if this doesn't return a node, you can also try the following
sudo k3s kubectl get nodes

# Install Helm
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod +x get_helm.sh
./get_helm.sh
helm version

# Optionally install k9s as a TUI alternative to kubectl
curl -OL https://github.com/derailed/k9s/releases/download/v0.32.4/k9s_linux_amd64.deb
sudo apt install ./k9s_linux_amd64.deb
```

1. [Install the NVIDIA Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html)

```bash

# Remove any pre-installed NVIDIA drivers and container runtime
sudo apt purge cuda-*
sudo apt purge nvidia-*
sudo apt autoremove
sudo apt autoclean

# Downgrade the Linux kernel because of https://forums.developer.nvidia.com/t/nvidia-modeset-unknown-symbol-on-module-load-error/239848
sudo apt install linux-image-5.15.0-107-generic
sudo apt remove linux-image-generic-hwe-22.04
sudo apt remove linux-image-6.2.0-37-generic
# Reboot to load the new kernel
sudo systemctl reboot

# Install the NVIDIA operator
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
helm repo update
helm install --wait --generate-name -n gpu-operator --create-namespace --set driver.version=550-5.15.0-107 --set driver.usePrecompiled=true nvidia/gpu-operator

# wait for the driver to be installed, this is where k9s is useful...
# if the NVIDIA pods for the driver and runtime succeed, but the other pods are stuck in init then restart
sudo systemctl reboot
```

2. Clone the prem-operator repository

```bash
git clone https://github.com/premAI-io/prem-operator.git
```

3. Install Prem Operator

```bash
helm install latest oci://registry-1.docker.io/premai/prem-operator-chart
```

4. Deploy the Phi-2 + Elia CPU example and exec Elia in a terminal session

```bash
cd ./prem-operator
kubectl apply -f examples/llama3-8b-gguf.yaml
# Grab a coffee while the container downloads
kubectl exec -it deployments/llama-3-tui -- elia
# Type a message and wait a little more for the model to load
```

5. Remove the example deployment and Prem Operator

```bash
kubectl delete aideployment/llama-3-8b-gguf
kubectl delete aimodelmap/llama-3-8b-gguf
kubectl delete deployment/llama-3-cli
kubectl delete deployment/llama-3-tui
helm uninstall latest
```

## Build a RAG with Prem 1B Chat

1. Go to rag_demo folder

```bash
cd rag_demo
```

2. Install the requirements:

```bash
pip install -r requirements.txt
```

3. Start jupyter lab and run the noteboook:

```bash
jupyter lab --allow-root
```

## Some questions to try out

- What is the key feature of ChatEval compared to the other evaluation strategies?

> ChatEval is a **multi-agent system** employed for evaluation of LLMs

- What is the key results obtained by Prometheus 2, regarding the evaluation of LLMs?

> On four direct assessment benchmarks and four pairwise ranking benchmarks, PROMETHEUS 2 scores the highest correlation and agreement with humans and proprietary LM judges among all tested open evaluator LMs. 

- How does the Infini-attention technique aim to address the problem related to limited context in generative models?

> The Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block.
