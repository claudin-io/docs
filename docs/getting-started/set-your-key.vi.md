# Thiết lập khóa API của bạn

Thiết lập khóa **Claudin.io** của bạn **một lần** dưới dạng biến môi trường và mọi công cụ trong hướng dẫn này có thể tái sử dụng nó — không cần phải dán thủ công vào từng client.

Lấy khóa `sk-...` của bạn từ [bảng điều khiển](https://claudin.io/dashboard) (xem [Tạo tài khoản](account.md)), sau đó thêm nó vào hồ sơ shell của bạn để nó có sẵn trong mọi terminal mới.

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

Thay thế `sk-...` bằng khóa thực của bạn. Không chắc bạn đang sử dụng shell nào? Chạy `echo $SHELL`.

## Xác minh

```bash
echo $CLAUDINIO_API_KEY
```

Bạn sẽ thấy khóa của mình được in ra. Nếu trống, hãy mở một terminal mới hoặc chạy lại lệnh `source` ở trên.

## Tại sao điều này hữu ích

Mọi tập lệnh **Thiết lập nhanh** trong phần [Kết nối công cụ của bạn](../clients/opencode.md) đều đọc `$CLAUDINIO_API_KEY`, vì vậy một khi nó được xuất, bạn có thể chạy bất kỳ tập lệnh nào trong số đó nguyên trạng — không có `YOUR_API_KEY` nào cần thay thế. Các công cụ đọc trực tiếp biến môi trường (Codex's `env_key`, bất kỳ CLI tương thích OpenAI nào) cũng tự động nhận nó.

!!! warning "Xem khóa của bạn như mật khẩu"
    Bất kỳ ai có khóa này đều có thể tiêu ngân sách gói của bạn. Đừng commit `~/.zshrc` / `~/.bashrc` của bạn vào repo công khai. Nếu khóa bị rò rỉ, hãy thu hồi nó trong bảng điều khiển và xuất một khóa mới.

---

Đã xuất khóa? Bây giờ hãy [thực hiện cuộc gọi đầu tiên](first-call.md) hoặc chuyển thẳng đến [kết nối công cụ của bạn](../clients/opencode.md).