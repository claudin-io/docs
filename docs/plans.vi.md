# Gói dịch vụ & giới hạn

Mọi gói dịch vụ của Claudin.io đều có **sử dụng không giới hạn** với **mức bảo vệ chi tiêu**.
Bạn sẽ không bị tính phí theo token hay theo yêu cầu — bạn trả một mức giá cố định hàng tháng và
sử dụng thoải mái. Mức giới hạn chỉ tồn tại để ngăn một agent chạy mất kiểm soát (ví dụ: một vòng lặp công cụ vô tận) làm cạn kiệt gói dịch vụ của bạn.

## Các gói dịch vụ

| Gói dịch vụ | Giá | Bảo vệ chi tiêu | Phù hợp nhất |
| --- | --- | --- | --- |
| **Essential** | $19 / tháng hoặc $189 / năm | $2,00 / giờ | Chất lượng cho sử dụng hàng ngày |
| **Pro** ★ | $39 / tháng hoặc $389 / năm | $4,00 / giờ | Quy trình làm việc agent chuyên sâu |
| **Ultra** | $99 / tháng hoặc $989 / năm | $10,00 / giờ | Sức mạnh tối đa, nhóm & sản xuất |

!!! tip "Hầu hết mọi người không bao giờ chạm tới mức giới hạn"
    Mức giới hạn theo giờ khá hào phóng cho công việc tương tác thông thường. Bạn thường chỉ
    chạm tới nó nếu một agent rơi vào vòng lặp chặt — đó chính xác là lúc bạn *muốn* có một cái phanh.

## Nên chọn mô hình nào? Claudinio vs Claudius

Chúng tôi cung cấp hai mô hình chính cho coding agent của bạn:

| Mô hình | Backend | Trường hợp sử dụng | Khuyến nghị cho |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Nhanh, cân bằng, tiết kiệm | Code hàng ngày, dự án cá nhân, code tổng quát | **Tất cả gói dịch vụ** (Essential đến Ultra) |
| **claudius** ★ | Cao cấp, suy luận sâu | Tác vụ phức tạp, suy luận sâu, quy trình agent chuyên sâu | **Pro và Ultra** |
!!! warning "`claudius` có trong Pro và Ultra"
    Trên **Essential**, một yêu cầu gọi tên `claudius` không bị từ chối — nó được `claudinio` phục vụ và tính theo giá của `claudinio`. Tác nhân của bạn vẫn chạy, và bạn không bao giờ bị tính giá cao cấp trên gói không bao gồm nó.

    Trên **Pro** và **Ultra**, hãy nhớ hạn mức được tính **bằng đô la, không phải số yêu cầu**: cùng khối lượng công việc trên `claudius` tiêu tốn khoảng sáu lần. Trên Pro ($4/giờ) là khoảng 70 yêu cầu premium trước khi hết giờ; trên Ultra ($10/giờ), khoảng 175. Hãy giữ `claudinio` làm mặc định và chỉ dùng `claudius` khi bạn thực sự cần khả năng suy luận.

### Nói thẳng

Đây là thực tế: `claudinio` mang lại chất lượng tương đương Claude Sonnet cho việc lập trình hằng ngày với **một phần nhỏ chi phí nội bộ**. Trên gói Essential, bạn có thể thực hiện **hàng trăm yêu cầu mỗi giờ** với nó — đó là lý do mọi gói đều được xây dựng quanh mô hình này.

| Chỉ số | claudinio | claudius |
| --- | --- | --- |
| Tác động đến ngân sách theo giờ | Thấp — kéo dài hơn nhiều | Cao — 6x mỗi yêu cầu |
| Trường hợp sử dụng | Code hàng ngày, dự án cá nhân | Suy luận nặng, agent phức tạp |

**Nguyên tắc vàng:** Cấu hình agent của bạn (Claude Code, Cursor, Continue, v.v.) với `claudinio` làm mô hình mặc định. Chỉ chuyển sang `claudius` khi bạn thực sự cần thêm sức mạnh suy luận. Đối với các dự án cá nhân, `claudinio` là **tất cả những gì bạn cần** và có lẽ **còn hơn cả bạn mong đợi**.

> 💡 Mẹo: Cả hai mô hình đều hoạt động với mọi tác nhân lập trình phổ biến. Đặt `model=claudinio` trong cấu hình tác nhân của bạn — hoặc `model=claudius` nếu bạn dùng Pro hay Ultra. `claudinio` cũng tự động phân giải các bí danh như `claude-sonnet-4`, `gpt-4o`, `o3-mini` và hàng chục tên khác — không cần đổi cấu hình tác nhân.

## Cơ chế bảo vệ chi tiêu hoạt động như thế nào

Mỗi gói dịch vụ xác định một **cửa sổ** ngân sách — một khoảng thời gian luân chuyển và mức chi tiêu tối đa
trong đó:

- **Essential**, **Pro** và **Ultra** sử dụng cửa sổ **1 giờ**.

Trong cửa sổ, mức sử dụng của bạn tích lũy một chi phí nội bộ nhỏ. Khi chi phí nội bộ đó đạt đến mức giới hạn của cửa sổ, các yêu cầu sẽ tạm dừng cho đến khi cửa sổ được đặt lại.

Chỉ các lệnh gọi mô hình thông qua proxy mới được tính. Mỗi yêu cầu sẽ cộng vào tổng đang chạy của cửa sổ hiện tại dựa trên các token đã sử dụng. Khi cửa sổ được đặt lại, tổng cũng được đặt lại theo.

Nếu bạn chạm tới mức giới hạn và nhận được lỗi ngân sách, bạn có hai tùy chọn:

1. Chờ cửa sổ đặt lại (hiển thị trong dashboard của bạn).
2. Nâng cấp lên gói dịch vụ cao hơn để có mức giới hạn lớn hơn.

Xem [Lỗi liên quan đến gói dịch vụ](api-reference.md#errors) để biết lỗi ngân sách trông như thế nào.