# FAQ

## What is Claudin.io, exactly?

Yapay zeka kodlama aracıları için bir API proxy'si. Sabit bir aylık abonelik ödersiniz ve OpenAI/Anthropic uyumlu bir API anahtarı alırsınız; bunu Claude Code, Kilo, Zed, Codex, Cursor veya herhangi bir OpenAI istemcisine ekleyebilirsiniz. Token başına ücretlendirme yok.

## Is it really unlimited?

Kullanım sınırsızdır — hiçbir istek sayacı veya token ölçer yoktur. Tek sınır, zaman penceresi başına bir **harcama koruma sınırı**dır; bu, kontrolden çıkmış bir aracının planınızı tüketmesini engeller. Normal etkileşimli çalışmada nadiren bu sınıra ulaşırsınız. [Planlar ve limitler](plans.md) bölümüne bakın.

## What model do I use?

Her zaman **`claudinio`** (veya `provider/model` biçimini isteyen istemciler için `claudinio/claudinio`) kullanın. Temel URL `https://api.claudin.io` şeklindedir.

## Do I authenticate with `Authorization` or `x-api-key`?

İkisi de çalışır. `Authorization: Bearer YOUR_API_KEY` veya `x-api-key: YOUR_API_KEY`.

## Can I use it with a tool that isn't listed?

Evet — özel bir OpenAI temel URL'si ayarlamanıza izin veren herhangi bir araç çalışır. [Genel OpenAI kurulumu](clients/openai-compatible.md)nu kullanın.

## Does it support tool / function calling?

Evet. Bu yüzden aracı düzenleyicilerin içinde çalışır. OpenAI API'sinde olduğu gibi `tools` parametresini geçirin ve `tool_calls` okuyun.

## Can it handle images, audio, or video?

Evet, şeffaf bir şekilde. Standart OpenAI içerik blokları gönderin; proxy, model görmeden önce görselleri/sesi/videoyu metin açıklamalarına veya transkripsiyonlara dönüştürür. Yapılandırmanız gereken özel bir şey yok.

## What's the context window?

256K token.

## How do I upgrade or cancel?

Panonuzdan ([dashboard](https://claudin.io/dashboard)). Yükseltmeler anında uygulanır (Stripe aracılığıyla). İptal ederseniz, zaten ödediğiniz dönemin sonuna kadar ücretli planınızı kullanmaya devam edersiniz, ardından otomatik olarak Ücretsiz plana düşersiniz.

## I hit a budget error. What now?

Geçerli pencerenin harcama koruma sınırına ulaştınız. Pencerenin sıfırlanmasını bekleyin (panonuz ne zaman olduğunu gösterir) veya daha büyük bir sınır için [yükseltme](plans.md) yapın.

## A request failed with 401.

Anahtarınız eksik veya yanlış. Panodan yeniden kopyalayın ve fazladan boşluk olmadığından ve kimlik doğrulama başlığının ayarlandığından emin olun.

## My key leaked. What do I do?

Panodan iptal edin ve hemen yeni bir tane oluşturun. Anahtarlara şifre gibi davranın — asla kaydetmeyin veya herkese açık olarak paylaşmayın.

## Where do I get help?

Panonuzdaki **Destek** kartından bir bilet açın veya desteğe e-posta gönderin. Size geri döneceğiz.