# Agent Reach — Installation Guide / 설치 가이드

## For Humans / 사용자용

이 문장을 AI Agent에 복사하세요:

```text
Agent Reach 설치 도와줘: https://raw.githubusercontent.com/cool25th/Agent-Reach-Kr/main/docs/install.md
```

> 🛡️ **Security-conscious? / 보안에 신경 쓰시나요?** Use safe mode — it won't auto-install system packages / 안전 모드를 사용하세요 — 시스템 패키지를 자동으로 설치하지 않습니다:
> ```text
> Agent Reach 설치 도와줘 (안전 모드): https://raw.githubusercontent.com/cool25th/Agent-Reach-Kr/main/docs/install.md
> 설치할 때 --safe 파라미터를 사용해줘
> ```

---

## For AI Agents / AI Agent용

### Goal / 목표

Install Agent Reach and all upstream tools so your user's agent has full internet access. After installation, you'll use the upstream tools directly (xreach CLI, yt-dlp, mcporter, gh CLI, etc.) — Agent Reach is just the installer and health checker.
Agent Reach와 모든 상위 도구를 설치하여 사용자의 에이전트가 완전한 인터넷 액세스를 할 수 있도록 합니다. 설치 후에는 상위 도구를 직접 사용하게 됩니다 (xreach CLI, yt-dlp, mcporter, gh CLI 등) — Agent Reach는 단지 설치 및 상태 확인 도구일 뿐입니다.

### ⚠️ Boundaries / 경계

When fixing issues, stay within these limits / 문제를 해결할 때 다음 제한 내에서 작동하세요:

- **DO NOT** run commands with `sudo` unless the user explicitly approved / **사용자가 명시적으로 승인하지 않은 한** `sudo`로 명령을 실행하지 마세요
- **DO NOT** modify system files outside `~/.agent-reach/` / `~/.agent-reach/` 외부의 시스템 파일을 수정하지 마세요
- **DO NOT** install packages not listed in this guide / 이 가이드에 나열되지 않은 패키지를 설치하지 마세요
- **DO NOT** disable firewalls, security settings, or system protections / 방화벽, 보안 설정 또는 시스템 보호를 비활성화하지 마세요
- **DO NOT** clone repos, create files, or run commands inside the agent workspace / working directory / 에이전트 워크스페이스/작업 디렉토리 내에서 리포지토리를 복제하거나 파일을 생성하거나 명령을 실행하지 마세요
- If something requires elevated permissions, **tell the user** what's needed and let them decide / 상승된 권한이 필요한 경우 사용자에게 **알리고** 사용자가 결정하도록 하세요

### 📁 Directory Rules / 디렉토리 규칙

All Agent Reach files go in dedicated directories — **never in the agent workspace** / 모든 Agent Reach 파일은 전용 디렉토리에 들어갑니다 — **절대 에이전트 워크스페이스에 두지 마세요**:

| Purpose / 용도 | Directory / 디렉토리 | Example / 예시 |
|---------|-----------|---------|
| Config & tokens / 설정 및 토큰 | `~/.agent-reach/` | `~/.agent-reach/config.json` |
| Upstream tool repos / 상위 도구 리포지토리 | `~/.agent-reach/tools/` | `~/.agent-reach/tools/douyin-mcp-server/` |
| Temporary files / 임시 파일 | `/tmp/` | `/tmp/yt-dlp-output/` |
| Skills / 스킬 | `~/.openclaw/skills/agent-reach/` | SKILL.md |

**Why? / 이유는 무엇인가요?** If you clone repos or create files in the workspace, it pollutes the user's project directory and can break their agent over time. Keep the workspace clean. / 워크스페이스에 리포지토리를 복제하거나 파일을 생성하면 사용자의 프로젝트 디렉토리가 오염되어 시간이 지나면서 에이전트가 중단될 수 있습니다. 워크스페이스를 깨끗하게 유지하세요.

### Step 1: Install / 1단계: 설치

