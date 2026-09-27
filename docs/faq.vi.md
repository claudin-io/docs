# Câu hỏi thường gặp

## Claudin.io chính xác là gì?

Một proxy API cho agent lập trình AI. Bạn trả một gói hằng tháng, nhận một ví
tín dụng được nạp lại mỗi tháng và một khóa API tương thích OpenAI/Anthropic để
dùng trong Claude Code, Kilo, Zed, Codex, Cursor hoặc bất kỳ client OpenAI nào.
Một yêu cầu lập trình thông thường tiêu khoảng một tín dụng. Không tính phí
theo token, không giới hạn theo giờ.

## Có giới hạn không?

Chỉ có ví của bạn. Không giới hạn theo giờ, giới hạn phiên hay hạn ngạch tuần —
thứ duy nhất dừng agent của bạn là số dư trống, và một lần nạp thêm sửa nó
ngay. Tín dụng của gói được làm mới mỗi tháng và không cộng dồn; tín dụng bạn
mua qua nạp thêm không bao giờ hết hạn. Xem
[Gói & tín dụng](plans.md).

## Vì sao là tín dụng thay vì giá cố định?

Vì chúng tôi đã đo giới hạn theo giờ của các gói giá cố định trên lưu lượng
thật và nó cắt 1 trong mỗi 10 giờ hoạt động trên Pro — những con người đang
làm dở việc, không phải vòng lặp mất kiểm soát. Một gói bán năng lực mà không
thể dùng khi cần thì sai hình dạng. Tín dụng là con số bạn nhìn thấy, một giờ
nặng được trả bằng những giờ yên, và một tháng nặng chỉ cách một lần nạp thêm
thay vì phải chờ.

## Có thể dùng cho việc khác ngoài lập trình không?

API tương thích OpenAI nên về kỹ thuật mọi yêu cầu đều chạy. Nhưng dịch vụ
được xây cho **lập trình bằng AI**: định tuyến, prompt và caching được tinh
chỉnh cho agent lập trình. Hoạt động không phải lập trình — chatbot chung, tự
động hóa không có code — có thể được định tuyến đặc biệt và phục vụ bởi mô hình
hoặc tầng khác với lưu lượng lập trình.

## Tôi dùng mô hình nào?

Mặc định là **`claudinio`** (hoặc `claudinio/claudinio` cho client đòi dạng
`provider/model`). Base URL là `https://api.claudin.io`. Đó là mô hình chúng
tôi tinh chỉnh, đo lường và cache cho code, và nơi tín dụng của bạn đi xa nhất.

## Tôi có thể chọn mô hình khác không?

Có, theo tên. `claudius` là lựa chọn cao cấp của chúng tôi, tối đa 6× tín dụng.
[Danh mục](plans.md#catalogue) thêm tám mô hình bên thứ ba — Claude Sonnet 5 và
Haiku 4.5, Gemini 3.1 Pro, Kimi K3, GLM 5.3, MiniMax M3, Qwen3 Coder — mỗi mô
hình được định giá là một bội số cố định của tín dụng `claudinio`, từ 3× đến
22×. Đặt ID trong client của bạn và chỉ yêu cầu đó trả hệ số. Mọi mô hình đều
có trên mọi gói; chúng tôi vẫn khuyến nghị `claudinio`.

## Xác thực bằng `Authorization` hay `x-api-key`?

Cả hai đều được. `Authorization: Bearer YOUR_API_KEY` hoặc
`x-api-key: YOUR_API_KEY`.

## Có thể dùng với công cụ không có trong danh sách không?

Có — bất kỳ công cụ nào cho phép đặt base URL OpenAI tùy chỉnh đều chạy. Dùng
[thiết lập OpenAI chung](clients/openai-compatible.md).

## Có hỗ trợ tool / function calling không?

Có. Đó là lý do nó chạy trong các trình soạn thảo agent. Truyền `tools` và đọc
`tool_calls` như với API OpenAI.

## Có xử lý được hình ảnh, âm thanh hay video không?

Có, một cách trong suốt. Gửi các khối nội dung OpenAI tiêu chuẩn; proxy chuyển
hình ảnh/âm thanh/video thành mô tả văn bản hoặc bản chép trước khi mô hình
thấy chúng. Không cần cấu hình gì đặc biệt.

## Cửa sổ ngữ cảnh là bao nhiêu?

256K token.

## Nâng cấp hoặc hủy như thế nào?

Từ [bảng điều khiển](https://claudin.io/dashboard) của bạn. Nâng cấp có hiệu
lực ngay (qua Stripe). Nếu hủy, bạn giữ gói đã trả đến hết kỳ đã thanh toán.
Tín dụng của gói kết thúc cùng kỳ đó; tín dụng bạn mua qua nạp thêm vẫn nằm
trong ví và tiếp tục dùng được sau khi gói kết thúc.

## Tôi có thể được hoàn tiền không?

**Trong vòng 48 giờ kể từ lần thanh toán đầu tiên**, có — viết đến
[support@claudin.io](mailto:support@claudin.io) từ email tài khoản của bạn. Gói
kết thúc ngay và bạn nhận lại số tiền đã trả, trừ một khoản phí sử dụng và xử
lý bù cho chi phí dùng mô hình của tài khoản bạn trong kỳ đó (không bao giờ
nhiều hơn số bạn đã trả). Thử một ngày và thấy không hợp? Bạn nhận lại gần như
toàn bộ. Tiêu hết tín dụng cả tháng trong hai ngày? Hãy chuẩn bị nhận rất ít
hoặc không có gì. Sau 48 giờ không hoàn tiền; hủy sẽ giữ gói của bạn đến hết
kỳ đã thanh toán. Toàn văn trong [Điều khoản](https://claudin.io/terms).

## Tôi nhận được `402 insufficient_credits`. Giờ sao?

Ví của bạn trống. Mua một gói [nạp thêm](plans.md#top-ups) từ bảng điều khiển
hoặc lên gói lớn hơn — cả hai có hiệu lực ngay. Không có gì xếp hàng, và không
có gì bị tính phí cho yêu cầu thất bại.

## Gói Essential / Pro / Ultra cũ của tôi thì sao?

Nó tiếp tục chạy đúng như cũ: cùng giá, cùng giới hạn theo giờ, và vẫn gia hạn
bình thường. Bạn vẫn có thể chuyển giữa Essential, Pro và Ultra từ bảng điều
khiển, và khóa API của bạn không đổi. Các gói có giới hạn theo giờ dùng
`claudinio`; `claudius` và danh mục mô hình đi kèm các gói tín dụng, nên trên gói
có giới hạn theo giờ, yêu cầu nêu tên chúng sẽ được `claudinio` phục vụ. Xem
[Gói cũ](plans.md#legacy-plans).

## Một yêu cầu thất bại với 401.

Khóa của bạn bị thiếu hoặc sai. Sao chép lại từ bảng điều khiển và đảm bảo
không có khoảng trắng thừa và header xác thực đã được đặt.

## Khóa của tôi bị lộ. Phải làm gì?

Thu hồi nó từ bảng điều khiển và tạo khóa mới ngay. Hãy coi khóa như mật khẩu —
không bao giờ commit hay chia sẻ công khai.

## Tôi tìm trợ giúp ở đâu?

Mở phiếu từ thẻ **Hỗ trợ** trong [bảng điều khiển](https://claudin.io/dashboard)
của bạn, hoặc gửi email cho bộ phận hỗ trợ. Chúng tôi sẽ phản hồi.
