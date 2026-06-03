# Danh sách đơn hàng ban đầu
express_order = ["GE101", "GE102-WORNG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_order.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_order.insert(0,"GE000-FAST")
print("Danh sách sau khi chèn là: ", express_order)

# Sửa mã đơn hàng bị nhập sai
express_order[1] = "GE102-UPDATE"

# Xóa đơn hàng bị khách hủy
express_order.remove("GE103-CANCEL")

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order =  express_order.pop(0)

print("Danh sách đơn hàng còn lại: ", express_order)
print("Đơn hàng đang giao: ", current_order)
