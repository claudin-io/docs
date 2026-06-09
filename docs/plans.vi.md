# Gói & giới hạn

Mọi gói Claudin.io đều **không giới hạn sử dụng** với một **giới hạn bảo vệ chi tiêu**.
Bạn không bị tính phí theo token hay yêu cầu — bạn trả một mức giá cố định hàng tháng và
sử dụng thoải mái. Giới hạn chỉ tồn tại để ngăn một tác nhân chạy không kiểm soát
(ví dụ: vòng lặp công cụ vô tận) làm cạn kiệt gói của bạn.

## Các gói

| Gói | Giá | Bảo vệ chi tiêu | Phù hợp nhất |
| --- | --- | --- | --- |
| **Miễn phí** | $0 | $0.45 / ngày | Dùng thử, sử dụng nhẹ |
| **Lite** | $5 / tháng | $0.60 / giờ | Dự án sở thích, thỉnh thoảng lập trình |
| **Essential** | $10 / tháng | $1.50 / giờ | Lập trình hàng ngày — lựa chọn phổ biến |
| **Pro** | $29 / tháng | $4.00 / giờ | Quy trình tác nhân nặng |

!!! tip "Hầu hết mọi người không bao giờ chạm giới hạn"
    Giới hạn hàng giờ rất hào phóng cho công việc tương tác bình thường. Bạn thường chỉ
    chạm vào nó nếu một tác nhân rơi vào vòng lặp chặt — đó chính là lúc bạn
    *muốn* có một cái phanh.

## Cách bảo vệ chi tiêu hoạt động

Mỗi gói xác định một **cửa sổ** ngân sách — một khoảng thời gian luân chuyển và chi tiêu tối đa
trong đó:

- **Miễn phí** sử dụng cửa sổ **24 giờ** (`$0.45/ngày`).
- **Lite / Essential / Pro** sử dụng cửa sổ **1 giờ**.

Trong cửa sổ, việc sử dụng của bạn tích lũy một chi phí nội bộ nhỏ. Khi chi phí nội bộ đó
đạt đến giới hạn của cửa sổ, các yêu cầu sẽ tạm dừng cho đến khi cửa sổ được đặt lại.
Cửa sổ đặt lại theo lịch cố định (đầu mỗi giờ, UTC, đối với các gói theo giờ), và ngân sách
còn lại của bạn được hiển thị **trực tiếp trong bảng điều khiển**.

Đây là *bảo vệ chi tiêu*, không phải thanh toán theo đồng hồ đo — các con số đô la là
trần bảo vệ, không phải số tiền bạn trả. Hóa đơn thực tế của bạn chỉ là đăng ký hàng tháng
cố định.

## Nâng cấp & hạ cấp

- **Nâng cấp** bất kỳ lúc nào từ [bảng điều khiển](https://claudin.io/dashboard).
  Thanh toán được xử lý qua Stripe và các giới hạn mới được áp dụng ngay lập tức.
- **Hạ cấp hoặc hủy** từ cùng một nơi. Nếu bạn hủy, bạn vẫn giữ gói đã trả tiền
  cho đến hết kỳ bạn đã thanh toán, sau đó tự động chuyển xuống **Miễn phí** —
  tài khoản và khóa của bạn được bảo toàn.

## Những gì được tính vào giới hạn

Chỉ các cuộc gọi mô hình của bạn thông qua proxy. Mỗi yêu cầu thêm vào tổng đang chạy
của cửa sổ hiện tại dựa trên các token đã sử dụng. Khi cửa sổ đặt lại, tổng cũng được
đặt lại theo.

Nếu bạn chạm giới hạn và nhận được lỗi ngân sách, bạn có hai lựa chọn:

1. Đợi cửa sổ đặt lại (được hiển thị trong bảng điều khiển của bạn).
2. Nâng cấp lên gói cao hơn để có giới hạn lớn hơn.

Xem [Lỗi liên quan đến gói](api-reference.md#errors) để biết lỗi ngân sách trông như thế nào.