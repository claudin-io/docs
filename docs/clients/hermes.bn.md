# হার্মিস এজেন্ট

[হার্মিস এজেন্ট](https://github.com/NousResearch/hermes-agent) হল নউস রিসার্চের একটি ওপেন-সোর্স
টার্মিনাল এআই এজেন্ট। এটি যেকোনো OpenAI-সামঞ্জস্যপূর্ণ এন্ডপয়েন্ট সমর্থন করে, যা এটিকে Claudin.io-এর জন্য একটি উপযুক্ত পছন্দ করে তোলে।

## উইজার্ডের মাধ্যমে দ্রুত শুরু

যেকোনো সক্রিয় হার্মিস সেশন থেকে প্রস্থান করুন (`Ctrl + C` অথবা `/quit`), তারপর চালান:

```bash
hermes model
```

মেনু থেকে **কাস্টম এন্ডপয়েন্ট** নির্বাচন করুন এবং নিম্নলিখিত তথ্য পূরণ করুন:

| ক্ষেত্র | মান |
| --- | --- |
| বেস URL | `https://api.claudin.io/v1` |
| API কী | আপনার `sk-...` কী |
| মডেল নাম | `claudinio` |

হার্মিস স্বয়ংক্রিয়ভাবে `~/.hermes/config.yaml`-এ কনফিগারেশন সংরক্ষণ করে।

এটি চেষ্টা করে দেখুন:

```bash
hermes
```

## ম্যানুয়াল কনফিগারেশন

`~/.hermes/config.yaml` সম্পাদনা করুন:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
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

> **টিপ:** টুল কলিং সহ জটিল কাজের জন্য, নিশ্চিত করুন আপনার হার্মিস এজেন্ট
> কমপক্ষে ৬৪K টোকেন কনটেক্সট সমর্থন করে এমন একটি মডেল ব্যবহার করছে (Claudinio এটি সমর্থন করে)।

## সমস্যা সমাধান

| সমস্যা | সমাধান |
| --- | --- |
| প্রমাণীকরণ ত্রুটি | `hermes doctor` চালিয়ে আপনার API কী দুবার পরীক্ষা করুন |
| মডেল পাওয়া যায়নি | নিশ্চিত করুন মডেলের নাম ঠিক `claudinio` |
| সংযোগ প্রত্যাখ্যান | আপনার নেটওয়ার্ক থেকে `https://api.claudin.io/v1`-এ পৌঁছানো যাচ্ছে কিনা যাচাই করুন |