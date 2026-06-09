# OpenCode

[OpenCode](https://opencode.ai) Claudin.io-এর সাথে একটি OpenAI-সামঞ্জস্যপূর্ণ প্রদানকারী হিসেবে যুক্ত হয়। সবচেয়ে দ্রুত উপায় হলো এর অন্তর্নির্মিত অথেনটিকেশন ফ্লো (auth flow) ব্যবহার করা।

## দ্রুত সেটআপ

1. লগইন কমান্ডটি চালান:

    ```bash
    opencode auth login
    ```

2. প্রদানকারী হিসেবে **Claudinio** নির্বাচন করুন।
3. অনুরোধ করলে আপনার API কী পেস্ট করুন — আপনার [ড্যাশবোর্ড](https://claudin.io/dashboard) থেকে এটি কপি করে নিন।

এরপর OpenCode চালু করুন এবং **claudinio** মডেলটি বেছে নিন।

## এনভায়রনমেন্ট ভেরিয়েবল বিকল্প

আপনি যদি ইতিমধ্যেই [আপনার কী এক্সপোর্ট করে থাকেন](../getting-started/set-your-key.md), তাহলে OpenCode স্ট্যান্ডার্ড OpenAI ভেরিয়েবলগুলি গ্রহণ করবে — কিছু পেস্ট করার প্রয়োজন নেই:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| সেটিং | মান |
| --- | --- |
| বেস URL | `https://api.claudin.io/v1` |
| মডেল | `claudinio` |
| প্রদানকারী | OpenAI-সামঞ্জস্যপূর্ণ |

---

সমস্যা হচ্ছে? [সাধারণ ত্রুটি](../api-reference.md#errors) বা [FAQ](../faq.md) দেখুন।