**Default (fully automatic) / 기본값 (완전 자동):**

```bash
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```

This auto-installs system dependencies (gh CLI, Node.js, mcporter, xreach), configures Exa search, detects environment, and tests all channels.
이 명령은 시스템 종속성(gh CLI, Node.js, mcporter, xreach)을 자동으로 설치하고, Exa 검색을 구성하며, 환경을 감지하고 모든 채널을 테스트합니다.

**Safe mode (no automatic system changes) / 안전 모드 (자동 시스템 변경 없음):**

If the user asked for safe mode, or you're on a production machine / 사용자가 안전 모드를 요청했거나 프로덕션 머신인 경우:

```bash
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto --safe
```

Safe mode checks what's installed and tells you what's missing, but doesn't auto-install system packages. You can then install each dependency manually.
안전 모드는 설치된 것을 확인하고 누락된 항목을 알려주지만, 시스템 패키지를 자동으로 설치하지는 않습니다. 그런 다음 각 종속성을 수동으로 설치할 수 있습니다.

**Dry run (preview only) / 드라이 런 (미리보기만):**

```bash
agent-reach install --env=auto --dry-run
```

Shows what would be done without making any changes.
변경 사항 없이 수행될 작업을 표시합니다.

**Read the output carefully / 출력을 주의 깊게 읽은 다음**, then run / 아래를 실행하세요:

```bash
agent-reach doctor
```

### Step 2: Fix what's broken / 2단계: 문제 수정

`agent-reach doctor` shows you which channels are active and which aren't.
`agent-reach doctor`는 어떤 채널이 활성화되어 있고 어떤 채널이 비활성화되어 있는지 보여줍니다.

Try to get as many channels to ✅ as possible. If something failed during install or shows as ❌/⚠️ in doctor, diagnose the problem and try to fix it — but stay within the boundaries above. If a fix requires elevated permissions or system changes, ask the user first.
가능한 한 많은 채널을 ✅로 만드세요. 설치 중 실패했거나 doctor에서 ❌/⚠️로 표시되는 경우 문제를 진단하고 수정을 시도하세요 — 단 위 경계 내에서만 작동하세요. 수정에 상승된 권한이나 시스템 변경이 필요한 경우 먼저 사용자에게 문의하세요.

Only ask the user when you genuinely need their input (credentials, permissions, etc.).
실제로 사용자 입력이 필요할 때만(자격 증명, 권한 등) 사용자에게 요청하세요.

### Step 3: Configure things that need user input / 3단계: 사용자 입력이 필요한 항목 구성

Some channels need credentials only the user can provide. Based on the doctor output, ask for what's missing:
일부 채널은 사용자만 제공할 수 있는 자격 증명이 필요합니다. doctor 출력을 기반으로 누락된 항목을 요청하세요:

> 🔒 **Security tip / 보안 팁:** For platforms that need cookies (Twitter, XiaoHongShu), we recommend using a **dedicated/secondary account** rather than your main account. Cookie-based auth carries two risks / 쿠키가 필요한 플랫폼(Twitter, XiaoHongShu)의 경우 **전용/보조 계정**을 사용하는 것이 좋습니다. 메인 계정 대신 보조 계정을 사용하세요. 쿠키 기반 인증에는 두 가지 위험이 있습니다:
> 1. **Account ban / 계정 정지** — platforms may detect non-browser API calls and restrict or ban the account / 플랫폼에서 비브라우저 API 호출을 감지하고 계정을 제한하거나 정지할 수 있습니다
> 2. **Credential exposure / 자격 증명 노출** — cookies grant full account access; using a secondary account limits the blast radius if credentials are ever compromised / 쿠키는 전체 계정 액세스 권한을 부여합니다. 자격 증명이 유출되더라도 보조 계정을 사용하면 영향 범위를 제한할 수 있습니다

