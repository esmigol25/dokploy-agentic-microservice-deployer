# Provider Matrix

## Preferencia por defecto

Prefiere repositorios privados para las apps del usuario. Si Dokploy no tiene una credencial Git privada lista y el usuario no quiere configurarla ahora, permite repo publico como alternativa.

## Opcion 1: Repo publico con provider Git generico

Usa `application-saveGitProvider` con:

- `customGitUrl`: `https://github.com/<owner>/<repo>.git`
- `customGitBranch`: rama objetivo, normalmente `main`
- `customGitBuildPath`: `/`
- `enableSubmodules`: `false` salvo que el repo los use

Este es el camino mas simple cuando el repo de la app es publico.

## Opcion 2: Repo privado con provider Git generico

Usa `application-saveGitProvider` con:

- `customGitUrl`: `git@github.com:<owner>/<repo>.git`
- `customGitBranch`: normalmente `main`
- `customGitBuildPath`: `/`
- `customGitSSHKeyId`: identificador de la SSH key ya cargada en Dokploy
- `enableSubmodules`: `false` salvo necesidad real

No inventes `customGitSSHKeyId`. Si no lo tienes, pidelo al usuario o cambia temporalmente a repo publico.

## Opcion 3: GitHub provider nativo de Dokploy

Usa `application-saveGithubProvider` solo si el usuario ya conoce o te da:

- `githubId`
- `owner`
- `repository`
- `branch`

Este flujo evita manejar URL Git manual, pero depende de una integracion GitHub ya configurada en Dokploy. Si ese `githubId` no esta disponible, vuelve al provider Git generico.

## Regla de decision

1. Si el usuario ya tiene integracion GitHub de Dokploy y conoce `githubId`, usa `application-saveGithubProvider`.
2. Si el repo de la app sera privado y hay SSH key en Dokploy, usa `application-saveGitProvider` con SSH.
3. Si el usuario prioriza velocidad o no hay SSH key lista, usa repo publico + `application-saveGitProvider` por HTTPS.

## Notas practicas

- Mantene `customGitBuildPath` en `/` salvo que el Dockerfile viva en una subcarpeta.
- Si el repo cambia de publico a privado despues, actualiza el provider antes de redeployar.
- Si Dokploy queda apuntando a una URL Git incorrecta, el deploy fallara antes del build. Revisa provider antes de tocar Dockerfile o env vars.
