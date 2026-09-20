# Gói & tín dụng

Mỗi gói Claudin.io là một **ví tín dụng** được nạp lại hằng tháng. Một yêu cầu
tiêu số tín dụng tương ứng với số token nó dùng — khoảng **một tín dụng** cho
một yêu cầu lập trình thông thường trên `claudinio` — và phần bạn không dùng
vẫn nằm trong ví. **Tín dụng không bao giờ hết hạn, và không có giới hạn theo
giờ.**

## Các gói

| Gói | Giá | Tín dụng / tháng | Dành cho |
| --- | --- | --- | --- |
| **Start** | $19 / tháng | 3,000 | Dùng thử, sử dụng nhẹ hằng ngày |
| **Solo** ★ | $39 / tháng | 7,000 | Một lập trình viên, mỗi ngày |
| **Pro** | $99 / tháng | 18,000 | Quy trình agent nặng |
| **Studio** | $199 / tháng | 36,000 | Nhiều agent, cả ngày |
| **Max** | $399 / tháng | 72,000 | Sản xuất, đội nhóm, bot |

Mọi gói đều bao gồm mọi mô hình: `claudinio`, `claudius` và toàn bộ
[danh mục](#catalogue). Các gói chỉ khác nhau ở số tín dụng nhận được mỗi
tháng — và gói càng lớn, mỗi tín dụng càng rẻ.

!!! tip "Gói nào đủ cho tháng của bạn"
    Một yêu cầu thông thường trên `claudinio` tiêu khoảng một tín dụng, đo trên
    hàng nghìn yêu cầu thật. Đếm số yêu cầu agent của bạn trong một ngày trọn
    vẹn, nhân với 22 ngày làm việc, và chọn bậc chứa được con số đó. Nếu nằm
    giữa hai gói, chọn gói nhỏ hơn — một tháng nặng thỉnh thoảng chỉ cần một
    lần nạp thêm là đủ.

### Nạp thêm {#top-ups}

Cần thêm trước khi tháng mới đến? Một gói **nạp thêm** cộng tín dụng vào cùng
một ví ngay lập tức, trên mọi gói:

| Nạp thêm | Tín dụng |
| --- | --- |
| $10 | 1,200 |
| $25 | 3,000 |
| $50 | 6,000 |

Tín dụng nạp thêm và tín dụng của gói là cùng một loại tín dụng: chúng cộng
dồn, không bao giờ hết hạn, và mọi mô hình đều tiêu chúng.

## Vì sao là tín dụng (và không còn giới hạn theo giờ)

Các gói của chúng tôi từng là giá cố định kèm **giới hạn chi tiêu theo giờ** —
một cái phanh chống agent kẹt trong vòng lặp, chúng tôi từng nói vậy. Trước khi
thay đổi bất cứ gì, chúng tôi đo nó trên ba ngày lưu lượng thật: **1 trong mỗi
10 giờ hoạt động trên Pro** (11.1%) kết thúc bằng việc giới hạn cắt ngang một
lập trình viên đang làm việc, và 1 trong 13 trên Essential. Đó không phải vòng
lặp vô tận. Đó là những con người đang làm việc.

Một gói bán năng lực mà không thể dùng khi cần thì sai hình dạng. Vì thế giới
hạn bị bỏ. Một gói là một số tín dụng mỗi tháng; một giờ nặng được trả bằng
những giờ yên; một tháng nặng chỉ cách một lần nạp thêm thay vì phải chờ. Thứ
duy nhất dừng agent của bạn là ví trống, và bảng điều khiển luôn hiển thị số
dư.

## Một tín dụng mua được gì

Một tín dụng có giá trị như nhau trên mọi trục. Trên `claudinio`:

| | Tín dụng cho mỗi 1M token |
| --- | --- |
| Đầu vào (cache miss) | 40 |
| Đầu vào (cache hit) | 6 |
| Đầu ra | 80 |

Gần như toàn bộ token của một agent là token prompt, và trong một phiên làm
việc gần như toàn bộ chúng đến từ cache — vì thế một yêu cầu thông thường nằm
quanh một tín dụng, và vì thế phiên dài rẻ hơn phiên ngắn tính trên mỗi yêu
cầu.

## Mô hình nào? `claudinio`, `claudius` và danh mục

| Mô hình | Nó là gì | Chi phí tín dụng | Có trong |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Mô hình chúng tôi tinh chỉnh, đo lường và cache cho code | 1× — khoảng một tín dụng mỗi yêu cầu | Mọi gói |
| **claudius** ★ | Lựa chọn cao cấp của chúng tôi cho suy luận sâu | tối đa 6x tín dụng claudinio (3× đầu vào, 4× đầu ra, 6× đọc cache) | Mọi gói (Start, Solo, Pro, Studio, Max) |

**Khuyến nghị của chúng tôi là `claudinio`.** Đó là mô hình mà mọi gói được xây
quanh: mô hình chúng tôi tinh chỉnh prompt, mô hình mọi bài đánh giá đã chấm
điểm, và nơi một tín dụng đi xa nhất. Cách thiết lập hiệu quả nhất chúng tôi
thấy là **lập kế hoạch với `claudius`, thực thi với `claudinio`** — suy luận là
nơi mô hình cao cấp xứng đáng với hệ số của nó, và vòng thực thi là nơi có khối
lượng.

### Danh mục: chọn mô hình theo tên {#catalogue}

Bạn cũng có thể gọi một mô hình bên thứ ba theo tên. Mô hình danh mục được phục
vụ **thô** — mô hình của nhà cung cấp, system prompt từ chính client của bạn,
không có tinh chỉnh Claudinio — và tiêu một bội số nguyên cố định của tín dụng
`claudinio` trên mọi trục, để giá đọc được như một con số:

| ID mô hình | Mô hình | Nhà cung cấp | Tín dụng so với `claudinio` |
| --- | --- | --- | --- |
| `qwen3-coder-flash` | Qwen3 Coder Flash | Qwen | 3× |
| `minimax-m3` | MiniMax M3 | MiniMax | 5× |
| `qwen3-coder-plus` | Qwen3 Coder Plus | Qwen | 10× |
| `haiku-4.5` | Claude Haiku 4.5 | Anthropic | 11× |
| `glm-5.3` | GLM 5.3 | Z.ai | 13× |
| `kimi-k3` | Kimi K3 | Moonshot | 18× |
| `sonnet-5` | Claude Sonnet 5 | Anthropic | 21× |
| `gemini-3.1-pro` | Gemini 3.1 Pro | Google | 22× |

Đặt `model=sonnet-5` (hoặc bất kỳ ID nào ở trên) trong client của bạn, và chỉ
yêu cầu đó trả hệ số — phần còn lại của phiên vẫn chạy theo giá `claudinio`.
Mọi mô hình danh mục đều có trên mọi gói.

!!! note "Vì sao chúng tôi vẫn khuyến nghị `claudinio`"
    Danh mục tồn tại cho lập trình viên muốn tự chọn, không phải vì có mục nào
    đo được tốt hơn cho code. `claudinio` là mô hình chúng tôi đánh giá đối
    chiếu, là nền của cache prompt, và — với chi phí mỗi yêu cầu thấp hơn 3×
    đến 22× — là nơi tín dụng của bạn đi xa nhất. Hãy dùng mô hình danh mục
    một cách có chủ đích, cho tác vụ thật sự cần nó.

> 💡 Mẹo: `claudinio` cũng phân giải các bí danh mà agent lập trình gửi mặc
> định — `claude-sonnet-4`, `gpt-4o`, `o3-mini` và hàng chục cái khác — nên
> bạn không cần đổi cấu hình agent để dùng nó.

## Khi ví trống

Yêu cầu trả về `402` với mã `insufficient_credits` (xem
[Lỗi](api-reference.md#errors)). Không có gì xếp hàng, không có gì bị tính phí.
Bạn có hai lối, cả hai đều tức thì:

1. **Mua gói nạp thêm** từ [bảng điều khiển](https://claudin.io/dashboard).
2. **Lên gói lớn hơn** — tín dụng tháng mới đến cùng hóa đơn.

Bảng điều khiển hiển thị số dư, chi tiêu trong ngày và cảnh báo số dư thấp
trước khi bạn chạm đến đó, và chúng tôi gửi một email khi số dư xuống thấp.

## Gói cũ (Essential, Pro, Ultra có giới hạn theo giờ) {#legacy-plans}

Nếu bạn đang ở một trong các gói trước đây, gói đó **tiếp tục chạy đúng như
cũ, với giới hạn theo giờ của nó, đến hết kỳ đã thanh toán**. Sau đó nó không
gia hạn. Khách hàng theo tháng nhận tín dụng thiện chí để thử hệ thống mới
trước khi chọn gói — hai tháng theo giá niêm yết của gói cũ; khách hàng theo
năm giữ trọn năm và chuyển sang tín dụng khi kết thúc. Khóa API của bạn không
đổi.
