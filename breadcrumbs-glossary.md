# Glossário de Breadcrumbs (Redis)

Cada breadcrumb é um membro do Redis Set `claudinio:user:{uid}:breadcrumbs`.
Serve como **gatilho de exclusão** para evitar re-envio da mesma campanha
para o mesmo usuário.

---

## `onboarding_feedback_sent`

| Campo | Valor |
|---|---|
| **Campanha** | Promo July 2025, Round 2 (nunca usaram os créditos) |
| **Script** | `promo_batch_send.py` |
| **Público** | Usuários com `signup_credit_granted`, sem tier, sem subscription, que **NUNCA usaram** os créditos (spent_cents == 0) |
| **Gatilho** | Se presente, `promo_batch_send.py` pula o usuário |

**Conteúdo do e-mail:** Feedback sobre o onboarding, convite para experimentar a plataforma com os $5 de crédito que ainda não usaram.

---

## `credit_exhausted_outreach_sent`

| Campo | Valor |
|---|---|
| **Campanha** | Promo July 2025, Round 1 (usaram parte dos créditos) |
| **Script** | `promo_batch_send.py` |
| **Público** | Usuários com `signup_credit_granted`, sem tier, sem subscription, que **USARAM** parte dos créditos (spent_cents > 0, balance < 500) |
| **Gatilho** | Se presente, `promo_batch_send.py` pula o usuário |
| **Nota** | Considerado **MANUAL** — setado por scripts ad-hoc, não pelo loop automático de campanhas |

**Conteúdo do e-mail:** Créditos esgotados ou quase esgotados, oferta promocional para continuar usando a plataforma.

---

## `receivedOnboarding`

| Campo | Valor |
|---|---|
| **Campanha** | Rule A — Onboarding automático |
| **Script** | `dashboard/scripts/email_campaigns.py` |
| **Público** | Conta com >1h de idade, 0 requisições na API |
| **Gatilho** | Se presente, `email_campaigns.py` Regra A não re-envia |

**Conteúdo do e-mail:** Boas-vindas e instruções de como começar.

---

## `credit_reminder_sent`

| Campo | Valor |
|---|---|
| **Campanha** | Rule D — "Créditos à tua espera" |
| **Script** | `dashboard/scripts/email_campaigns.py` |
| **Público** | Non-subscriber com crédito > 0, sem uso há ≥2 dias |
| **Gatilho** | Se presente, `email_campaigns.py` Regra D não re-envia (one-shot) |

**Conteúdo do e-mail:** Lembrete de que o usuário tem créditos não utilizados.

---

## `maintenance_notice_20260722`

| Campo | Valor |
|---|---|
| **Campanha** | Manutenção programada — one-off bulk |
| **Script** | `dashboard/scripts/send_maintenance_notice.py` |
| **Público** | Todos os usuários ativos (subscribers ativos + qualquer um com crédito > 0) |
| **Gatilho** | Se presente, o script pula o envio |
| **Nota** | O nome inclui a data (`20260722`) para permitir múltiplas notificações sem colisão |

**Conteúdo do e-mail:** Aviso de janela de manutenção programada.

---

## `claudinio_code_launch_20260715`

| Campo | Valor |
|---|---|
| **Campanha** | Lançamento do Claudinio Code — one-off bulk |
| **Script** | Ad-hoc (não versionado no repositório) |
| **Público** | Broadcast geral para todos os usuários ativos |
| **Gatilho** | Se presente, pula o envio |
| **Nota** | Nome datado (`20260715`) pelo mesmo motivo do `maintenance_notice` |

**Conteúdo do e-mail:** Anúncio de lançamento da feature Claudinio Code.

---

## Como consultar

```bash
# Ver breadcrumbs de um usuário específico
REDIS_PW=$(grep REDIS_PASSWORD .env | cut -d= -f2)
docker compose exec -T redis redis-cli -a "$REDIS_PW" \
  SMEMBERS "claudinio:user:{uid}:breadcrumbs"

# Listar todos os UIDs que tem um breadcrumb específico (ex: onboarding_feedback_sent)
docker compose exec -T redis redis-cli -a "$REDIS_PW" \
  --scan --pattern 'claudinio:user:*:breadcrumbs' 2>/dev/null \
| while read key; do
    uid=$(echo "$key" | cut -d: -f3)
    has=$(docker compose exec -T redis redis-cli -a "$REDIS_PW" \
      SISMEMBER "$key" "onboarding_feedback_sent" 2>/dev/null)
    [ "$has" = "1" ] && echo "$uid"
  done
```

## Mapa mental

```
                     ┌─ Já recebeu promo? ─── onboarding_feedback_sent
                     │                        credit_exhausted_outreach_sent
Usuário com ─────────┤
signup_credit        ├─ Já recebeu onboarding? ─── receivedOnboarding
                     │
                     ├─ Já recebeu lembrete? ──── credit_reminder_sent
                     │
                     ├─ Já recebeu aviso? ─────── maintenance_notice_20260722
                     │
                     └─ Já recebeu launch? ────── claudinio_code_launch_20260715
```

> **Regra geral:** se o breadcrumb existe, o usuário não deve receber aquela campanha novamente.
> Para campanhas one-shot (ex: Rule D, promo July 2025), basta verificar presença no Set.
> Para campanhas repeatable (ex: B1/B2 do email_campaigns.py), a lógica é mais complexa e usa outros critérios além do breadcrumb.
