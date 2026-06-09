# FAQ

## Chính xác thì Claudin.io là gì?

Một proxy API cho các tác nhân lập trình AI. Bạn trả một khoản phí đăng ký cố định hàng tháng và nhận được một khóa API tương thích với OpenAI/Anthropic mà bạn có thể sử dụng trong Claude Code, Kilo, Zed, Codex, Cursor, hoặc bất kỳ ứng dụng client OpenAI nào. Không tính phí theo token.

## Nó thực sự không giới hạn?

Việc sử dụng là không giới hạn — không có bộ đếm yêu cầu hay đồng hồ đo token. Giới hạn duy nhất là một **giới hạn bảo vệ chi tiêu** trong mỗi khung thời gian nhằm ngăn một tác nhân chạy quá đà làm cạn kiệt gói của bạn. Trong công việc tương tác bình thường, bạn hiếm khi chạm tới nó. Xem [Gói & giới hạn](plans.md).

## Tôi sử dụng mô hình nào?

Luôn là **`claudinio`** (hoặc `claudinio/claudinio` cho các client muốn dạng `provider/model`). URL cơ sở là `https://api.claudin.io`.

## Tôi xác thực bằng `Authorization` hay `x-api-key`?

Cả hai đều được. `Authorization: Bearer YOUR_API_KEY` hoặc `x-api-key: YOUR_API_KEY`.

## Tôi có thể sử dụng nó với một công cụ không có trong danh sách?

Có — bất kỳ công cụ nào cho phép bạn đặt URL cơ sở OpenAI tùy chỉnh đều hoạt động. Sử dụng [thiết lập OpenAI chung](clients/openai-compatible.md).

## Nó có hỗ trợ gọi công cụ / hàm không?

Có. Đó là lý do nó hoạt động bên trong các trình soạn thảo tác nhân. Truyền `tools` và đọc `tool_calls` giống như với API OpenAI.

## Nó có thể xử lý hình ảnh, âm thanh hay video?

Có, một cách minh bạch. Gửi các khối nội dung OpenAI tiêu chuẩn; proxy chuyển đổi hình ảnh/âm thanh/video thành