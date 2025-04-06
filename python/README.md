# Projeto Final - OpenShift

Esta aplicação foi desenvolvida para ser construída e executada diretamente no OpenShift usando Source-to-Image (s2i).

## Como usar no OpenShift

### Criar a aplicação via linha de comando:

```bash
oc new-app python:3.9~https://github.com/SEU_USUARIO/openshift-final-project.git
```

### Expor a aplicação:

```bash
oc expose svc/openshift-final-project
```

### Acessar no navegador:

```bash
echo "http://$(oc get route openshift-final-project -o jsonpath='{.spec.host}')"
```

---

Desenvolvido para o projeto final da disciplina de OpenShift.
