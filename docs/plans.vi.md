# Gói dịch vụ & giới hạn

Mọi gói dịch vụ của Claudin.io đều có **sử dụng không giới hạn** với **mức bảo vệ chi tiêu**.
Bạn sẽ không bị tính phí theo token hay theo yêu cầu — bạn trả một mức giá cố định hàng tháng và
sử dụng thoải mái. Mức giới hạn chỉ tồn tại để ngăn một agent chạy mất kiểm soát (ví dụ: một vòng lặp công cụ vô tận) làm cạn kiệt gói dịch vụ của bạn.

## Các gói dịch vụ

| Gói dịch vụ | Giá | Bảo vệ chi tiêu | Phù hợp nhất |
| --- | --- | --- | --- |
| **Starter** | $5 / tháng | $0,50 / giờ | Dùng thử — cam kết thấp |
| **Lite** | $9 / tháng | $1,00 / giờ | Dự án cá nhân, thỉnh thoảng code |
| **Essential** | $19 / tháng hoặc $189 / năm | $2,00 / giờ | Chất lượng cho sử dụng hàng ngày |
| **Pro** ★ | $39 / tháng hoặc $389 / năm | $4,00 / giờ | Quy trình làm việc agent chuyên sâu |
| **Power** | $59 / tháng hoặc $589 / năm | $6,00 / giờ | Nhóm, nhiều dự án |
| **Ultra** | $99 / tháng hoặc $989 / năm | $10,00 / giờ | Sức mạnh tối đa, nhóm & sản xuất |

!!! tip "Hầu hết mọi người không bao giờ chạm tới mức giới hạn"
    Mức giới hạn theo giờ khá hào phóng cho công việc tương tác thông thường. Bạn thường chỉ
    chạm tới nó nếu một agent rơi vào vòng lặp chặt — đó chính xác là lúc bạn *muốn* có một cái phanh.

## Nên chọn mô hình nào? Claudinio vs Claudius

Chúng tôi cung cấp hai mô hình chính cho coding agent của bạn:

| Mô hình | Backend | Trường hợp sử dụng | Khuyến nghị cho |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Nhanh, cân bằng, tiết kiệm | Code hàng ngày, dự án cá nhân, code tổng quát | **Tất cả gói dịch vụ** (Starter đến Ultra) |
| **claudius** ★ | Cao cấp, suy luận sâu | Tác vụ phức tạp, suy luận sâu, quy trình agent chuyên sâu | Essential+ (Pro, Power, Ultra) |

### Nói thẳng

Nếu bạn đang dùng **Starter** ($5) hoặc **Lite** ($9) — **hãy dùng `claudinio` và đừng ngoái lại nhìn.** 🎯

Sự thật là: `claudinio` mang lại chất lượng tương đương Claude Sonnet cho code hàng ngày với **một phần nhỏ chi phí nội bộ**. Với gói Lite, bạn có thể nhận được **hàng trăm yêu cầu mỗi giờ** với `claudinio` — trong khi `claudius` sẽ đốt ngân sách theo giờ của bạn nhanh hơn nhiều.

| Chỉ số | claudinio | claudius |
| --- | --- | --- |
| Tác động đến ngân sách theo giờ | Thấp — kéo dài hơn nhiều | Cao — đốt nhanh hơn |
| Trường hợp sử dụng | Code hàng ngày, dự án cá nhân | Suy luận nặng, agent phức tạp |

**Nguyên tắc vàng:** Cấu hình agent của bạn (Claude Code, Cursor, Continue, v.v.) với `claudinio` làm mô hình mặc định. Chỉ chuyển sang `claudius` khi bạn thực sự cần thêm sức mạnh suy luận — và nếu gói dịch vụ của bạn cho phép (Essential+). Đối với các dự án cá nhân, `claudinio` là **tất cả những gì bạn cần** và có lẽ **còn hơn cả bạn mong đợi**.

> 💡 Mẹo: Cả hai mô hình đều hoạt động với tất cả các coding agent chính. Chỉ cần đặt `model=claudinio` hoặc `model=claudius` trong cấu hình agent của bạn. `claudinio` cũng tự động phân giải các bí danh như `claude-sonnet-4`, `gpt-4o`, `o3-mini` và hàng chục mô hình khác — không cần thay đổi cấu hình agent của bạn.

## Cơ chế bảo vệ chi tiêu hoạt động như thế nào

Mỗi gói dịch vụ xác định một **cửa sổ** ngân sách — một khoảng thời gian luân chuyển và mức chi tiêu tối đa
trong đó:

- **Starter**, **Lite**, **Essential**, **Pro**, **Power** và **Ultra** sử dụng cửa sổ **1 giờ**.

Trong cửa sổ, mức sử dụng của bạn tích lũy một chi phí nội bộ nhỏ. Khi chi phí nội bộ đó đạt đến mức giới hạn của cửa sổ, các yêu cầu sẽ tạm dừng cho đến khi cửa sổ được đặt lại.

Chỉ các lệnh gọi mô hình thông qua proxy mới được tính. Mỗi yêu cầu sẽ cộng vào tổng đang chạy của cửa sổ hiện tại dựa trên các token đã sử dụng. Khi cửa sổ được đặt lại, tổng cũng được đặt lại theo.

Nếu bạn chạm tới mức giới hạn và nhận được lỗi ngân sách, bạn có hai tùy chọn:

1. Chờ cửa sổ đặt lại (hiển thị trong dashboard của bạn).
2. Nâng cấp lên gói dịch vụ cao hơn để có mức giới hạn lớn hơn.

Xem [Lỗi liên quan đến gói dịch vụ](api-reference.md#errors) để biết lỗi ngân sách trông như thế nào.