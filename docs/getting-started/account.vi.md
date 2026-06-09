# Tạo tài khoản của bạn

Lấy một khóa API hoạt động chỉ mất khoảng một phút.

## 1. Đăng nhập bằng GitHub

Truy cập **[claudin.io](https://claudin.io)** và nhấp vào **Sign in with GitHub**.
Claudin.io sử dụng GitHub để đăng nhập — không cần quản lý mật khẩu riêng.

Lần đầu tiên bạn đăng nhập, tài khoản của bạn được tạo tự động trên gói
**Free**, vì vậy bạn có thể dùng thử trước khi trả bất kỳ khoản phí nào.

## 2. Tạo khóa API của bạn

Khi bạn đã vào [bảng điều khiển](https://claudin.io/dashboard):

1. Tìm thẻ **API Keys**.
2. Nhấp vào **Generate key** (hoặc **Create new key**).
3. Sao chép khóa — nó có dạng `sk-...`.

!!! warning "Xem khóa của bạn như mật khẩu"
    Khóa API của bạn cấp quyền truy cập vào ngân sách gói của bạn. Đừng commit nó vào
    kho lưu trữ, dán nó trong cuộc trò chuyện công khai hoặc chia sẻ nó. Nếu khóa bị rò rỉ, hãy thu hồi nó
    từ bảng điều khiển và tạo một khóa mới.

## 3. Ghi lại hai giá trị bạn sẽ cần

Mọi tích hợp đều cần hai điều tương tự:

| Giá trị | Mô tả |
| --- | --- |
| **Base URL** | `https://api.claudin.io` |
| **Model** | `claudinio` |
| **API key** | `sk-...` bạn vừa sao chép |

Đó là tất cả. Tiếp theo, hãy [thực hiện lệnh gọi API thô](first-call.md) để xác nhận nó hoạt động,
hoặc chuyển thẳng đến [kết nối công cụ của bạn](../clients/claude-code.md).

---

## Chọn gói

Bạn có thể ở lại gói **Free** để dùng thử. Khi bạn sẵn sàng có thêm
không gian, hãy nâng cấp từ bảng điều khiển — xem [Gói & giới hạn](../plans.md) để biết
chi tiết đầy đủ.

Việc nâng cấp được xử lý qua Stripe và có hiệu lực ngay lập tức.