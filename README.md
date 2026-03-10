# dokploy-agentic-microservice-deployer

Dokploy-first Codex skill for turning local automations into internal FastAPI microservices that n8n can call over the Dokploy network.

## Que incluye

Este repositorio publico solo contiene la skill reutilizable:

- `dokploy-agentic-microservice-deployer/`
  - `SKILL.md`
  - `agents/openai.yaml`
  - `references/`
  - `assets/fastapi-template/`

La skill esta pensada para trabajar con GitHub MCP + Dokploy MCP. No trae wrappers Python para las APIs.

## Instalar con skill-installer

Desde Codex, usa `$skill-installer` apuntando a este repo y al path `dokploy-agentic-microservice-deployer`.

Comando equivalente con el script del instalador:

```bash
python "$CODEX_HOME/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo esmigol25/dokploy-agentic-microservice-deployer \
  --path dokploy-agentic-microservice-deployer \
  --dest /ruta/a/skills
```

Ejemplo para este workspace:

```powershell
python "C:\Users\esmig\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo esmigol25/dokploy-agentic-microservice-deployer `
  --path dokploy-agentic-microservice-deployer `
  --dest "C:\Users\esmig\Downloads\n8n Onboarding\.agent\skills"
```

## Diferencia entre este repo y los repos de apps

Este repo es publico porque solo almacena la skill y el template reusable.

Los repositorios de aplicacion que la skill cree para cada microservicio pueden quedar:

- privados, que es la preferencia por defecto
- publicos, si el usuario prioriza una configuracion Dokploy mas simple

## Enfoque

- Dokploy-first
- MCP-native
- FastAPI + Dockerfile + puerto `8000`
- estado final interno por defecto, sin dominio publico permanente
- autenticacion opcional con `X-API-Key`, activada por defecto si el usuario no decide otra cosa

## Inspiracion

Inspirado en el flujo de `kevinrivm/agentic-microservice-deployer`:

- https://github.com/kevinrivm/agentic-microservice-deployer

La implementacion de esta version fue reescrita para Dokploy y para uso directo con MCP.
