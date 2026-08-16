#!/usr/bin/env python3
"""Insert the "alternative cap response" section into every api-reference.

The hourly ceiling normally answers with `429` + `Retry-After`, and all 18
copies of the API reference promise exactly that. Some accounts may instead
receive a normal completion whose text explains the ceiling — so the reference
has to say so, in every language, BEFORE that is switched on for anyone.

Wording rules, and why each one:

* **Do not call it an A/B test.** There is no split and no randomisation; it is
  a small set of accounts. Describing a mechanism as an experiment it is not
  would be its own inaccuracy, in a document whose value is being accurate.
* **Warn integrators explicitly.** The alternative answer arrives with a
  success status, so any loop keyed on the status code alone reads a refusal as
  a result. That sentence is the whole reason this section is worth publishing.
* **Say the `429` is still the default**, because it is, and a reader who
  over-corrects and stops handling it would be worse off than before.

Insertion point is immediately before the `##` heading that follows the budget
cap section, located from the last prose mention of `Retry-After` rather than
from translated headings.

Run from the repo root: python3 docs/insert_cap_alternative.py
"""

import os
import re

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
ANCHOR = "{#cap-alternative-response}"

SECTIONS = {
    "api-reference.md": """### A message instead of a `429` {#cap-alternative-response}

On a small number of accounts we are trialling a different answer to the same
situation. Instead of the error, the request completes and the reply itself
explains that the ceiling is reached and when it resets. We are measuring
whether that reaches people more reliably than an error their agent quietly
swallows — and whether, told plainly, they would rather move to a plan that
fits.

**If you build automation, do not read a `2xx` as "work was done".** Treat a
reply that says the ceiling is reached as the ceiling being reached, and back
off until the window resets. The `429` above remains the default and is what
almost every account receives.
""",
    "api-reference.pt.md": """### Uma mensagem em vez de um `429` {#cap-alternative-response}

Num pequeno número de contas estamos a experimentar uma resposta diferente para
a mesma situação. Em vez do erro, o pedido é concluído e a própria resposta
explica que o teto foi atingido e quando reinicia. Estamos a medir se assim a
informação chega às pessoas de forma mais fiável do que um erro que o agente
delas engole em silêncio — e se, dito com clareza, preferem mudar para um plano
à medida.

**Se está a construir automação, não leia um `2xx` como "o trabalho foi
feito".** Trate uma resposta que diz que o teto foi atingido como o teto tendo
sido atingido, e recue até a janela reiniciar. O `429` acima continua a ser o
comportamento por omissão e é o que quase todas as contas recebem.
""",
    "api-reference.pt-BR.md": """### Uma mensagem em vez de um `429` {#cap-alternative-response}

Em um pequeno número de contas estamos testando uma resposta diferente para a
mesma situação. Em vez do erro, a requisição é concluída e a própria resposta
explica que o teto foi atingido e quando ele reinicia. Estamos medindo se assim
a informação chega às pessoas de forma mais confiável do que um erro que o
agente delas engole em silêncio — e se, dito com clareza, elas prefeririam
mudar para um plano do tamanho certo.

**Se você constrói automação, não leia um `2xx` como "o trabalho foi
feito".** Trate uma resposta que diz que o teto foi atingido como o teto tendo
sido atingido, e recue até a janela reiniciar. O `429` acima continua sendo o
comportamento padrão e é o que quase todas as contas recebem.
""",
    "api-reference.es.md": """### Un mensaje en lugar de un `429` {#cap-alternative-response}

En un pequeño número de cuentas estamos probando una respuesta distinta para la
misma situación. En vez del error, la solicitud se completa y la propia
respuesta explica que se alcanzó el límite y cuándo se reinicia. Estamos
midiendo si así la información llega a las personas de forma más fiable que un
error que su agente se traga en silencio — y si, dicho claramente, prefieren
pasar a un plan que les quede bien.

**Si construyes automatización, no leas un `2xx` como "el trabajo se hizo".**
Trata una respuesta que dice que se alcanzó el límite como el límite alcanzado,
y retrocede hasta que la ventana se reinicie. El `429` de arriba sigue siendo
el comportamiento por defecto y es lo que recibe casi cualquier cuenta.
""",
    "api-reference.fr.md": """### Un message au lieu d'un `429` {#cap-alternative-response}

Sur un petit nombre de comptes, nous testons une réponse différente à la même
situation. Au lieu de l'erreur, la requête aboutit et la réponse elle-même
explique que le plafond est atteint et quand il se réinitialise. Nous mesurons
si l'information atteint ainsi les personnes plus sûrement qu'une erreur que
leur agent avale en silence — et si, dit clairement, elles préfèrent passer à
une offre à leur taille.

**Si vous construisez de l'automatisation, ne lisez pas un `2xx` comme « le
travail a été fait ».** Traitez une réponse qui dit que le plafond est atteint
comme le plafond atteint, et attendez la réinitialisation de la fenêtre. Le
`429` ci-dessus reste le comportement par défaut et c'est ce que reçoit presque
tous les comptes.
""",
    "api-reference.de.md": """### Eine Nachricht statt eines `429` {#cap-alternative-response}

Bei einer kleinen Zahl von Konten testen wir eine andere Antwort auf dieselbe
Situation. Statt des Fehlers wird die Anfrage abgeschlossen, und die Antwort
selbst erklärt, dass das Limit erreicht ist und wann es zurückgesetzt wird. Wir
messen, ob die Information Menschen so zuverlässiger erreicht als ein Fehler,
den ihr Agent stillschweigend schluckt — und ob sie, klar gesagt, lieber zu
einem passenden Tarif wechseln.

**Wenn du Automatisierung baust, lies ein `2xx` nicht als „Arbeit erledigt".**
Behandle eine Antwort, die sagt, das Limit sei erreicht, als erreichtes Limit,
und warte bis zum Zurücksetzen des Fensters. Der `429` oben bleibt das
Standardverhalten und ist das, was fast jedes Konto erhält.
""",
    "api-reference.it.md": """### Un messaggio invece di un `429` {#cap-alternative-response}

Su un piccolo numero di account stiamo provando una risposta diversa alla stessa
situazione. Invece dell'errore, la richiesta va a buon fine e la risposta stessa
spiega che il limite è stato raggiunto e quando si azzera. Stiamo misurando se
così l'informazione arriva alle persone in modo più affidabile di un errore che
il loro agente si beve in silenzio — e se, detto chiaramente, preferiscono
passare a un piano della misura giusta.

**Se costruisci automazioni, non leggere un `2xx` come "il lavoro è stato
fatto".** Tratta una risposta che dice che il limite è stato raggiunto come il
limite raggiunto, e attendi l'azzeramento della finestra. Il `429` qui sopra
resta il comportamento predefinito ed è ciò che riceve quasi ogni account.
""",
    "api-reference.ru.md": """### Сообщение вместо `429` {#cap-alternative-response}

На небольшом числе аккаунтов мы пробуем другой ответ в той же ситуации. Вместо
ошибки запрос завершается успешно, а сам ответ объясняет, что лимит достигнут и
когда он обнулится. Мы измеряем, доходит ли так информация до людей надёжнее,
чем ошибка, которую их агент молча проглатывает, — и предпочтут ли они, если
сказать прямо, перейти на подходящий тариф.

**Если вы строите автоматизацию, не читайте `2xx` как «работа выполнена».**
Считайте ответ, сообщающий о достигнутом лимите, достигнутым лимитом и делайте
паузу до обнуления окна. `429` выше остаётся поведением по умолчанию и именно
его получает почти любой аккаунт.
""",
    "api-reference.tr.md": """### `429` yerine bir mesaj {#cap-alternative-response}

Az sayıda hesapta aynı duruma farklı bir yanıt deniyoruz. Hata yerine istek
tamamlanıyor ve yanıtın kendisi tavana ulaşıldığını ve ne zaman sıfırlanacağını
açıklıyor. Bunun, ajanlarının sessizce yuttuğu bir hataya kıyasla bilgiyi
insanlara daha güvenilir şekilde ulaştırıp ulaştırmadığını ölçüyoruz — ve açıkça
söylendiğinde kendilerine uygun bir plana geçmeyi tercih edip etmediklerini.

**Otomasyon geliştiriyorsan bir `2xx`'i "iş yapıldı" diye okuma.** Tavana
ulaşıldığını söyleyen bir yanıtı tavana ulaşılmış say ve pencere sıfırlanana
kadar bekle. Yukarıdaki `429` varsayılan davranış olmayı sürdürüyor ve hemen
hemen her hesabın aldığı yanıt bu.
""",
    "api-reference.zh.md": """### 用一条消息代替 `429` {#cap-alternative-response}

在少数账户上，我们正在为同一种情况尝试另一种回应方式。请求不再返回错误，而是
正常完成，回复内容本身会说明已达到上限以及何时重置。我们在衡量：相比一个被客户
端智能体悄悄吞掉的错误，这种方式是否能更可靠地把信息传达给真人——以及在把话说
清楚之后，他们是否更愿意换成合适的套餐。

**如果你在做自动化，不要把 `2xx` 当作"任务已完成"。** 请把说明已达上限的回复
视为确实已达上限，并等到窗口重置后再继续。上面的 `429` 仍然是默认行为，也是几
乎所有账户会收到的响应。
""",
    "api-reference.ja.md": """### `429` の代わりにメッセージを返す場合 {#cap-alternative-response}

ごく一部のアカウントで、同じ状況に対する別の応答を試しています。エラーではなく
リクエストが正常に完了し、応答の本文そのものが上限に達したこととリセットの時刻を
説明します。エージェントが黙って飲み込んでしまうエラーより、この方が人に確実に
届くかどうかを測っています。あわせて、はっきり伝えられたときに、見合ったプランへ
移りたいと思うかどうかも見ています。

**自動化を組んでいる場合、`2xx` を「処理された」と読まないでください。** 上限に
達したと述べている応答は、上限に達したものとして扱い、ウィンドウがリセットされる
まで待ってください。上記の `429` は引き続き既定の動作であり、ほぼすべてのアカウ
ントが受け取るのはそちらです。
""",
    "api-reference.ko.md": """### `429` 대신 메시지를 받는 경우 {#cap-alternative-response}

소수의 계정에서 같은 상황에 대한 다른 응답을 시험하고 있습니다. 오류 대신 요청이
정상적으로 완료되고, 응답 본문이 직접 상한에 도달했다는 사실과 재설정 시점을
설명합니다. 에이전트가 조용히 삼켜 버리는 오류보다 이 방식이 사람에게 더 확실히
전달되는지, 그리고 분명히 알렸을 때 알맞은 요금제로 옮기고 싶어 하는지를 측정하고
있습니다.

**자동화를 만들고 있다면 `2xx`를 "작업이 처리됨"으로 읽지 마세요.** 상한에
도달했다고 말하는 응답은 실제로 상한에 도달한 것으로 처리하고, 창이 재설정될
때까지 기다리세요. 위의 `429`는 여전히 기본 동작이며 거의 모든 계정이 받는 응답
입니다.
""",
    "api-reference.hi.md": """### `429` के बजाय एक संदेश {#cap-alternative-response}

कुछ ही खातों पर हम इसी स्थिति के लिए एक अलग उत्तर आज़मा रहे हैं। त्रुटि के बजाय
अनुरोध पूरा होता है और उत्तर स्वयं बताता है कि सीमा पूरी हो गई है और वह कब रीसेट
होगी। हम माप रहे हैं कि क्या इस तरह जानकारी लोगों तक उस त्रुटि से अधिक भरोसे के
साथ पहुँचती है जिसे उनका एजेंट चुपचाप निगल जाता है — और क्या स्पष्ट रूप से बताए
जाने पर वे अपने काम के अनुरूप प्लान पर जाना पसंद करते हैं।

**यदि आप ऑटोमेशन बना रहे हैं, तो `2xx` को "काम हो गया" न पढ़ें।** जो उत्तर कहे कि
सीमा पूरी हो गई है, उसे सीमा पूरी होना ही मानें और विंडो रीसेट होने तक रुकें। ऊपर
दिया `429` अब भी डिफ़ॉल्ट व्यवहार है और लगभग हर खाते को वही मिलता है।
""",
    "api-reference.bn.md": """### `429`-এর বদলে একটি বার্তা {#cap-alternative-response}

অল্প কিছু অ্যাকাউন্টে আমরা একই পরিস্থিতির জন্য ভিন্ন একটি উত্তর পরখ করছি। ত্রুটির
বদলে অনুরোধটি সম্পন্ন হয় এবং উত্তরটিই জানায় যে সীমা ছুঁয়ে গেছে এবং কখন তা রিসেট
হবে। আমরা মাপছি, এজেন্ট যে ত্রুটিটি নিঃশব্দে গিলে ফেলে তার চেয়ে এভাবে তথ্যটি
মানুষের কাছে বেশি নির্ভরযোগ্যভাবে পৌঁছায় কি না — এবং স্পষ্ট করে বললে তাঁরা
মানানসই প্ল্যানে যেতে চান কি না।

**আপনি অটোমেশন বানালে `2xx`-কে "কাজ হয়ে গেছে" বলে পড়বেন না।** যে উত্তর বলে সীমা
ছুঁয়ে গেছে, সেটিকে সীমা ছোঁয়া হিসেবেই ধরুন এবং উইন্ডো রিসেট না হওয়া পর্যন্ত
অপেক্ষা করুন। উপরের `429` এখনও ডিফল্ট আচরণ এবং প্রায় প্রতিটি অ্যাকাউন্ট সেটিই পায়।
""",
    "api-reference.id.md": """### Sebuah pesan alih-alih `429` {#cap-alternative-response}

Pada sejumlah kecil akun kami sedang mencoba jawaban berbeda untuk situasi yang
sama. Alih-alih galat, permintaan diselesaikan dan balasannya sendiri
menjelaskan bahwa batas sudah tercapai dan kapan batas itu disetel ulang. Kami
mengukur apakah dengan cara ini informasinya sampai ke orangnya lebih andal
daripada galat yang ditelan diam-diam oleh agen mereka — dan apakah, kalau
dikatakan terus terang, mereka lebih memilih pindah ke paket yang pas.

**Kalau kamu membangun otomasi, jangan membaca `2xx` sebagai "pekerjaan
selesai".** Perlakukan balasan yang menyatakan batas tercapai sebagai batas yang
memang tercapai, dan tunggu sampai jendelanya disetel ulang. `429` di atas tetap
perilaku bawaan dan itulah yang diterima hampir semua akun.
""",
    "api-reference.vi.md": """### Một tin nhắn thay cho `429` {#cap-alternative-response}

Trên một số ít tài khoản, chúng tôi đang thử một câu trả lời khác cho cùng tình
huống. Thay vì lỗi, yêu cầu vẫn hoàn tất và chính nội dung trả lời sẽ giải thích
rằng đã chạm trần và khi nào trần được đặt lại. Chúng tôi đang đo xem cách này
có đưa thông tin đến người dùng đáng tin cậy hơn một lỗi bị tác nhân của họ nuốt
đi lặng lẽ hay không — và liệu khi được nói rõ, họ có muốn chuyển sang gói vừa
tầm hay không.

**Nếu bạn xây dựng tự động hoá, đừng đọc `2xx` là "đã làm xong việc".** Hãy xem
một phản hồi nói rằng đã chạm trần đúng là đã chạm trần, và chờ đến khi cửa sổ
được đặt lại. `429` ở trên vẫn là hành vi mặc định và là thứ gần như mọi tài
khoản nhận được.
""",
    "api-reference.ar.md": """### رسالة بدل الرمز `429` {#cap-alternative-response}

في عدد صغير من الحسابات نجرّب ردًّا مختلفًا على الموقف نفسه. فبدل الخطأ يكتمل
الطلب، ويشرح الردّ نفسه أن الحدّ قد بُلغ ومتى تُعاد تهيئته. نحن نقيس ما إذا كانت
المعلومة تصل إلى الأشخاص بهذه الطريقة على نحو أوثق من خطأ يبتلعه وكيلهم بصمت —
وما إذا كانوا، حين يُقال لهم ذلك بوضوح، يفضّلون الانتقال إلى خطة على مقاسهم.

**إن كنت تبني أتمتة، فلا تقرأ الرمز `2xx` على أنه "أُنجز العمل".** تعامل مع أي
ردّ يقول إن الحدّ قد بُلغ على أنه بلوغ فعلي للحدّ، وتوقّف حتى تُعاد تهيئة النافذة.
يبقى الرمز `429` أعلاه هو السلوك الافتراضي، وهو ما تتلقاه كل الحسابات تقريبًا.
""",
    "api-reference.ur.md": """### `429` کے بجائے ایک پیغام {#cap-alternative-response}

چند ایک اکاؤنٹس پر ہم اسی صورتِ حال کے لیے ایک مختلف جواب آزما رہے ہیں۔ خرابی کے
بجائے درخواست مکمل ہو جاتی ہے اور جواب خود بتاتا ہے کہ حد پوری ہو چکی ہے اور وہ
کب دوبارہ مقرر ہوگی۔ ہم یہ ماپ رہے ہیں کہ آیا اس طرح معلومات لوگوں تک اُس خرابی
کی نسبت زیادہ بھروسے سے پہنچتی ہیں جسے اُن کا ایجنٹ خاموشی سے نگل جاتا ہے — اور
یہ کہ صاف بتائے جانے پر کیا وہ اپنے کام کے مطابق پلان پر جانا پسند کرتے ہیں۔

**اگر آپ آٹومیشن بنا رہے ہیں تو `2xx` کو "کام ہو گیا" نہ سمجھیں۔** جو جواب کہے کہ
حد پوری ہو چکی ہے، اُسے حد کا پورا ہونا ہی سمجھیں اور ونڈو دوبارہ مقرر ہونے تک
رُک جائیں۔ اوپر دیا گیا `429` اب بھی طے شدہ رویہ ہے اور تقریباً ہر اکاؤنٹ کو وہی
ملتا ہے۔
""",
}


def insert(path: str, section: str) -> bool:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    if ANCHOR in "\n".join(lines):
        return False

    # The budget-cap prose is the last mention of Retry-After (the errors table
    # above it is the first). Insert before the next top-level heading.
    last = max(
        (i for i, l in enumerate(lines) if "Retry-After" in l), default=-1
    )
    if last < 0:
        raise SystemExit(f"{path}: no Retry-After mention to anchor against")

    nxt = next(
        (i for i in range(last + 1, len(lines)) if re.match(r"^## ", lines[i])),
        len(lines),
    )

    block = section.rstrip("\n").split("\n")
    lines[nxt:nxt] = block + [""]

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return True


def main() -> None:
    for name, section in SECTIONS.items():
        path = os.path.join(DOCS, name)
        if not os.path.exists(path):
            raise SystemExit(f"missing {path}")
        print(f"{name}: {'inserted' if insert(path, section) else 'already present'}")


if __name__ == "__main__":
    main()
