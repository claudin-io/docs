# OpenCode

[OpenCode](https://opencode.ai) ক্লডিন.আইও-তে একটি OpenAI-সামঞ্জস্যপূর্ণ প্রদানকারী হিসেবে সংযোগ করে। সবচেয়ে দ্রুত উপায় হলো এর বিল্ট-ইন auth ফ্লো।

## দ্রুত সেটআপ

1. লগইন কমান্ড চালান:

    ```bash
    opencode auth login
    ```

2. **Claudinio** কে প্রদানকারী হিসেবে নির্বাচন করুন।
3. প্রম্পট করা হলে আপনার API কী পেস্ট করুন — এটি আপনার [ড্যাশবোর্ড](https://claudin.io/dashboard) থেকে কপি করুন।

তারপর OpenCode শুরু করুন এবং **claudinio** মডেলটি বাছুন।

## এনভায়রনমেন্ট-ভেরিয়েবল বিকল্প

আপনি যদি ইতিমধ্যে [আপনার কী এক্সপোর্ট করে থাকেন](../getting-started/set-your-key.md), তাহলে OpenCode স্ট্যান্ডার্ড OpenAI ভেরিয়েবলগুলো গ্রহণ করে — কিছু পেস্ট করার প্রয়োজন নেই:

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

সমস্যা? [সাধারণ ত্রুটিগুলি](../api-reference.md#errors) বা [FAQ](../faq.md) দেখুন।