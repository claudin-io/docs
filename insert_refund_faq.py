#!/usr/bin/env python3
"""Insert the "Can I get a refund?" FAQ entry into every translated faq.*.md,
right after the upgrade/cancel entry (the one that links the dashboard).

Policy decided 2026-09-11; the English source is docs/faq.md and the canonical
clause is terms.section.5.refund in the app's locales. One-shot, idempotent.
"""
import os, re

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
T = {
"pt": ("Posso pedir um reembolso?", """Nas **48 horas seguintes ao seu primeiro pagamento**, sim — escreva para
[support@claudin.io](mailto:support@claudin.io) a partir do e-mail da conta. A
subscrição termina imediatamente e recebe de volta o que pagou menos uma taxa de
utilização e processamento que cobre o custo da utilização de modelos feita pela
sua conta nesse período (nunca mais do que pagou). Experimentou um dia e não era
para si? Recebe quase tudo. Correu no teto horário durante dois dias? Conte com
pouco ou nada. Passadas 48 horas não há reembolsos; cancelar mantém o plano até
ao fim do período pago. Texto completo nos [Termos](https://claudin.io/terms)."""),
"pt-BR": ("Posso pedir reembolso?", """Em até **48 horas após o seu primeiro pagamento**, sim — escreva para
[support@claudin.io](mailto:support@claudin.io) a partir do e-mail da conta. A
assinatura é encerrada imediatamente e você recebe de volta o que pagou menos uma
taxa de uso e processamento que cobre o custo do uso de modelos feito pela sua
conta nesse período (nunca mais do que você pagou). Testou por um dia e não era
para você? Recebe quase tudo. Rodou no teto horário por dois dias? Espere pouco
ou nada. Após 48 horas não há reembolsos; cancelar mantém o plano até o fim do
período pago. Texto completo nos [Termos](https://claudin.io/terms)."""),
"es": ("¿Puedo pedir un reembolso?", """Dentro de las **48 horas siguientes a tu primer pago**, sí — escribe a
[support@claudin.io](mailto:support@claudin.io) desde el correo de tu cuenta. La
suscripción finaliza de inmediato y recuperas lo que pagaste menos una tarifa de
uso y gestión que cubre el coste del uso de modelos que hizo tu cuenta en ese
tiempo (nunca más de lo que pagaste). ¿Lo probaste un día y no era para ti?
Recuperas casi todo. ¿Lo usaste al tope horario durante dos días? Espera poco o
nada. Pasadas 48 horas no hay reembolsos; cancelar mantiene tu plan hasta el
final del periodo pagado. Texto completo en los [Términos](https://claudin.io/terms)."""),
"fr": ("Puis-je obtenir un remboursement ?", """Dans les **48 heures suivant votre premier paiement**, oui — écrivez à
[support@claudin.io](mailto:support@claudin.io) depuis l'e-mail de votre compte.
L'abonnement prend fin immédiatement et vous récupérez ce que vous avez payé,
moins des frais d'utilisation et de traitement couvrant le coût de l'utilisation
des modèles par votre compte pendant cette période (jamais plus que ce que vous
avez payé). Essayé un jour, pas convaincu ? Vous récupérez presque tout. Utilisé
au plafond horaire pendant deux jours ? Attendez-vous à peu ou rien. Passé 48
heures, aucun remboursement ; la résiliation maintient votre forfait jusqu'à la
fin de la période payée. Texte complet dans les [Conditions](https://claudin.io/terms)."""),
"de": ("Kann ich eine Erstattung bekommen?", """Innerhalb von **48 Stunden nach Ihrer ersten Zahlung**, ja — schreiben Sie von
der E-Mail-Adresse Ihres Kontos an [support@claudin.io](mailto:support@claudin.io).
Das Abonnement endet sofort, und Sie erhalten den gezahlten Betrag zurück,
abzüglich einer Nutzungs- und Bearbeitungsgebühr, die die Kosten der
Modellnutzung Ihres Kontos in dieser Zeit deckt (nie mehr als Sie gezahlt haben).
Einen Tag ausprobiert und nicht das Richtige? Sie bekommen fast alles zurück.
Zwei Tage an der Stundenobergrenze gefahren? Rechnen Sie mit wenig oder nichts.
Nach 48 Stunden gibt es keine Erstattungen; eine Kündigung behält den Plan bis
zum Ende des bezahlten Zeitraums. Vollständiger Wortlaut in den
[Bedingungen](https://claudin.io/terms)."""),
"it": ("Posso ottenere un rimborso?", """Entro **48 ore dal tuo primo pagamento**, sì — scrivi a
[support@claudin.io](mailto:support@claudin.io) dall'e-mail del tuo account.
L'abbonamento termina immediatamente e ricevi indietro quanto pagato meno una
commissione di utilizzo e gestione che copre il costo dell'utilizzo dei modelli
fatto dal tuo account in quel periodo (mai più di quanto hai pagato). Provato un
giorno e non faceva per te? Ricevi quasi tutto. Usato al tetto orario per due
giorni? Aspettati poco o nulla. Dopo 48 ore non ci sono rimborsi; annullare
mantiene il piano fino alla fine del periodo pagato. Testo completo nei
[Termini](https://claudin.io/terms)."""),
"ru": ("Могу ли я получить возврат?", """В течение **48 часов после первого платежа** — да: напишите на
[support@claudin.io](mailto:support@claudin.io) с адреса электронной почты
аккаунта. Подписка прекращается немедленно, и вы получаете обратно уплаченную
сумму за вычетом платы за использование и обработку, покрывающей стоимость
использования моделей вашим аккаунтом за это время (никогда не больше, чем вы
заплатили). Попробовали день и не подошло? Вернётся почти всё. Два дня работали
на почасовом лимите? Рассчитывайте на малую сумму или ноль. По истечении 48 часов
возвратов нет; при отмене план сохраняется до конца оплаченного периода. Полный
текст — в [Условиях](https://claudin.io/terms)."""),
"tr": ("İade alabilir miyim?", """**İlk ödemenizden itibaren 48 saat içinde**, evet — hesabınızın e-posta
adresinden [support@claudin.io](mailto:support@claudin.io) adresine yazın.
Abonelik derhal sona erer ve ödediğiniz tutarı, bu süre içinde hesabınızın
yaptığı model kullanımının maliyetini karşılayan bir kullanım ve işlem ücreti
düşülerek geri alırsınız (asla ödediğinizden fazla değil). Bir gün denediniz ve
size göre değil miydi? Neredeyse tamamını geri alırsınız. İki gün boyunca saatlik
tavanda mı çalıştırdınız? Az ya da hiç bekleyin. 48 saat sonra iade yoktur; iptal
etmek planınızı ödenmiş dönemin sonuna kadar korur. Tam metin
[Şartlar](https://claudin.io/terms) sayfasında."""),
"ja": ("返金は受けられますか？", """**初回支払いから48時間以内**であれば可能です。アカウントのメールアドレスから
[support@claudin.io](mailto:support@claudin.io) までご連絡ください。サブスクリプションは
直ちに終了し、お支払い金額から、その期間にアカウントが行ったモデル利用のコストに相当する
利用・処理手数料を差し引いた額が返金されます（お支払い金額を超えることはありません）。
1日試して合わなかった場合はほぼ全額が戻ります。2日間、時間上限いっぱいで使った場合は、
返金はわずかか、ない場合があります。48時間を過ぎると返金はありません。解約した場合、
プランは支払い済み期間の終了まで有効です。全文は[利用規約](https://claudin.io/terms)を
ご覧ください。"""),
"ko": ("환불받을 수 있나요?", """**첫 결제 후 48시간 이내**라면 가능합니다. 계정 이메일 주소로
[support@claudin.io](mailto:support@claudin.io)에 연락해 주세요. 구독은 즉시 종료되며,
결제 금액에서 해당 기간 동안 계정이 사용한 모델 사용 비용에 해당하는 사용 및 처리
수수료를 뺀 금액을 돌려받습니다(결제 금액을 초과하지 않습니다). 하루 써 보고 맞지
않았다면 거의 전액을 돌려받습니다. 이틀 동안 시간당 한도까지 사용했다면 환불액이
적거나 없을 수 있습니다. 48시간이 지나면 환불되지 않으며, 취소 시 결제된 기간이
끝날 때까지 플랜이 유지됩니다. 전문은 [이용약관](https://claudin.io/terms)을 참고하세요."""),
"zh": ("可以退款吗？", """在**首次付款后 48 小时内**可以——请使用账户邮箱写信至
[support@claudin.io](mailto:support@claudin.io)。订阅会立即终止，您将收到已付金额减去
一笔使用及处理费后的退款，该费用等于您的账户在此期间的模型使用成本（绝不会超过已付金额）。
试用了一天觉得不合适？几乎可以全额退回。连续两天按小时上限使用？退款可能很少或没有。
48 小时后不再退款；取消订阅后，套餐会保留至已付费周期结束。完整条款见
[服务条款](https://claudin.io/terms)。"""),
"ar": ("هل يمكنني استرداد المبلغ؟", """خلال **48 ساعة من أول دفعة**، نعم — راسل
[support@claudin.io](mailto:support@claudin.io) من البريد الإلكتروني المرتبط بحسابك.
ينتهي الاشتراك فورًا وتستعيد ما دفعته مطروحًا منه رسوم استخدام ومعالجة تغطي تكلفة
استخدام النماذج الذي قام به حسابك خلال تلك الفترة (ولا تتجاوز أبدًا ما دفعته). جرّبته
يومًا ولم يناسبك؟ تستعيد كل شيء تقريبًا. استخدمته عند الحد الأقصى للساعة طوال يومين؟
توقّع القليل أو لا شيء. بعد 48 ساعة لا يوجد استرداد؛ الإلغاء يُبقي خطتك حتى نهاية
الفترة المدفوعة. النص الكامل في [الشروط](https://claudin.io/terms)."""),
"hi": ("क्या मुझे रिफ़ंड मिल सकता है?", """**आपके पहले भुगतान के 48 घंटों के भीतर**, हाँ — अपने खाते के ईमेल से
[support@claudin.io](mailto:support@claudin.io) पर लिखें। सदस्यता तुरंत समाप्त हो जाती है
और आपको चुकाई गई राशि वापस मिलती है, जिसमें से उस अवधि में आपके खाते द्वारा किए गए मॉडल
उपयोग की लागत के बराबर उपयोग एवं प्रोसेसिंग शुल्क घटाया जाता है (कभी भी चुकाई गई राशि से
अधिक नहीं)। एक दिन आज़माया और पसंद नहीं आया? लगभग सब कुछ वापस मिलेगा। दो दिन प्रति घंटा
सीमा पर चलाया? बहुत कम या कुछ भी नहीं की उम्मीद रखें। 48 घंटे बाद कोई रिफ़ंड नहीं; रद्द
करने पर प्लान भुगतान की गई अवधि के अंत तक बना रहता है। पूरा पाठ
[शर्तों](https://claudin.io/terms) में।"""),
"bn": ("আমি কি রিফান্ড পেতে পারি?", """**প্রথম পেমেন্টের ৪৮ ঘণ্টার মধ্যে**, হ্যাঁ — অ্যাকাউন্টের ইমেইল থেকে
[support@claudin.io](mailto:support@claudin.io)-এ লিখুন। সাবস্ক্রিপশন তৎক্ষণাৎ শেষ হয় এবং
আপনি যা পরিশোধ করেছেন তা ফেরত পান, শুধু সেই সময়ে আপনার অ্যাকাউন্টের মডেল ব্যবহারের খরচের
সমান একটি ব্যবহার ও প্রক্রিয়াকরণ ফি বাদ দিয়ে (কখনও পরিশোধিত অর্থের বেশি নয়)। একদিন
পরীক্ষা করে পছন্দ হয়নি? প্রায় সবটাই ফেরত পাবেন। দুই দিন ঘণ্টাভিত্তিক সীমায় চালিয়েছেন?
সামান্য বা কিছুই না আশা করুন। ৪৮ ঘণ্টা পর কোনো রিফান্ড নেই; বাতিল করলে প্ল্যান পরিশোধিত
সময়কালের শেষ পর্যন্ত থাকে। সম্পূর্ণ পাঠ্য [শর্তাবলীতে](https://claudin.io/terms)।"""),
"ur": ("کیا مجھے رقم واپس مل سکتی ہے؟", """**پہلی ادائیگی کے 48 گھنٹوں کے اندر**، جی ہاں — اپنے اکاؤنٹ کے ای میل سے
[support@claudin.io](mailto:support@claudin.io) پر لکھیں۔ سبسکرپشن فوراً ختم ہو جاتی ہے اور
آپ کو ادا شدہ رقم واپس ملتی ہے، جس میں سے اس مدت میں آپ کے اکاؤنٹ کے ماڈل استعمال کی لاگت
کے برابر استعمال اور پروسیسنگ فیس منہا کی جاتی ہے (کبھی ادا شدہ رقم سے زیادہ نہیں)۔ ایک دن
آزمایا اور پسند نہیں آیا؟ تقریباً سب کچھ واپس ملے گا۔ دو دن فی گھنٹہ حد پر چلایا؟ بہت کم یا
کچھ بھی نہیں کی توقع رکھیں۔ 48 گھنٹے بعد کوئی واپسی نہیں؛ منسوخ کرنے پر پلان ادا شدہ مدت کے
اختتام تک برقرار رہتا ہے۔ مکمل متن [شرائط](https://claudin.io/terms) میں۔"""),
"id": ("Bisakah saya mendapatkan pengembalian dana?", """Dalam **48 jam setelah pembayaran pertama Anda**, bisa — tulis ke
[support@claudin.io](mailto:support@claudin.io) dari email akun Anda. Langganan
berakhir segera dan Anda menerima kembali yang Anda bayar dikurangi biaya
penggunaan dan penanganan yang menutup biaya penggunaan model oleh akun Anda
selama waktu itu (tidak pernah lebih dari yang Anda bayar). Mencoba sehari dan
tidak cocok? Hampir semuanya kembali. Menjalankannya di batas per jam selama dua
hari? Harapkan sedikit atau tidak sama sekali. Setelah 48 jam tidak ada
pengembalian dana; membatalkan tetap mempertahankan paket hingga akhir periode
yang dibayar. Teks lengkap di [Ketentuan](https://claudin.io/terms)."""),
"vi": ("Tôi có thể được hoàn tiền không?", """Trong vòng **48 giờ kể từ khoản thanh toán đầu tiên**, có — hãy gửi email đến
[support@claudin.io](mailto:support@claudin.io) từ địa chỉ email của tài khoản.
Gói đăng ký kết thúc ngay lập tức và bạn nhận lại số tiền đã trả trừ đi khoản phí
sử dụng và xử lý bằng chi phí sử dụng mô hình mà tài khoản của bạn đã dùng trong
thời gian đó (không bao giờ nhiều hơn số bạn đã trả). Dùng thử một ngày và không
hợp? Bạn nhận lại gần như toàn bộ. Chạy ở mức trần theo giờ suốt hai ngày? Hãy
chuẩn bị nhận lại rất ít hoặc không có. Sau 48 giờ không hoàn tiền; hủy đăng ký
giữ gói đến hết kỳ đã thanh toán. Toàn văn tại [Điều khoản](https://claudin.io/terms)."""),
}

for lang, (title, body) in T.items():
    path = os.path.join(HERE, f"faq.{lang}.md")
    s = open(path, encoding="utf-8").read()
    if "claudin.io/terms" in s and "48" in s:
        print(f"{lang}: already present"); continue
    heads = [m.start() for m in re.finditer(r"^## ", s, re.M)]
    anchor = None
    for i, h in enumerate(heads):
        end = heads[i + 1] if i + 1 < len(heads) else len(s)
        if "claudin.io/dashboard" in s[h:end] and ("Stripe" in s[h:end]):
            anchor = end; break
    if anchor is None:
        raise SystemExit(f"{lang}: cancel entry not found")
    block = f"## {title}\n\n{body}\n\n"
    s = s[:anchor] + block + s[anchor:]
    open(path, "w", encoding="utf-8").write(s)
    print(f"{lang}: inserted")
