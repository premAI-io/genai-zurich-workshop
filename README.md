# GenAI Zurich Workshop

## Build a RAG with Prem Platform

> Currently the platform is not open-source, but we plan to release it open-source in the future.

1. Upload the documents in a Prem Repository
2. Test the Assistant from the Lab
3. Launch the Best Model and configurations
4. Integrate Prem in your Product with our official SDKs

## Deploy a Model in your Infrastructure with Prem Operator 

1. Clone the prem-operator repository

```bash
git clone git@github.com:premAI-io/prem-operator.git
```

2. Create a cluster with Kind

> Depending on your operating system you can install kind in different ways. Learn more here: https://kind.sigs.k8s.io/docs/user/quick-start/#installing-with-a-package-manager. If you have a Mac, you can simply run `brew install kind`

```bash
kind create cluster --name genai-zurich
```

3. Check if the cluster has been created and configure the default context

```bash
kind get clusters
kubectl cluster-info --context kind-genai-zurich
```

4. Install Prem Operator

```bash
helm install latest oci://registry-1.docker.io/premai/prem-operator-chart
```

5. Deploy the Phi-2 + Elia CPU example and exec Elia in a terminal session

```bash
cd ./prem-operator
kubectl apply -f examples/elia-tui-cpu.yaml
kubectl exec -it deployments/elia elia
```

6. Delete the cluster when you are done experimenting

```bash
kind delete cluster --name kind-genai-zurich 
```

## Build a RAG with Prem 1B Chat

> PLACEHOLDER FOR ROHIT