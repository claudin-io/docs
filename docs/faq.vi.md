# Câu hỏi thường gặp

## Claudin.io chính xác là gì?

Một proxy API cho các AI coding agent. Bạn trả một khoản phí đăng ký hàng tháng cố định và nhận
một khóa API tương thích với OpenAI/Anthropic mà bạn có thể sử dụng trong Claude Code, Kilo, Zed,
Codex, Cursor, hoặc bất kỳ OpenAI client nào. Không tính phí theo token.

## Có thực sự không giới hạn không?

Việc sử dụng là không giới hạn — không có bộ đếm yêu cầu hay đồng hồ đo token. Giới hạn duy nhất
là một **ngưỡng bảo vệ chi tiêu** trong mỗi khung thời gian nhằm ngăn một agent chạy không kiểm soát
làm cạn kiệt gói của bạn. Trong công việc tương tác thông thường, bạn hiếm khi chạm tới giới hạn này. Xem
[Gói & giới hạn](plans.md).

## Tôi có thể dùng nó cho việc ngoài lập trình không?

API tương thích OpenAI nên về mặt kỹ thuật mọi yêu cầu đều chạy. Nhưng dịch vụ
được xây dựng cho **lập trình với AI**: định tuyến, prompt và bộ nhớ đệm đều
được tinh chỉnh cho các agent viết mã. Hoạt động không liên quan đến lập trình
— chatbot đa mục đích, tự động hóa không phải viết mã — có thể chịu định tuyến
đặc biệt và được phục vụ bởi mô hình hoặc bậc khác với lưu lượng lập trình.

## Tôi sử dụng model nào?

Luôn luôn là **`claudinio`** (hoặc `claudinio/claudinio` cho các client muốn
định dạng `provider/model`). Base URL là `https://api.claudin.io`.

## Tôi xác thực bằng `Authorization` hay `x-api-key`?

Cả hai đều được. `Authorization: Bearer YOUR_API_KEY` hoặc `x-api-key: YOUR_API_KEY`.

## Tôi có thể sử dụng nó với một công cụ không có trong danh sách không?

Có — bất kỳ công cụ nào cho phép bạn đặt base URL OpenAI tùy chỉnh đều hoạt động. Sử dụng
[thiết lập OpenAI chung](clients/openai-compatible.md).

## Nó có hỗ trợ tool / function calling không?

Có. Đó là lý do nó hoạt động bên trong các trình soạn thảo agentic. Truyền `tools` và đọc
`tool_calls` như với API OpenAI.

## Nó có thể xử lý hình ảnh, âm thanh hoặc video không?

Có, một cách minh bạch. Gửi các content block tiêu chuẩn của OpenAI; proxy sẽ chuyển đổi
hình ảnh/âm thanh/video thành mô tả văn bản hoặc bản ghi âm trước khi model nhìn thấy
chúng. Không cần cấu hình gì đặc biệt.

## Cửa sổ ngữ cảnh là bao nhiêu?

256K token.

## Làm thế nào để tôi nâng cấp hoặc hủy?

Từ [dashboard](https://claudin.io/dashboard) của bạn. Việc nâng cấp có hiệu lực ngay lập tức
(qua Stripe). Nếu bạn hủy, bạn vẫn giữ gói đã trả tiền cho đến cuối kỳ
mà bạn đã thanh toán, sau đó tự động chuyển xuống Free.

## Tôi có thể được hoàn tiền không?

Trong vòng **48 giờ kể từ khoản thanh toán đầu tiên**, có — hãy gửi email đến
[support@claudin.io](mailto:support@claudin.io) từ địa chỉ email của tài khoản.
Gói đăng ký kết thúc ngay lập tức và bạn nhận lại số tiền đã trả trừ đi khoản phí
sử dụng và xử lý bằng chi phí sử dụng mô hình mà tài khoản của bạn đã dùng trong
thời gian đó (không bao giờ nhiều hơn số bạn đã trả). Dùng thử một ngày và không
hợp? Bạn nhận lại gần như toàn bộ. Chạy ở mức trần theo giờ suốt hai ngày? Hãy
chuẩn bị nhận lại rất ít hoặc không có. Sau 48 giờ không hoàn tiền; hủy đăng ký
giữ gói đến hết kỳ đã thanh toán. Toàn văn tại [Điều khoản](https://claudin.io/terms).

## Tôi gặp lỗi ngân sách. Làm sao đây?

Bạn đã đạt đến ngưỡng bảo vệ chi tiêu của khung thời gian hiện tại. Hoặc đợi cho đến khi
khung thời gian được đặt lại (dashboard của bạn hiển thị thời gian) hoặc [nâng cấp](plans.md) để có
ngưỡng cao hơn.

## Một yêu cầu thất bại với mã 401.

Khóa của bạn bị thiếu hoặc sai. Sao chép lại từ dashboard và đảm bảo
không có khoảng trắng thừa, và header xác thực đã được thiết lập.

## Khóa của tôi bị rò rỉ. Tôi phải làm gì?

Thu hồi nó từ dashboard và tạo một khóa mới ngay lập tức. Hãy coi các khóa như
mật khẩu — không bao giờ commit chúng hoặc chia sẻ chúng công khai.

## Tôi nhận trợ giúp ở đâu?

Mở một ticket từ thẻ **Hỗ trợ** trong
[dashboard](https://claudin.io/dashboard) của bạn, hoặc gửi email đến bộ phận hỗ trợ. Chúng tôi sẽ phản hồi
bạn.