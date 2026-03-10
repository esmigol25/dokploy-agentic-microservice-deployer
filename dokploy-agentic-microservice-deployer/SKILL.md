---
name: dokploy-agentic-microservice-deployer
description: Despliega automatizaciones y agentes como microservicios FastAPI internos en Dokploy para ser consumidos desde n8n por red interna. Usa este skill cuando Codex necesite convertir codigo local en un servicio desplegable, crear o actualizar el repo de la app en GitHub, configurar el provider Git en Dokploy, guardar variables de entorno, lanzar el deploy, verificar salud, o dejar lista la URL interna `http://appName:8000`. Tambien aplica cuando el usuario pida "publica este agente", "sube este servicio a Dokploy", "haz que n8n lo llame por red interna", o "crea el microservicio y dejalo desplegado".
---

# Dokploy Agentic Microservice Deployer

Convierte codigo local en un microservicio interno para Dokploy y dejalo listo para que n8n lo consuma por red interna. Prioriza GitHub MCP y Dokploy MCP; no reimplementes estas APIs con scripts locales.

## Flujo rapido

1. Pide datos de prueba reales y la respuesta esperada antes de cerrar el contrato del servicio.
2. Decide con el usuario si el repo de la app sera privado o publico.
3. Decide si el servicio llevara `X-API-Key`; si el usuario no responde, dejalo activado.
4. Si no existe una base de servicio, parte de `assets/fastapi-template/` y reescribe sus placeholders.
5. Publica el repo de la app con GitHub MCP.
6. Descubre el entorno destino con `project-all`, crea la aplicacion con `application-create`, y sigue [references/deployment-workflow.md](references/deployment-workflow.md).
7. Deja el estado final sin dominio publico salvo que el usuario lo pida explicitamente. El endpoint esperado para n8n es `http://<appName>:8000`.

## Datos que debes congelar primero

- Un ejemplo real de cada payload de entrada
- La salida esperada para ese payload
- Los endpoints que se van a exponer
- Las variables de entorno de negocio
- El nombre deseado del servicio y del repo
- Si n8n vivira en la misma red de Dokploy o necesitara acceso publico

No cierres el deploy solo con descripciones vagas. Congela al menos un caso feliz y un caso dificil.

## Como estructurar la aplicacion

- Reusa `assets/fastapi-template/` cuando el usuario aun no tenga una base de servicio.
- Reemplaza el endpoint de ejemplo por endpoints reales, modelos reales y logica real.
- Reescribe `directives/README.md` con:
  - descripcion funcional
  - endpoints
  - variables de entorno
  - ejemplos de llamadas desde n8n
- Manten `GET /health` retornando `200`.
- Mantene el puerto `8000` salvo que el usuario pida otra cosa y Dokploy quede configurado igual.

## Reglas operativas

- Usa GitHub MCP para crear o actualizar el repo de la app.
- Usa Dokploy MCP para crear la aplicacion, configurar provider, build, entorno y deploy.
- Prefiere repos de aplicacion privados. Si el usuario no quiere configurar acceso Git privado en Dokploy, permite repo publico como alternativa.
- No dejes un dominio permanente por defecto.
- Si necesitas un dominio temporal para testear desde fuera de la red interna, sigue [references/testing-and-networking.md](references/testing-and-networking.md) y luego eliminalo.
- Si `application-saveGithubProvider` requiere un `githubId` que no tienes, no lo inventes. Usa el flujo generico de Git descrito en [references/provider-matrix.md](references/provider-matrix.md) o pide ese identificador al usuario.

## Orden recomendado

1. Congela contrato, payloads y criterio de exito.
2. Prepara o adapta el repo de la app.
3. Publica el repo con GitHub MCP.
4. Descubre el entorno de Dokploy y crea la aplicacion.
5. Configura provider, build Dockerfile y variables.
6. Despliega y verifica monitoreo.
7. Ejecuta pruebas externas temporales o una prueba desde n8n.
8. Entrega al usuario la URL interna final y la documentacion de uso.

## Referencias de apoyo

- Flujo de despliegue completo: [references/deployment-workflow.md](references/deployment-workflow.md)
- Matriz de providers Git/GitHub: [references/provider-matrix.md](references/provider-matrix.md)
- Red interna, dominios temporales y tests: [references/testing-and-networking.md](references/testing-and-networking.md)

## Asset principal

Usa `assets/fastapi-template/` como punto de partida cuando el usuario necesite un microservicio nuevo. No copies el template a ciegas: reescribe nombres, modelos, endpoints, mensajes y la documentacion interna para que coincidan con el caso real.