> 🍪 **Cookie 导入（所有需要登录的平台通用）/ 쿠키 가져오기 (로그인이 필요한 모든 플랫폼 공통):**
>
> 所有需要 Cookie 的平台（Twitter、小红书等），**优先使用 Cookie-Editor 导入**，这是最简单最可靠的方式 / 쿠키가 필요한 모든 플랫폼(Twitter, XiaoHongShu 등)의 경우 **Cookie-Editor 가져오기를 우선 사용하세요**. 가장 간단하고 신뢰할 수 있는 방법입니다:
> 1. 用户在自己的浏览器上登录对应平台 / 사용자가 자신의 브라우저에서 해당 플랫폼에 로그인
> 2. 安装 [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) Chrome 插件 / [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) Chrome 확장 프로그램 설치
> 3. 点击插件 → Export → Header String / 확장 프로그램 클릭 → Export → Header String
> 4. 把导出的字符串发给 Agent / 내보낸 문자열을 Agent에 전송
>
> **本地电脑用户**也可以用 `agent-reach configure --from-browser chrome` 一键自动提取（支持 Twitter + 小红书）。 / **로컬 컴퓨터 사용자**는 `agent-reach configure --from-browser chrome` 명령으로 일회용 자동 추출도 가능합니다(Twitter + XiaoHongShu 지원).

**Twitter search & posting / Twitter 검색 및 게시:**
> "To unlock Twitter search, I need your Twitter cookies. Install the Cookie-Editor Chrome extension, go to x.com/twitter.com, click the extension → Export → Header String, and paste it to me." / "Twitter 검색을 잠금 해제하려면 Twitter 쿠키가 필요합니다. Cookie-Editor Chrome 확장 프로그램을 설치하고, x.com/twitter.com으로 이동한 다음 확장 프로그램을 클릭 → Export → Header String을 선택하여 저에게 붙여넣으세요."

```bash
agent-reach configure twitter-cookies "PASTED_STRING"
```

> **代理说明（中国大陆等需要翻墙的网络环境）/ 프록시 설명 (중국 본토 등 프록시가 필요한 네트워크 환경):**
>
> xreach CLI 使用 Node.js 原生 `fetch()`，默认不走系统代理（`HTTP_PROXY`/`HTTPS_PROXY`）。 / xreach CLI는 Node.js 네이티브 `fetch()`를 사용하며, 기본적으로 시스템 프록시(`HTTP_PROXY`/`HTTPS_PROXY`)를 따르지 않습니다.
> Agent Reach 已内置解决方案：安装时会自动安装 `undici`（`npm install -g undici`）， / Agent Reach에 내장된 솔루션이 있습니다: 설치 시 `undici`(`npm install -g undici`)를 자동으로 설치하고,
> 运行 xreach 时自动注入 `EnvHttpProxyAgent`，让 fetch 走用户配置的代理。 / xreach 실행 시 `EnvHttpProxyAgent`를 자동으로 주입하여 fetch가 사용자가 구성한 프록시를 따르도록 합니다.
>
> **你（Agent）需要做的：** / **(Agent) 귀하가 해야 할 일:**
> 1. 确认 `undici` 已全局安装：`npm list -g undici`，没有就装：`npm install -g undici` / `undici`가 전역으로 설치되었는지 확인: `npm list -g undici`, 설치되지 않았으면 설치: `npm install -g undici`
> 2. 确认用户配了代理：`agent-reach configure proxy http://user:pass@ip:port` / 사용자가 프록시를 구성했는지 확인: `agent-reach configure proxy http://user:pass@ip:port`
> 3. Agent Reach 会自动处理剩下的，不需要用户做额外操作 / Agent Reach가 나머지를 자동으로 처리하므로 사용자가 추가 작업을 할 필요가 없습니다
>
> 如果用户报告 "fetch failed"，参考 [troubleshooting.md](troubleshooting.md) / 사용자가 "fetch failed"를 보고하면 [troubleshooting.md](troubleshooting.md)를 참조하세요

