zh2Hans = {
    '顯著': '显著',
    '土著': '土著',
    '印表機': '打印机',
    '說明檔案': '帮助文件',
    "瀋": "沈",
    "畫": "划",
    "鍾": "钟",
    "靦": "腼",
    "餘": "余"}
print(zh2Hans)
zh2Hans["印表機"]='激动'
zh2Hans["乐凯"]="可乐"
print(zh2Hans)
n = input()
print(zh2Hans[n])
print(zh2Hans.keys())
for key in zh2Hans:
    print(key)
