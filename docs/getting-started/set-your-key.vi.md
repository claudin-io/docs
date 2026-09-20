# Thiết lập khóa API của bạn

Thiết lập khóa Claudin.io của bạn **một lần** như một biến môi trường và mọi công cụ trong
hướng dẫn này có thể tái sử dụng nó — không cần phải dán nó vào từng ứng dụng khách một cách thủ công.

Lấy khóa `sk-...` của bạn từ [bảng điều khiển](https://claudin.io/dashboard) (xem
[Tạo tài khoản của bạn](account.md)), sau đó thêm nó vào hồ sơ shell của bạn để nó có sẵn trong mọi terminal mới.

## macOS / Linux

=== "zsh (mặc định trên macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Thay `sk-...` bằng khóa thực của bạn. Không chắc bạn đang dùng shell nào? Chạy
`echo $SHELL`.

## Xác minh

```bash
echo $CLAUDINIO_API_KEY
```

Bạn sẽ thấy khóa của mình được in ra. Nếu trống, hãy mở một terminal mới hoặc
chạy lại lệnh `source` ở trên.

## Tại sao điều này hữu ích

Mọi tập lệnh **Quick setup** trong phần [Kết nối công cụ của bạn](../clients/opencode.md)
đều đọc `$CLAUDINIO_API_KEY`, vì vậy khi đã xuất nó, bạn có thể chạy bất kỳ tập lệnh nào
nguyên trạng — không cần thay `YOUR_API_KEY`. Các công cụ đọc trực tiếp biến môi trường
(Codex `env_key`, bất kỳ CLI tương thích OpenAI nào) cũng tự động nhận nó.

!!! warning "Xem khóa của bạn như mật khẩu"
    Bất kỳ ai có khóa này đều có thể tiêu tín dụng của bạn. Đừng commit `~/.zshrc`
    / `~/.bashrc` của bạn vào repo công khai. Nếu khóa bị lộ, thu hồi nó trong bảng
    điều khiển và export khóa mới.

---

Đã xuất khóa? Bây giờ hãy [thực hiện cuộc gọi đầu tiên](first-call.md) hoặc nhảy thẳng đến
[kết nối công cụ của bạn](../clients/opencode.md).