**Reddit & Bilibili full access (server users) / Reddit & Bilibili 전체 액세스 (서버 사용자):**
> "Reddit and Bilibili block server IPs. To unlock full access, I need a residential proxy. You can get one at https://webshare.io ($1/month). Send me the proxy address." / "Reddit과 Bilibili는 서버 IP를 차단합니다. 전체 액세스를 잠금 해제하려면 Residential(주거용) 프록시가 필요합니다. https://webshare.io에서 구할 수 있습니다(월 $1). 프록시 주소를 저에게 보내주세요."

```bash
agent-reach configure proxy http://user:pass@ip:port
```

**XiaoHongShu / 小红书 (需要 Docker) / (Docker 필요):**
> "小红书需要一个 MCP 服务。需要你的机器上有 Docker。安装好 Docker 后我来搞定剩下的。" / "XiaoHongShu는 MCP 서비스가 필요합니다. 머신에 Docker가 설치되어 있어야 합니다. Docker를 설치한 후 나머지는 제가 처리하겠습니다."

```bash
docker run -d --name xiaohongshu-mcp -p 18060:18060 xpzouying/xiaohongshu-mcp
mcporter config add xiaohongshu http://localhost:18060/mcp
```

> 如果在服务器上，建议加代理避免 IP 风控： / 서버인 경우 IP 리스크 방지를 위해 프록시를 추가하는 것이 좋습니다:
> `docker run -d --name xiaohongshu-mcp -p 18060:18060 -e XHS_PROXY=http://user:pass@ip:port xpzouying/xiaohongshu-mcp`
>
> **登录方式（优先用 Cookie-Editor，最简单）：** / **로그인 방법 (Cookie-Editor 우선, 가장 간단):**
> 1. 用户在自己的浏览器登录小红书 (xiaohongshu.com) / 사용자가 자신의 브라우저에서 샤오홍슈(xiaohongshu.com)에 로그인
> 2. 用 [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) 插件导出 Cookie（JSON 或 Header String 格式均可） / [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) 확장 프로그램으로 Cookie를 내보냅니다(JSON 또는 Header String 모두 가능)
> 3. 把 Cookie 字符串发给 Agent / 쿠키 문자열을 Agent에 전달
> 4. Agent 运行命令完成登录： / Agent가 아래 명령으로 로그인을 마무리합니다
>
> **备选：** 本地电脑如果有浏览器，也可以打开 http://localhost:18060 扫码登录。 / **대안:** 로컬 컴퓨터에 브라우저가 있는 경우 http://localhost:18060을 열어 QR 코드로 로그인할 수도 있습니다.

```bash
# JSON 格式（Cookie-Editor → Export → JSON）
agent-reach configure xhs-cookies '[{"name":"web_session","value":"xxx","domain":".xiaohongshu.com",...}]'

# 或 Header String 格式（Cookie-Editor → Export → Header String）
agent-reach configure xhs-cookies "key1=val1; key2=val2; ..."
```

**微博 / Weibo (mcp-server-weibo) / 웨이보 (mcp-server-weibo):**
> "微博已默认安装，装好即用。可搜索微博内容、查看热搜、获取用户动态和评论。" / "웨이보는 기본 설치 대상으로 바로 사용할 수 있습니다. 콘텐츠 검색, 인기 검색어, 사용자 피드, 댓글 조회를 지원합니다."

如果自动安装失败，手动安装： / 자동 설치가 실패하면 수동으로 설치하세요:

```bash
pip install git+https://github.com/Panniantong/mcp-server-weibo.git
mcporter config add weibo --command 'mcp-server-weibo'
```

> 无需登录、无需 Cookie、无需代理。海外服务器通常也可以直接访问。 / 로그인, Cookie, 프록시 없이 동작하며 해외 서버에서도 대체로 바로 사용할 수 있습니다.

