# Gói và giới hạn

Mọi gói Claudin.io đều là **sử dụng không giới hạn** với **giới hạn bảo vệ chi tiêu**.
Bạn không bị tính phí theo token hay yêu cầu — bạn trả một mức giá cố định hàng tháng và
sử dụng tự do. Giới hạn chỉ tồn tại để ngăn một tác nhân mất kiểm soát
(ví dụ: vòng lặp công cụ vô hạn) làm cạn kiệt gói của bạn.

## Các gói

| Gói | Giá | Bảo vệ chi tiêu | Tốt nhất cho |
| --- | --- | --- | --- |
| **Khởi đầu** | $5 / tháng | $0.50 / giờ | Dùng thử — cam kết thấp |
| **Nhẹ** | $9 / tháng | $1.00 / giờ | Dự án sở thích, thỉnh thoảng code |
| **Cơ bản** | $19 / tháng hoặc $189 / năm | $2.00 / giờ | Code hàng ngày — lựa chọn phổ biến |
| **Pro** ★ | $39 / tháng hoặc $389 / năm | $4.00 / giờ | Quy trình làm việc tác nhân nặng |
| **Mạnh mẽ** | $59 / tháng hoặc $589 / năm | $6.00 / giờ | Nhóm, nhiều dự án |
| **Siêu** | $99 / tháng hoặc $989 / năm | $10.00 / giờ | Sức mạnh tối đa, nhóm và sản xuất |

!!! mẹo "Hầu hết mọi người không bao giờ chạm giới hạn"
    Giới hạn theo giờ rất hào phóng cho công việc tương tác thông thường. Bạn thường chỉ
    chạm phải nó khi tác nhân rơi vào vòng lặp chặt — chính xác là lúc bạn *muốn* phanh.

## claudinio vs Claudius

|                      | claudinio 🏆         | claudius ★           |
| -------------------- | -------------------- | -------------------- |
| **Starter**          | ✅                   |                      |
| **Lite**             | ✅                   |                      |
| **Essential**        | ✅                   | ✅                   |
| **Pro**              | ✅                   | ✅                   |
| **Power**            | ✅                   | ✅                   |
| **Ultra**            | ✅                   | ✅                   |

> **Giá trị tốt nhất cho đồng tiền của bạn.**

### Dành cho Starter / Lite: sử dụng claudinio

Nếu bạn đang dùng Starter hoặc Lite, claudinio là mô hình bạn sẽ sử dụng. Và thành thật mà nói? Bạn sẽ không cần nhìn lại phía sau. claudinio sánh ngang với các mô hình hàng đầu trong khi chỉ có chi phí bằng một phần nhỏ — hoàn hảo cho việc coding hàng ngày, học tập và các dự án sở thích.

### Dành cho Essential trở lên: cả thế giới là của bạn

Essential trở lên cho bạn quyền truy cập cả claudinio và claudius. Sử dụng claudinio cho các tác vụ hàng ngày và dành claudius cho những lúc bạn cần thêm sức mạnh — kiến trúc phức tạp, suy luận sâu sắc, hoặc các phiên gỡ lỗi khó khăn.

### Nhưng này, nguyên tắc vàng

Bất kể gói của bạn là gì, chúng tôi khuyên bạn nên đặt claudinio làm mô hình mặc định. Đây là mô hình hàng đầu của chúng tôi, và chúng tôi tin tưởng vào nó. Bạn luôn có thể chuyển sang claudius khi công việc yêu cầu.

### Bí danh mô hình

Tất cả các gói đều hỗ trợ bí danh mô hình cho các mô hình phổ biến như: `claude-sonnet-4`, `gpt-4o`, `gemini-2.5-pro`, `llama-4`, `deepseek-v4`. Xem [API Reference](/api-reference/) của chúng tôi để biết danh sách đầy đủ.

## Bảo vệ chi tiêu hoạt động như thế nào

Mỗi gói xác định một **cửa sổ** ngân sách — một khoảng thời gian luân phiên và chi tiêu tối đa trong đó:

- **Khởi đầu**, **Nhẹ**, **Cơ bản**, **Pro**, **Mạnh mẽ** và **Siêu** sử dụng cửa sổ **1 giờ**.

Trong cửa sổ, việc sử dụng của bạn tích lũy một chi phí nội bộ nhỏ. Khi chi phí nội bộ
đó đạt đến giới hạn của cửa sổ, các yêu cầu sẽ tạm dừng cho đến khi cửa sổ được đặt lại.

Chỉ các cuộc gọi mô hình của bạn đi qua proxy. Mỗi yêu cầu thêm vào tổng số hiện tại
của cửa sổ dựa trên các token đã sử dụng. Khi cửa sổ được đặt lại, tổng số cũng được đặt lại.

Nếu bạn chạm giới hạn và nhận được lỗi ngân sách, bạn có hai lựa chọn:

1. Đợi cửa sổ đặt lại (hiển thị trong bảng điều khiển của bạn).
2. Nâng cấp lên gói cao hơn để có giới hạn lớn hơn.

Xem [Lỗi liên quan đến gói](api-reference.md#errors) để biết lỗi ngân sách trông như thế nào.
