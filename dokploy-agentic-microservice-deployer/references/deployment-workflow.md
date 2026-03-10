# Deployment Workflow

## Resumen

Usa este flujo cuando vayas a convertir codigo local en una aplicacion real de Dokploy. La secuencia preferida es GitHub MCP para el repo y Dokploy MCP para el runtime.

## Inputs obligatorios

- nombre del servicio
- descripcion breve
- payloads reales de prueba
- resultado esperado
- variables de entorno
- entorno destino de Dokploy
- decision de autenticacion `X-API-Key`
- decision de privacidad del repo de la app

## 1. Preparar el repo de la app

Si el usuario ya tiene repo, inspeccionalo y adapta su estructura. Si no existe:

1. crea el repo con GitHub MCP
2. usa `assets/fastapi-template/` como base si el servicio es nuevo
3. reescribe `main.py`, `requirements.txt`, `Dockerfile`, `.env.example` y `directives/README.md`
4. publica los archivos con `push_files`

Mantene el repo de la app separado del repo publico de la skill.

## 2. Descubrir el entorno de Dokploy

Usa `project-all` para localizar:

- `projectId`
- `environmentId`
- `serverId` si el usuario quiere forzarlo o existe mas de un servidor

Si ya existe una aplicacion candidata, no dupliques sin confirmar. Revisa primero si conviene actualizarla.

## 3. Crear la aplicacion

Usa `application-create` con:

- `name`: nombre visible
- `appName`: slug DNS interno estable, en minusculas y con guiones
- `environmentId`
- `serverId` solo si hace falta fijarlo

El `appName` es el host interno que luego n8n usara en la forma `http://appName:8000`.

## 4. Configurar el provider Git

Sigue la decision de [provider-matrix.md](provider-matrix.md).

Regla por defecto:

- repo privado: `application-saveGitProvider` con URL SSH y `customGitSSHKeyId`
- repo publico: `application-saveGitProvider` con URL HTTPS
- `application-saveGithubProvider`: solo si el usuario aporta un `githubId` valido de Dokploy

## 5. Configurar build Dockerfile

Usa `application-saveBuildType` con:

- `buildType`: `dockerfile`
- `dockerfile`: `Dockerfile`
- `dockerContextPath`: `/`
- `dockerBuildStage`: `""` salvo que el Dockerfile use una stage nombrada

Si el repo guarda el Dockerfile en otra ruta, ajusta `dockerfile` y `dockerContextPath` juntos.

## 6. Guardar variables de entorno

Usa `application-saveEnvironment`. Pasa `env` como texto multilinea:

```text
SERVICE_API_KEY=...
OPENAI_API_KEY=...
OTRA_VAR=...
```

Incluye `SERVICE_API_KEY` solo si el servicio va a validar `X-API-Key`.

## 7. Desplegar

Usa `application-deploy`. Si estas corrigiendo una app existente, `application-redeploy` tambien es valido.

Despues revisa:

- `application-one`
- `application-readAppMonitoring`

Busca errores de build, restart loops y escucha efectiva en el puerto `8000`.

## 8. Verificar y entregar

Completa al menos:

1. `GET /health`
2. un endpoint de negocio con payload real

Si necesitas exposicion temporal para probar desde fuera, sigue [testing-and-networking.md](testing-and-networking.md). El estado final por defecto es sin dominio publico.

## 9. Entrega final

Entrega al usuario:

- `appName` final
- URL interna para n8n: `http://appName:8000`
- header `X-API-Key` si aplica
- endpoints y payloads
- variables que el usuario aun deba aportar
