# Defina a sua chave API

Defina a sua chave Claudin.io **uma vez** como uma variável de ambiente e todas as ferramentas neste guia poderão reutilizá-la — sem necessidade de a colar manualmente em cada cliente.

Obtenha a sua chave `sk-...` a partir do [dashboard](https://claudin.io/dashboard) (consulte [Criar a sua conta](account.md)), e adicione-a ao seu perfil de shell para que fique disponível em todos os novos terminais.

## macOS / Linux

=== "zsh (predefinido no macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Substitua `sk-...` pela sua chave real. Não tem a certeza de que shell está a usar? Execute `echo $SHELL`.

## Verificar

```bash
echo $CLAUDINIO_API_KEY
```

Deverá ver a sua chave impressa. Se estiver vazia, abra um novo terminal ou execute novamente o comando `source` acima.

## Porque é que isto ajuda

Todos os scripts de **Configuração rápida** na secção [Ligar a sua ferramenta](../clients/opencode.md) leem `$CLAUDINIO_API_KEY`, pelo que, depois de exportada, pode executar qualquer um deles tal como está — não há `YOUR_API_KEY` para substituir. Ferramentas que leem variáveis de ambiente diretamente (o `env_key` do Codex, qualquer CLI compatível com OpenAI) também a reconhecem automaticamente.

!!! warning "Trate a sua chave como uma palavra-passe"
    Qualquer pessoa com esta chave pode gastar o saldo do seu plano. Não faça commit do seu `~/.zshrc` / `~/.bashrc` para um repositório público. Se a chave for comprometida, revogue-a no dashboard e exporte uma nova.

---

Chave exportada? Agora [faça a sua primeira chamada](first-call.md) ou salte diretamente para [ligar a sua ferramenta](../clients/opencode.md).