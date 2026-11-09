## --- DSA1 UPDATE ---

**DSA1 | PARTIAL — TIME | 33:25.83 | Level: 3.2/5**

**Date:** 08/11/2026

### Focus Topic

HT-01 — Hash Table Foundation: khởi tạo bucket và cài đặt hàm băm chuỗi.

### Session Notes

- Thống nhất kiến trúc Hash Table sử dụng **separate chaining**, với 16 bucket ban đầu.
- Tự viết `class HashTable` và `__init__()`:
  - `_capacity = 16`
  - `_size = 0`
  - `_buckets` chứa 16 list rỗng độc lập.
- Tự triển khai `_hash(self, key)` theo công thức:
  `index = (index * 10 + ord(char)) % self._capacity`
- Đã chạy thành công trên terminal:
  - `_capacity` trả về `16`.
  - `_hash("FPT")` trả về `12`.
- Hiểu rõ hơn các khái niệm Python:
  - `class` và object (instance).
  - `__init__()` và `self`.
  - Sự khác nhau giữa `HashTable` và `HashTable()`.
  - Cách truy cập thuộc tính của object.
- Đã tìm hiểu logic của `set()` nhưng chưa bắt đầu triển khai.

### Minhyi Notes

- Ban đầu nhầm lẫn giữa việc tham chiếu class và tạo object.
- Gặp `AttributeError` khi truy cập `_capacity` trực tiếp thông qua class.
- Gặp `TypeError` khi truyền đối số vào constructor không nhận tham số.
- Ban đầu thiếu bước khởi tạo `index = 0` trong `_hash()`.
- Sau khi được giải thích, đã sửa code và chạy thành công.
- Chủ động quyết định tạm hoãn kiểm tra kiểu dữ liệu của key để ưu tiên tiến độ dự án.
- Code được tự viết dựa trên yêu cầu và hướng dẫn, không sử dụng nguyên class do AI tạo.

### Key Lesson

> Class là bản thiết kế, còn object là thực thể được tạo từ class. Muốn sử dụng các thuộc tính được khởi tạo bởi `__init__()`, cần tạo object bằng cách gọi class với `()`.

### Performance Evaluation

- Concept understanding: 3.0/5
- Coding correctness: 3.5/5
- Reasoning / problem decomposition: 3.0/5
- Independence: 3.5/5
- Debugging: 3.0/5

**Final Score: 3.2/5**

### Blank-Screen Performance

- Tự viết `__init__()` và `_hash()` trong VS Code.
- Không nhận hoặc sao chép nguyên class hoàn chỉnh từ AI.
- Công thức hash và yêu cầu thiết kế được cung cấp trước.
- AI hỗ trợ giải thích class/instance, chẩn đoán lỗi và chỉ ra bước khởi tạo `index = 0` còn thiếu.
- Chưa thực hiện bài kiểm tra viết lại độc lập sau khi được hướng dẫn.

**Independence Assessment:** Có khả năng tự triển khai các cấu trúc Python cơ bản theo yêu cầu, nhưng vẫn cần hỗ trợ khi gặp lỗi liên quan đến object và phương thức.

### Progress Update

- Project: Final Project DSA — Multi-User Stock Trade Management System
- Component: HT-01 — Hash Table
- Session: DSA1
- Current Phase: Hash Table Foundation
- Current Position: Đã triển khai khởi tạo Hash Table và hàm băm chuỗi.

**Completed:**
- `__init__()`
- `_hash()` với input chuỗi hợp lệ

**Verified:**
- Capacity ban đầu bằng 16.
- `_hash("FPT") = 12`.

**Not Yet Completed / Verified:**
- Kiểm tra key phải thuộc kiểu `str`.
- Kiểm thử tính độc lập của các bucket bằng mutation.
- Kiểm thử collision với `AAK` và `ABA`.
- `set()`, `get()`, `delete()`.
- `__contains__()`, `__len__()`.
- `items()`, `values()`.
- Resize và rehash.
- Bộ kiểm thử `unittest`.

### Critical Weakness

> Chưa thực sự vững sự khác biệt giữa class và instance trong Python. Cần củng cố kiến thức này trong quá trình tự triển khai các phương thức của Hash Table.

### Session Verdict

**PARTIAL — TIME**

Đã triển khai và chạy thành công phần khởi tạo cùng hàm băm cơ bản.

Tuy nhiên, chưa hoàn thành toàn bộ yêu cầu của `_hash()` và chưa bắt đầu `set()`.

HT-01 chưa được xem là hoàn thành.

### Next Session

**DSA2 — Hash Table: `set(key, value)`**

Mục tiêu:
- Tự triển khai thao tác thêm key mới.
- Cập nhật value của key đã tồn tại.
- Xử lý collision bằng separate chaining.
- Đảm bảo `_size` chỉ tăng khi thêm key mới.
- Kiểm tra insert và update với các key có cùng hash.

**Next Starting Point:** Tự viết phương thức `set()` dựa trên `__init__()` và `_hash()` hiện có.

Việc kiểm tra kiểu key được giữ trong danh sách cần hoàn thiện trước khi review toàn bộ HT-01.