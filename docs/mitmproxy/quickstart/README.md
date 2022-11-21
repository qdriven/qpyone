# Quick Start 快速开始

## mitmproxy 使用
```shell
poetry add mitmproxy
```
- mitmproxy
- mitmweb

```shell
mitmweb -s plugins/mitm/recorder.py
```
- mitmdump
```shell
mitmdump -s examples/simple/add_header.py
```

```shell
--proxy-server=127.0.0.1:8080 --ignore-certificate-errors
```

## mitmproxy ssh certification


## 启动mitmproxy 监听
