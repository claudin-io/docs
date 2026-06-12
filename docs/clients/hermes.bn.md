[Hermes Agent](https://github.com/NousResearch/hermes-agent) একটি ওপেন সোর্স
টার্মিনাল এজেন্ট যা Nous Research তৈরি করেছে। এটি OpenAI-সামঞ্জস্যপূর্ণ যেকোনো
এন্ডপয়েন্ট সমর্থন করে, যা এটিকে Claudin.io-এর জন্য উপযুক্ত করে তোলে।

## উইজার্ড দিয়ে দ্রুত শুরু

যেকোনো সক্রিয় Hermes সেশন থেকে বেরিয়ে আসুন (`Ctrl + C` বা `/quit`), তারপর চালান:

```bash
hermes model
```

মেনু থেকে **Custom endpoint** নির্বাচন করুন এবং পূরণ করুন:

| ফিল্ড | মান |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | আপনার `sk-...` কী |
| Model name | `claudinio` |

Hermes স্বয়ংক্রিয়ভাবে কনফিগারেশন সংরক্ষণ করে `~/.hermes/config.yaml`-এ।

চেষ্টা করুন:

```bash
hermes
```

## ম্যানুয়াল কনফিগারেশন

`~/.hermes/config.yaml` এডিট করুন:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-apnar-key"
  default: "claudinio"
```

অথবা সরাসরি মান সেট করুন:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

যাচাই করুন:

```bash
hermes config check
hermes config show
```

> **টিপ:** জটিল টাস্কের জন্য নিশ্চিত করুন আপনার Hermes Agent কমপক্ষে
> 64K টোকেন কনটেক্সট সমর্থন করে (Claudinio এটি সমর্থন করে)।

## সমস্যা সমাধান

| সমস্যা | সমাধান |
| --- | --- |
| প্রমাণীকরণ ত্রুটি | `hermes doctor` দিয়ে API কী যাচাই করুন |
| মডেল পাওয়া যায়নি | মডেলের নাম `claudinio` ঠিক আছে কিনা নিশ্চিত করুন |
| সংযোগ প্রত্যাখ্যান | `https://api.claudin.io/v1` অ্যাক্সেসযোগ্য কিনা যাচাই করুন |

## দরকারি কমান্ড

| কমান্ড | বর্ণনা |
| --- | --- |
| `hermes config show` | বর্তমান কনফিগারেশন দেখুন |
| `hermes config edit` | ইন্টারঅ্যাকটিভ এডিট |
| `hermes doctor` | সমস্যা নির্ণয় |
| `hermes model` | প্রোভাইডার পরিবর্তন |
