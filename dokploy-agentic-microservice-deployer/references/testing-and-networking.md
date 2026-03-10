# Testing and Networking

## Estado final esperado

El estado final por defecto es:

- aplicacion desplegada
- sin dominio publico permanente
- acceso desde n8n por `http://<appName>:8000`

Obtiene `appName` con `application-one`. Ese valor es el host interno, no el nombre visible.

## Prueba preferida: dominio temporal

Cuando necesites probar desde fuera de la red interna:

1. genera un host con `domain-generateDomain`
2. crea el dominio con `domain-create`
3. ejecuta tests HTTP reales
4. elimina el dominio con `domain-delete`

Configuracion recomendada para el dominio temporal:

- `domainType`: `application`
- `applicationId`: la app actual
- `host`: el host generado
- `https`: `false`
- `certificateType`: `none`
- `port`: `8000`
- `stripPath`: `false`

Si el usuario quiere HTTPS incluso para la prueba, cambia `https` y `certificateType` segun su infraestructura.

## Tests minimos

Siempre corre:

1. `GET /health`
2. un endpoint de negocio con payload real

Valida:

- `200` o el codigo esperado
- forma del JSON
- presencia de autenticacion cuando aplique
- ausencia de errores en monitoreo de Dokploy

## Limpieza despues del test

Si abriste un dominio temporal:

1. guarda el `domainId`
2. ejecuta `domain-delete`
3. confirma con `domain-byApplicationId` que no quedaron dominios residuales

No cierres el trabajo dejando un dominio publico temporal colgado.

## Fallback cuando no puedas abrir dominio temporal

Si no puedes generar o crear un dominio temporal:

- revisa `application-readAppMonitoring`
- confirma que la app levanta y escucha bien
- pide una unica prueba dentro de n8n o desde otro servicio en la misma red

En ese caso entrega el comando o la configuracion exacta para el nodo HTTP Request de n8n usando `http://<appName>:8000`.

## Casos de borde

- Si n8n corre fuera de Dokploy o fuera de la misma red Docker, `appName` no resolvera.
- Si el servicio no escucha en `0.0.0.0`, la app puede parecer sana pero no responder a otros contenedores.
- Si usas `X-API-Key`, prueba una llamada valida y una invalida.
- Si el usuario pide exposicion publica permanente, eso ya no es un flujo interno-only y debes tratarlo como un requisito adicional.
