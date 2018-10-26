#_*_coding=utf8_*_
"""
author:ts
"""

import autoit

#设置焦#点
autoit.control_focus("打开", "[Class:Edit; instance:1]")
#输入文本
autoit.control_set_text(
    "打开",
    "[Class:Edit; instance:1]",
    r"C:\Users\Administrator\Desktop\226523.jpg"
)
# 单击按钮
autoit.control_click("打开", "[Class:Button; instance:1]")

# 根据窗口聚丙来单击
# autoit.control_click_by_handle()
# 原型control_click_by_handle(hwnd, h_ctrl, **kwargs):
# hwnd:窗口聚丙
# h_ctrl:类型
# kwargs:
# button = kwargs.get("button", "left")
# clicks = kwargs.get("clicks", 1)
# x = kwargs.get("x", INTDEFAULT)
# y = kwargs.get("y", INTDEFAULT)

# autoit.send()
# 原型:send(send_text, mode=0)
# send_text:要发送的文本
# mode:0 字符串
# mode:1 一行数据
