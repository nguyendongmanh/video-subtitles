from tasks import my_task

# Gửi 5 tác vụ không đồng bộ vào hàng đợi
results = [
    my_task.apply_async(args=[5]),  # Task mất 5 giây
    my_task.apply_async(args=[3]),  # Task mất 3 giây
    my_task.apply_async(args=[1]),  # Task mất 1 giây
    my_task.apply_async(args=[4]),  # Task mất 4 giây
    my_task.apply_async(args=[2]),   # Task mất 2 giây
]

# Theo dõi kết quả từng tác vụ
# for result in results:
#     result.wait()  # Đợi tác vụ hoàn thành
#     print(result.result)  # In kết quả ngay sau khi tác vụ hoàn thành

# while any(not result.ready() for result in results):  # Lặp đến khi tất cả hoàn thành
#     for result in results:
#         # if result.ready() and not result.successful():  # Kiểm tra tác vụ nào đã hoàn thành
#         #     print(f"Task completed with result: {result.result}")
#         if result.successful():  # Kiểm tra tác vụ nào đã hoàn thành
#             print(f"Task completed with result: {result.result}")
