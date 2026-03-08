# 常见问题排查 / 문제 해결 가이드

## Twitter/X: xreach CLI "fetch failed"

**症状 / 증상：** `xreach search` 或其他命令返回 "fetch failed" / `xreach search` 또는 다른 명령이 "fetch failed" 반환

**原因 / 원인：** xreach CLI 使用 Node.js 的 `undici` 库发请求。如果你的网络环境需要代理才能访问 x.com，需要明确传入代理参数。 / xreach CLI는 Node.js의 `undici` 라이브러리를 사용하여 요청을 보냅니다. 네트워크 환경에서 x.com에 접근하기 위해 프록시가 필요한 경우 프록시 파라미터를 명시적으로 전달해야 합니다.

**解决方案 / 해결 방법：**

### 方案 1：使用 --proxy 参数 / 방법 1: --proxy 파라미터 사용

```bash
xreach search "test" --auth-token "$AUTH_TOKEN" --ct0 "$CT0" --proxy "http://user:pass@host:port"
```

### 方案 2：使用全局代理工具 / 방법 2: 전역 프록시 도구 사용

让代理工具接管所有网络流量，这样 xreach 的请求也会走代理： / 프록시 도구가 모든 네트워크 트래픽을接管하도록 하여 xreach 요청도 프록시를 통해 전송:

```bash
# macOS — ClashX / Surge 开启"增强模式" / "향상된 모드" 활성화
# Linux — proxychains 或 tun2socks
proxychains xreach search "test" -n 1
```

### 方案 3：不用 xreach，用 Exa 搜索替代 / 방법 3: xreach 대신 Exa 검색 사용

xreach 不可用时，可以直接用 Exa 搜索 Twitter 内容： / xreach를 사용할 수 없을 때 Exa로 직접 Twitter 콘텐츠 검색:

```bash
mcporter call 'exa.web_search_exa(query: "site:x.com 搜索词", numResults: 5)'
```

### 方案 4：设置 HTTP_PROXY 环境变量 / 방법 4: HTTP_PROXY 환경변수 설정

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

xreach search "test"
```

> ⚠️ 注意 / 주의：Node.js 原生 fetch 不一定读取这些环境变量，推荐用方案 1 的 --proxy 参数。 / Node.js 네이티브 fetch는 이 환경변수를 반드시 읽지 않으므로 방법 1의 --proxy 파라미터 사용을 권장합니다.
