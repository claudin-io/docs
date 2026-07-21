# Tạo tài khoản của bạn

Việc lấy một API key hoạt động chỉ mất khoảng một phút.

## 1. Đăng nhập bằng GitHub

Đi đến **[claudin.io](https://claudin.io)** và nhấp vào **Đăng nhập bằng GitHub**.
Claudin.io sử dụng GitHub để đăng nhập — không có mật khẩu riêng biệt nào để quản lý.

Lần đầu tiên bạn đăng nhập, tài khoản của bạn được tạo tự động trên gói
**Free**, vì vậy bạn có thể dùng thử trước khi trả bất kỳ khoản phí nào.

## 2. Tạo API key của bạn

Khi bạn đã vào [bảng điều khiển](https://claudin.io/dashboard):

1. Tìm thẻ **API Keys**.
2. Nhấp vào **Tạo key** (hoặc **Tạo key mới**).
3. Sao chép key — nó có dạng `sk-...`.

!!! warning "Hãy coi key của bạn như mật khẩu"
    API key của bạn cấp quyền truy cập vào hạn mức gói của bạn. Đừng commit nó vào
    kho lưu trữ, dán nó vào chat công cộng, hoặc chia sẻ nó. Nếu key bị lộ, hãy thu hồi nó
    từ bảng điều khiển và tạo một key mới.

## 3. Ghi chú hai giá trị bạn sẽ cần

Mọi tích hợp đều cần hai thứ giống nhau:

| Giá trị | Mô tả |
| --- | --- |
| **Base URL** | `https://api.claudin.io` |
| **Model** | `claudinio` |
| **API key** | `sk-...` bạn vừa sao chép |

Vậy là xong. Tiếp theo, hãy [thực hiện lệnh gọi API thô](first-call.md) để xác nhận
nó hoạt động, hoặc nhảy thẳng đến [kết nối công cụ của bạn](../clients/claude-code.md).

---

## Chọn gói

Bạn có thể ở lại gói **Free** để dùng thử. Khi bạn sẵn sàng có thêm không gian,
hãy nâng cấp từ bảng điều khiển — xem [Gói & giới hạn](../plans.md) để biết
chi tiết đầy đủ.

Việc nâng cấp được xử lý qua Stripe và có hiệu lực ngay lập tức.