**抖音 / Douyin (douyin-mcp-server):**
> "抖音视频解析需要一个 MCP 服务。安装 douyin-mcp-server 后即可解析视频、获取无水印下载链接。" / "Douyin 동영상 파싱에 MCP 서비스가 필요합니다. douyin-mcp-server를 설치하면 동영상을 파싱하고 워터마크 없는 다운로드 링크를 얻을 수 있습니다."

```bash
# 1. 安装 / 설치
pip install douyin-mcp-server

# 2. 启动 HTTP 服务（端口 18070） / HTTP 서비스 시작 (포트 18070)
# 方式一：用 uv（推荐） / 방법 1: uv 사용 (권장)
mkdir -p ~/.agent-reach/tools && cd ~/.agent-reach/tools
git clone https://github.com/yzfly/douyin-mcp-server.git && cd douyin-mcp-server
uv sync && uv run python run_http.py

# 方式二：直接用 Python 启动 / 방법 2: Python으로 직접 시작
python -c "
from douyin_mcp_server.server import mcp
mcp.settings.host = '127.0.0.1'
mcp.settings.port = 18070
mcp.run(transport='streamable-http')
"

# 3. 注册到 mcporter / mcporter에 등록
mcporter config add douyin http://localhost:18070/mcp
```

> 无需认证即可解析视频信息和获取下载链接。 / 인증 없이 동영상 정보를 파싱하고 다운로드 링크를 얻을 수 있습니다.
> 如需 AI 语音识别提取文案功能，需要配置 SiliconFlow API Key（`export API_KEY="sk-xxx"`）。 / AI 음성 인식으로 문안을 추출하려면 SiliconFlow API Key(`export API_KEY="sk-xxx"`)를 구성해야 합니다.
>
> 详见 https://github.com/yzfly/douyin-mcp-server / 자세한 내용은 https://github.com/yzfly/douyin-mcp-server를 참조하세요

**LinkedIn (可选 — linkedin-scraper-mcp) / (선택 사항 — linkedin-scraper-mcp):**
> "LinkedIn 基本内容可通过 Jina Reader 读取。完整功能（Profile 详情、职位搜索）需要 linkedin-scraper-mcp。" / "LinkedIn 기본 콘텐츠는 Jina Reader로 읽을 수 있습니다. 전체 기능(Profile 상세, 직책 검색)에는 linkedin-scraper-mcp가 필요합니다."

```bash
pip install linkedin-scraper-mcp
```

> **登录方式（需要浏览器界面）：** / **로그인 방법 (브라우저 인터페이스 필요):**
>
> linkedin-scraper-mcp 使用 Chromium 浏览器登录，需要你能看到浏览器窗口。 / linkedin-scraper-mcp는 Chromium 브라우저로 로그인하므로 브라우저 창을 볼 수 있어야 합니다.
>
> - **本地电脑（有桌面）：** 直接运行： / **로컬 컴퓨터 (데스크톱 있음):** 직접 실행:
>   ```bash
>   linkedin-scraper-mcp --login --no-headless
>   ```
>   浏览器会弹出来，手动登录 LinkedIn 即可。 / 브라우저가 팝업되고 수동으로 LinkedIn에 로그인합니다.
>
> - **服务器（无 UI）：** 需要通过 VNC 远程桌面操作： / **서버 (UI 없음):** VNC 원격 데스크톱을 통해 작업해야 합니다:
>   ```bash
>   # 1. 服务器上安装并启动 VNC（如已有可跳过） / 서버에 VNC 설치 및 시작 (이미 있는 경우 생략)
>   apt install -y tigervnc-standalone-server
>   vncserver :1 -geometry 1280x720
>
>   # 2. 用 VNC 客户端连接 服务器IP:5901 / VNC 클라이언트로 서버IP:5901 연결
>
>   # 3. 在 VNC 桌面的终端里运行： / VNC 데스크톱의 터미널에서 실행:
>   export DISPLAY=:1
>   linkedin-scraper-mcp --login --no-headless
>   ```
>   在 VNC 里看到浏览器后手动登录。登录成功后 session 会保存到 `~/.linkedin-mcp/profile/`。 / VNC에서 브라우저를 보고 수동으로 로그인합니다. 로그인 성공 후 세션이 `~/.linkedin-mcp/profile/`에 저장됩니다.
>
> **登录后启动 MCP 服务：** / **로그인 후 MCP 서비스 시작:**
> ```bash
> linkedin-scraper-mcp --transport streamable-http --port 8001
> mcporter config add linkedin http://localhost:8001/mcp
> ```
>
> 详见 https://github.com/stickerdaniel/linkedin-mcp-server / 자세한 내용은 https://github.com/stickerdaniel/linkedin-mcp-server를 참조하세요

