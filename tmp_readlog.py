import io
f = io.open('e:/Hunyuan3D-2-main/server_log.txt', encoding='utf-16-le', errors='replace')
all_text = f.read()
tail = all_text[-5000:]
for line in tail.splitlines():
    if line.strip():
        print(repr(line))
