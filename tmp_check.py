import pathlib, os, sys
hf = pathlib.Path(os.path.expanduser('~/.cache/huggingface'))
results = []
for f in hf.rglob('*'):
    try:
        sz = f.stat().st_size
        if sz > 100*1024*1024 and f.is_file():
            results.append((sz, f))
    except:
        pass
for sz, p in sorted(results, reverse=True):
    sys.stdout.write(str(round(sz/1024/1024)) + ' MB | ' + str(p) + '\n')
    sys.stdout.flush()
sys.stdout.write('Total: ' + str(len(results)) + '\n')
