# Defina sua chave de API

Defina sua chave do Claudin.io **uma vez** como uma variável de ambiente e toda ferramenta
deste guia poderá reutilizá-la — sem necessidade de colá-la em cada cliente manualmente.

Pegue sua chave `sk-...` no [dashboard](https://claudin.io/dashboard) (veja
[Crie sua conta](account.md)), então adicione-a ao seu perfil do shell para que
esteja disponível em todo novo terminal.

## macOS / Linux

=== "zsh (padrão no macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Substitua `sk-...` pela sua chave real. Não sabe em qual shell está? Execute
`echo $SHELL`.

## Verifique

```bash
echo $CLAUDINIO_API_KEY
```

Você deve ver sua chave impressa na tela. Se estiver vazia, abra um novo terminal ou
execute novamente o comando `source` acima.

## Por que isso ajuda

Todo script de **Configuração rápida** na seção [Conecte sua ferramenta](../clients/opencode.md)
lê `$CLAUDINIO_API_KEY`. Portanto, uma vez exportada, você pode executar qualquer um deles
como está — não há `YOUR_API_KEY` para substituir. Ferramentas que leem variáveis de ambiente
diretamente (o `env_key` do Codex, qualquer CLI compatível com OpenAI) também a reconhecem
automaticamente.

!!! warning "Trate sua chave como uma senha"
    Qualquer pessoa com esta chave pode gastar o saldo do seu plano. Não envie seu
    `~/.zshrc` / `~/.bashrc` para um repositório público. Se a chave vazar, revogue-a no
    dashboard e exporte uma nova.

---

Chave exportada? Agora [faça sua primeira chamada](first-call.md) ou vá direto para
[conectar sua ferramenta](../clients/opencode.md).