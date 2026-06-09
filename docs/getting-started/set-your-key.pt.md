# Definir a sua chave de API

Defina a sua chave Claudin.io **uma vez** como uma variável de ambiente e todas as ferramentas neste guia podem reutilizá-la — sem necessidade de a colar manualmente em cada cliente.

Obtenha a sua chave `sk-...` a partir do [painel de controlo](https://claudin.io/dashboard) (veja [Criar a sua conta](account.md)), depois adicione-a ao seu perfil de shell para que esteja disponível em todos os novos terminais.

## macOS / Linux

=== "zsh (default on macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Substitua `sk-...` pela sua chave real. Não tem a certeza de qual shell está a usar? Execute `echo $SHELL`.

## Verify

```bash
echo $CLAUDINIO_API_KEY
```

Deverá ver a sua chave impressa. Se estiver vazia, abra um novo terminal ou execute novamente o comando `source` acima.

## Why this helps

Cada script de **Configuração rápida** na secção [Ligar a sua ferramenta](../clients/opencode.md) lê `$CLAUDINIO_API_KEY`, por isso, depois de exportada, pode executar qualquer um deles tal como está — não há `YOUR_API_KEY` para substituir. As ferramentas que leem variáveis de ambiente diretamente (o `env_key` do Codex, qualquer CLI compatível com OpenAI) também a detetam automaticamente.

!!! warning "Trate a sua chave como uma palavra-passe"
    Qualquer pessoa com esta chave pode gastar o orçamento do seu plano. Não faça commit do seu `~/.zshrc` / `~/.bashrc` para um repositório público. Se a chave vazar, revogue-a no painel de controlo e exporte uma nova.

---

Chave exportada? Agora [faça a sua primeira chamada](first-call.md) ou salte diretamente para [ligar a sua ferramenta](../clients/opencode.md).