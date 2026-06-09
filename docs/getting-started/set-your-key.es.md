# Establece tu clave de API

Establece tu clave de Claudin.io **una vez** como variable de entorno y cada herramienta en esta guía puede reutilizarla — no es necesario pegarla en cada cliente manualmente.

Obtén tu clave `sk-...` desde el [panel de control](https://claudin.io/dashboard) (consulta [Crea tu cuenta](account.md)), luego agrégala a tu perfil de shell para que esté disponible en cada nueva terminal.

## macOS / Linux

=== "zsh (predeterminado en macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Reemplaza `sk-...` con tu clave real. ¿No estás seguro de qué shell tienes? Ejecuta `echo $SHELL`.

## Verificar

```bash
echo $CLAUDINIO_API_KEY
```

Deberías ver tu clave impresa. Si está vacía, abre una nueva terminal o vuelve a ejecutar el comando `source` anterior.

## Por qué esto ayuda

Cada script de **Configuración rápida** en la sección [Conecta tu herramienta](../clients/opencode.md) lee `$CLAUDINIO_API_KEY`, así que una vez exportada puedes ejecutar cualquiera de ellos tal cual — no hay `YOUR_API_KEY` que reemplazar. Las herramientas que leen variables de entorno directamente (el `env_key` de Codex, cualquier CLI compatible con OpenAI) también lo recogen automáticamente.

!!! warning "Trata tu clave como una contraseña"
    Cualquier persona con esta clave puede gastar el presupuesto de tu plan. No subas tu `~/.zshrc` / `~/.bashrc` a un repositorio público. Si la clave se filtra, revócala en el panel de control y exporta una nueva.

---

¿Clave exportada? Ahora [haz tu primera llamada](first-call.md) o salta directamente a [conectar tu herramienta](../clients/opencode.md).