**Boss直聘 (可选 — mcp-bosszp) / (선택 사항 — mcp-bosszp):**
> "Boss直聘职位页面可直接读取。完整搜索和打招呼功能需要 mcp-bosszp。" / "Boss直聘(보스즈핑) 채용 공고 페이지는 직접 읽을 수 있습니다. 전체 검색 및 메시지 기능에는 mcp-bosszp가 필요합니다."

```bash
mkdir -p ~/.agent-reach/tools && cd ~/.agent-reach/tools
git clone https://github.com/mucsbr/mcp-bosszp.git && cd mcp-bosszp
pip install -r requirements.txt && playwright install chromium
```

> **登录方式（手机 App 扫码）：** / **로그인 방법 (모바일 App QR 코드 스캔):**
>
> mcp-bosszp 使用二维码登录，需要 Boss直聘 App 扫码。 / mcp-bosszp는 QR 코드 로그인을 사용하며 Boss直聘(보스즈핑) App으로 스캔해야 합니다.
>
> ```bash
> # 1. 启动 MCP 服务 / MCP 서비스 시작
> python boss_zhipin_fastmcp_v2.py
>
> # 2. 通过 MCP 触发登录（会生成二维码图片） / MCP를 통해 로그인 트리거 (QR 코드 이미지 생성)
> mcporter call 'bosszhipin.start_login()'
>
> # 3. 浏览器打开二维码图片（服务器上用 http://服务器IP:8000/static/qrcode_xxx.png） / 브라우저에서 QR 코드 이미지 열기 (서버인 경우 http://서버IP:8000/static/qrcode_xxx.png)
> # 4. 用 Boss直聘 App 扫码确认 / Boss直聘(보스즈핑) App으로 스캔하여 확인
> ```
>
> 扫码成功后 session 自动保存，之后可以搜索职位和自动打招呼。 / 스캔 성공 후 세션이 자동으로 저장되며 그 후 채용 공고 검색 및 자동 메시지를 보낼 수 있습니다.
>
> 或用 Docker：`docker-compose up -d` / 또는 Docker 사용: `docker-compose up -d`
>
> 详见 https://github.com/mucsbr/mcp-bosszp / 자세한 내용은 https://github.com/mucsbr/mcp-bosszp를 참조하세요

### Step 4: Final check / 4단계: 최종 확인

Run `agent-reach doctor` one final time and report the results to your user.
`agent-reach doctor`를 한 번 더 실행하고 결과를 사용자에게 보고하세요.

### Step 5: Set up daily monitoring (OpenClaw only) / 5단계: 일일 모니터링 설정 (OpenClaw만 해당)

If you are running inside **OpenClaw**, ask your user / **OpenClaw** 내에서 실행 중인 경우 사용자에게 물어보세요:

> "Agent Reach 安装好了。要不要我设一个每天自动检查的任务？它会帮你盯着这些渠道是否正常、有没有新版本。有问题才会通知你，没问题不打扰。" / "Agent Reach가 설치되었습니다. 매일 자동으로 확인하는 작업을 설정할까요? 이러한 채널이 정상인지, 새 버전이 있는지 확인해 드립니다. 문제가 있을 때만 알려드리고, 문제가 없으면 방해하지 않습니다."

If the user agrees, create a **cron job** (daily, `sessionTarget: "isolated"`, `delivery: "announce"`) with this task / 사용자가 동의하면 다음 작업으로 **cron job**을 생성하세요 (매일, `sessionTarget: "isolated"`, `delivery: "announce"`):

```
运行 agent-reach watch 命令。 / agent-reach watch 명령을 실행하세요.
如果输出包含"全部正常"，不需要通知用户，静默结束。 / 출력에 "모두 정상"이 포함된 경우 사용자에게 알리지 않고 조용히 종료합니다.
如果输出包含问题（❌ ⚠️）或新版本（🆕），把完整报告发给用户，并建议修复方案。 / 출력에 문제(❌ ⚠️) 또는 새 버전(🆕)이 포함된 경우 전체 보고서를 사용자에게 보내고 수정 방안을 제안합니다.
如果有新版本可用，问用户是否要升级（升级命令：pip install --upgrade https://github.com/Panniantong/agent-reach/archive/main.zip）。 / 새 버전을 사용할 수 있는 경우 사용자에게 업그레이드할지 물어보세요(업그레이드 명령: pip install --upgrade https://github.com/Panniantong/agent-reach/archive/main.zip).
```

If the user wants a different agent to handle it, let them choose / 사용자가 다른 에이전트가 처리하기를 원하면 사용자가 선택하도록 하세요.

---

## Quick Reference / 빠른 참조

| Command / 명령 | What it does / 기능 |
|---------|-------------|
| `agent-reach install --env=auto` | Full auto-setup (installs deps + configures) / 완전 자동 설정 (종속성 설치 + 구성) |
| `agent-reach install --env=auto --safe` | Safe setup (no auto system changes) / 안전 설정 (자동 시스템 변경 없음) |
| `agent-reach install --env=auto --dry-run` | Preview what would be done / 수행될 작업 미리보기 |
| `agent-reach doctor` | Show channel status / 채널 상태 표시 |
| `agent-reach watch` | Quick health + update check (for scheduled tasks) / 빠른 상태 + 업데이트 확인 (예약 작업용) |
| `agent-reach check-update` | Check for new versions / 새 버전 확인 |
| `agent-reach configure twitter-cookies "..."` | Unlock Twitter search + posting / Twitter 검색 + 게시 잠금 해제 |
| `agent-reach configure proxy URL` | Unlock Reddit + Bilibili on servers / 서버에서 Reddit + Bilibili 잠금 해제 |

After installation, use upstream tools directly. See SKILL.md for the full command reference / 설치 후에는 상위 도구를 직접 사용하세요. 전체 명령 참조는 SKILL.md를 참조하세요:

| Platform / 플랫폼 | Upstream Tool / 상위 도구 | Example / 예시 |
|----------|--------------|---------|
| Twitter/X | `xreach` | `xreach search "query" --json` |
| YouTube | `yt-dlp` | `yt-dlp --dump-json URL` |
| Bilibili | `yt-dlp` | `yt-dlp --dump-json URL` |
| Reddit | `curl` | `curl -s "https://reddit.com/r/xxx.json"` |
| GitHub | `gh` | `gh search repos "query"` |
| Web | `curl` + Jina | `curl -s "https://r.jina.ai/URL"` |
| Exa Search | `mcporter` | `mcporter call 'exa.web_search_exa(...)'` |
| 小红书 | `mcporter` | `mcporter call 'xiaohongshu.search_feeds(...)'` |
| 微博 | `mcporter` | `mcporter call 'weibo.get_trendings(limit: 10)'` |
| 抖音 | `mcporter` | `mcporter call 'douyin.parse_douyin_video_info(...)'` |
| LinkedIn | `mcporter` | `mcporter call 'linkedin.get_person_profile(...)'` |
| Boss直聘 | `mcporter` | `mcporter call 'bosszhipin.search_jobs_tool(...)'` |
| RSS | `feedparser` | `python3 -c "import feedparser; ..."` |
