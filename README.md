<h1 align="center">👁️ Agent Reach</h1>

<p align="center">
  <strong>AI Agent에 인터넷 능력을 원클릭으로 추가</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#빠른-시작">빠른 시작</a> · <a href="docs/README_en.md">English</a> · <a href="#지원-플랫폼">지원 플랫폼</a> · <a href="#설계-철학">설계 철학</a>
</p>

---

## Agent Reach가 필요한 이유

AI Agent는 이미 코드 작성, 문서 수정, 프로젝트 관리를 도와줄 수 있지만, 인터넷에서 실제 정보를 찾게 하려면 금방 막히기 시작합니다.

- 📺 "이 YouTube 튜토리얼이 뭘 설명하는지 확인해줘" → **불가**, 자막을 바로 읽지 못함
- 🐦 "Twitter/X에서 이 제품 평가 좀 찾아줘" → **불가**, API는 유료이거나 제약이 큼
- 📖 "Reddit에 같은 버그 겪은 사람이 있는지 봐줘" → **403 차단**, 서버 IP가 막힘
- 📕 "샤오홍슈에서 이 제품 후기를 찾아줘" → **접근 불가**, 로그인 필요
- 📺 "Bilibili 기술 영상을 요약해줘" → **연결 불안정**, 해외/서버 IP 차단 가능
- 🔍 "최신 LLM 프레임워크 비교를 검색해줘" → **쓸 만한 검색 도구 부족**, 유료이거나 품질이 낮음
- 🌐 "이 웹페이지 내용 좀 읽어줘" → **HTML만 가져옴**, 읽기 어려움
- 📦 "이 GitHub 저장소는 뭐 하는 거야? 이슈는 어때?" → 가능은 하지만 인증과 설정이 번거로움
- 📡 "이 RSS들을 구독하고 업데이트 알려줘" → 직접 라이브러리와 코드를 만져야 함

**구현 자체는 어렵지 않지만, 직접 설정을 다뤄야 합니다.**

플랫폼마다 장벽이 다릅니다. 유료 API, 우회해야 하는 차단, 로그인 계정, 정제해야 하는 데이터가 따로 있고, Agent가 쓸 수 있게 만들려면 설치와 설정을 하나씩 반복해야 합니다.

**Agent Reach는 이 과정을 한 문장으로 바꿉니다:**

```text
Agent Reach 설치 도와줘: https://raw.githubusercontent.com/cool25th/Agent-Reach-Kr/main/docs/install.md
```

Agent에 그대로 붙여넣으면 몇 분 뒤에는 트윗 읽기, Reddit 검색, YouTube 자막 추출, 샤오홍슈 탐색 같은 작업을 바로 시킬 수 있습니다.

**이미 설치했다면 업데이트도 한 문장입니다:**

```text
Agent Reach 업데이트 도와줘: https://raw.githubusercontent.com/cool25th/Agent-Reach-Kr/main/docs/update.md
```

> ⭐ 이 프로젝트에 Star를 눌러 주세요. 플랫폼 변화 추적, 채널 추가, 설정 방식 개선이 계속 들어옵니다.

### ✅ 시작 전에 알아둘 점

| | |
|---|---|
| 💰 **완전 무료** | 모든 도구는 오픈소스이고 기본 API도 무료입니다. 선택 비용은 서버 프록시 정도(월 약 $1)이며, 로컬 컴퓨터는 대체로 필요 없습니다 |
| 🔒 **프라이버시 보호** | 쿠키와 토큰은 로컬에만 저장되며 업로드되지 않습니다. 코드도 공개되어 있어 검증할 수 있습니다 |
| 🔄 **지속 업데이트** | yt-dlp, xreach, Jina Reader 같은 상위 도구 변화를 계속 따라갑니다 |
| 🤖 **모든 Agent 호환** | Claude Code, OpenClaw, Cursor, Windsurf, Codex 등 셸 명령을 실행할 수 있는 Agent면 사용할 수 있습니다 |
| 🩺 **내장 진단** | `agent-reach doctor` 한 번으로 어떤 채널이 되고 안 되는지, 어떻게 고쳐야 하는지 확인할 수 있습니다 |

---

## 지원 플랫폼

| 플랫폼 | 설치 후 바로 사용 | 설정 후 확장 | 설정 방법 |
|------|---------|-----------|-------|
| 🌐 **웹페이지** | 모든 웹페이지 읽기 | — | 설정 불필요 |
| 📺 **YouTube** | 자막 추출 + 비디오 검색 | — | 설정 불필요 |
| 📡 **RSS** | RSS/Atom 소스 읽기 | — | 설정 불필요 |
| 🔍 **웹 검색** | — | 전체 시맨틱 검색 | 자동 구성(MCP 연동, 무료, API Key 불필요) |
| 📦 **GitHub** | 공개 저장소 읽기 + 검색 | 비공개 저장소, Issue/PR 생성, Fork | Agent에게 "GitHub 로그인 도와줘"라고 요청 |
| 🐦 **Twitter/X** | 단일 트윗 읽기 | 검색, 타임라인, 게시 | Agent에게 "Twitter 설정 도와줘"라고 요청 |
| 📺 **Bilibili** | 로컬에서 자막 추출 + 검색 | 서버에서도 사용 | Agent에게 "프록시 설정 도와줘"라고 요청 |
| 📖 **Reddit** | 검색(Exa 무료 경유) | 게시물과 댓글 읽기 | Agent에게 "프록시 설정 도와줘"라고 요청 |
| 📕 **샤오홍슈 / XiaoHongShu** | — | 읽기, 검색, 게시, 댓글, 좋아요 | Agent에게 "샤오홍슈 설정 도와줘"라고 요청 |
| 📰 **웨이보 / Weibo** | 핫토픽, 검색, 사용자 피드, 댓글 | — | 설정 불필요 |
| 🎵 **더우인 / Douyin** | — | 비디오 파싱, 워터마크 없는 다운로드 링크 | Agent에게 "더우인 설정 도와줘"라고 요청 |
| 💼 **LinkedIn** | Jina Reader로 공개 페이지 읽기 | 프로필 상세, 회사 페이지, 채용 검색 | Agent에게 "LinkedIn 설정 도와줘"라고 요청 |
| 🏢 **Boss直聘** | Jina Reader로 채용 공고 읽기 | 채용 검색, HR 메시지 | Agent에게 "Boss直聘 설정 도와줘"라고 요청 |
| 💬 **WeChat 공식계정 글** | 검색 + 본문 읽기(전체 Markdown) | — | 설정 불필요 |

> 설정 수준: 설정 불필요 = 설치 즉시 사용 · 자동 구성 = 설치 중 처리 · mcporter = MCP 서비스 필요 · Cookie = 브라우저에서 내보내기 · Proxy = 약 $1/월
>
> 🍪 Cookie가 필요한 플랫폼(Twitter/X, 샤오홍슈 등)은 Chrome 확장 프로그램 [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)로 내보내면 가장 간단합니다. 흐름은 같습니다: 브라우저 로그인 → Cookie-Editor 내보내기 → Agent에 전달.
>
> 🔒 Cookie는 로컬에만 저장되며 외부로 업로드되지 않습니다. 💻 프록시는 대체로 서버 환경에서만 필요합니다.

---

## 빠른 시작

> ⚠️ **OpenClaw 사용자는 먼저 `exec` 권한을 켜야 합니다**
>
> Agent Reach는 `pip install`, `mcporter`, `xreach` 같은 셸 명령을 실행해야 합니다. OpenClaw는 2026년 1월부터 기본적으로 `exec` 도구를 비활성화하므로, 설치 전에 다음 중 하나를 먼저 설정해야 합니다.
>
> ```text
> /config set exec.allow true
> ```
>
> 또는 `~/.openclaw/config.json`에 `"exec": { "allow": true }`를 추가한 뒤 대화를 다시 시작하세요. Claude Code, Cursor, Windsurf 등 다른 Agent는 이 제한이 없습니다.

AI Agent(Claude Code, OpenClaw, Cursor 등)에게 이 문장을 복사해서 보내세요:

```text
Agent Reach 설치 도와줘: https://raw.githubusercontent.com/cool25th/Agent-Reach-Kr/main/docs/install.md
```

이 한 줄이면 충분합니다. Agent가 나머지 설치와 진단을 자동으로 처리합니다.

> 🔄 **이미 설치했나요?**
> ```text
> Agent Reach 업데이트 도와줘: https://raw.githubusercontent.com/cool25th/Agent-Reach-Kr/main/docs/update.md
> ```
>
> 🛡️ **보안이 걱정되나요?**
> ```text
> Agent Reach 설치 도와줘 (안전 모드): https://raw.githubusercontent.com/cool25th/Agent-Reach-Kr/main/docs/install.md
> 설치할 때 --safe 파라미터를 사용해줘
> ```

<details>
<summary>설치가 실제로 하는 일</summary>

1. `agent-reach` CLI 설치
2. Node.js, gh CLI, mcporter, xreach 같은 시스템 의존성 점검 및 설치
3. Exa 검색 연동 구성
4. 로컬/서버 환경 감지
5. SKILL.md 등록으로 Agent가 어떤 상위 도구를 불러야 하는지 학습

설치가 끝나면 `agent-reach doctor`로 채널 상태를 바로 확인할 수 있습니다.
</details>

---

## 설치 후 바로 쓰기

별도 설정 없이 Agent에게 말하면 됩니다.

- "이 링크 읽어줘" → `curl https://r.jina.ai/URL`
- "이 GitHub 저장소 뭐야?" → `gh repo view owner/repo`
- "이 영상이 무슨 내용이야?" → `yt-dlp --dump-json URL`
- "이 트윗 읽어줘" → `xreach tweet URL --json`
- "이 RSS 구독해줘" → `feedparser`로 파싱
- "GitHub에서 LLM 프레임워크 검색해줘" → `gh search repos "LLM framework"`

**명령어를 외울 필요는 없습니다.** Agent가 SKILL.md를 읽고 적절한 상위 도구를 고릅니다.

---

## 설계 철학

**Agent Reach는 프레임워크가 아니라 스캐폴딩 도구입니다.**

새 Agent를 띄울 때마다 Twitter는 뭘로 읽고, Reddit 차단은 어떻게 피하고, YouTube 자막은 어떻게 뽑는지 다시 조사할 필요가 없습니다. Agent Reach는 그 선택과 초기 설정을 대신합니다.

설치가 끝난 뒤 Agent는 xreach CLI, yt-dlp, mcporter, gh CLI 같은 상위 도구를 **직접 호출**합니다. Agent Reach는 설치와 상태 점검을 담당하는 얇은 계층입니다.

### 🔌 각 채널은 교체 가능

플랫폼마다 독립된 상위 도구를 씁니다. 마음에 들지 않으면 파일 하나를 교체하면 됩니다.

```text
channels/
├── web.py          → Jina Reader        ← Firecrawl, Crawl4AI 등으로 교체 가능
├── twitter.py      → xreach             ← Nitter, 공식 API 등으로 교체 가능
├── youtube.py      → yt-dlp             ← YouTube API, Whisper 등으로 교체 가능
├── github.py       → gh CLI             ← REST API, PyGithub 등으로 교체 가능
├── bilibili.py     → yt-dlp             ← bilibili-api 등으로 교체 가능
├── reddit.py       → JSON API + Exa     ← PRAW, Pushshift 등으로 교체 가능
├── xiaohongshu.py  → mcporter MCP       ← 다른 XHS 도구로 교체 가능
├── weibo.py        → mcp-server-weibo   ← 다른 Weibo 도구로 교체 가능
├── douyin.py       → mcporter MCP       ← 다른 Douyin 도구로 교체 가능
├── linkedin.py     → linkedin-mcp       ← LinkedIn API 등으로 교체 가능
├── bosszhipin.py   → mcp-bosszp         ← 다른 채용 도구로 교체 가능
├── wechat.py       → camoufox + miku_ai ← 검색 + 읽기용
├── rss.py          → feedparser         ← atoma 등으로 교체 가능
├── exa_search.py   → mcporter MCP       ← Tavily, SerpAPI 등으로 교체 가능
└── __init__.py     → 채널 등록(doctor 점검용)
```

각 채널 파일은 `check()` 메서드로 상위 도구 사용 가능 여부를 점검하고, 실제 읽기와 검색은 Agent가 상위 도구를 직접 호출해 수행합니다.

### 현재 선택

| 시나리오 | 선택 | 이유 |
|------|------|-----------|
| 웹페이지 읽기 | [Jina Reader](https://github.com/jina-ai/reader) | 무료, API Key 불필요, Markdown 정리 품질이 좋음 |
| 트윗 읽기 | [xreach](https://www.npmjs.com/package/xreach-cli) | Cookie 인증 기반, 무료. 공식 API보다 접근성이 좋음 |
| 비디오 자막 + 검색 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | YouTube, Bilibili 포함 1800+ 사이트 지원 |
| 웹 검색 | [Exa](https://exa.ai) via [mcporter](https://github.com/steipete/mcporter) | AI 시맨틱 검색, MCP 연동 |
| GitHub | [gh CLI](https://cli.github.com) | 공식 도구, 인증 후 전체 API 활용 가능 |
| RSS | [feedparser](https://github.com/kurtmckee/feedparser) | Python 생태계 표준 |
| 샤오홍슈 | [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | MCP 서비스, Docker 배포 간단 |
| 웨이보 | [mcp-server-weibo](https://github.com/Panniantong/mcp-server-weibo) | 핫 검색, 검색, 사용자 피드, 댓글 기능 제공 |
| 더우인 | [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) | 로그인 없이 비디오 파싱과 다운로드 링크 제공 |
| LinkedIn | [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server) | MCP 기반 상세 프로필/채용 검색 |
| Boss直聘 | [mcp-bosszp](https://github.com/mucsbr/mcp-bosszp) | MCP 기반 채용 검색 및 메시지 기능 |
| WeChat 공식계정 | [wechat-article-for-ai](https://github.com/bzd6661/wechat-article-for-ai) + [miku_ai](https://github.com/GobinFan/Miku_Spider) | Camoufox 기반 전체 본문 읽기 + Sogou 검색 |

> 지금의 선택일 뿐입니다. 필요하면 상위 도구를 바꿀 수 있습니다.

---

## 보안

Agent Reach는 기본적으로 안전한 설정을 우선합니다.

| 조치 | 설명 |
|------|------|
| 🔒 **자격 증명 로컬 저장** | Cookie와 Token은 `~/.agent-reach/config.yaml`에만 저장되고, 권한은 600입니다 |
| 🛡️ **안전 모드** | `agent-reach install --safe`는 시스템을 자동 수정하지 않고 필요한 항목만 안내합니다 |
| 👀 **완전 오픈소스** | 코드와 의존 도구 모두 확인할 수 있습니다 |
| 🔍 **Dry Run** | `agent-reach install --dry-run`으로 실제 변경 전에 작업 내용을 미리 봅니다 |
| 🧩 **플러그인 구조** | 특정 구성 요소가 마음에 들지 않으면 그 파일만 교체할 수 있습니다 |

### 🍪 Cookie 사용 시 권장사항

> ⚠️ Twitter/X, 샤오홍슈처럼 Cookie 로그인이 필요한 플랫폼은 자동화 호출이 플랫폼에 탐지되어 계정이 제한될 수 있습니다. **반드시 전용 부계정**을 쓰는 편이 안전합니다.

Cookie 기반 로그인에 부계정을 권장하는 이유는 두 가지입니다.

1. 계정 정지 위험을 메인 계정에서 분리할 수 있습니다.
2. Cookie는 사실상 전체 로그인 권한이므로 유출 시 영향 범위를 줄일 수 있습니다.

### 📦 설치 방식

| 방식 | 명령 | 적합한 환경 |
|------|------|---------|
| 기본 자동 설치 | `agent-reach install --env=auto` | 개인 컴퓨터, 개발 환경 |
| 안전 모드 | `agent-reach install --env=auto --safe` | 프로덕션 서버, 공유 머신 |
| 미리보기 | `agent-reach install --env=auto --dry-run` | 실제 변경 전 확인 |

### 🗑️ 제거

```bash
agent-reach uninstall
```

다음 항목이 제거됩니다: `~/.agent-reach/`(token/cookie 포함), 각 Agent의 skill 파일, mcporter MCP 설정.

```bash
# 미리보기만 수행
agent-reach uninstall --dry-run

# skill 파일만 삭제하고 설정은 유지
agent-reach uninstall --keep-config
```

Python 패키지 자체를 제거하려면 `pip uninstall agent-reach`를 실행하면 됩니다.

---

## 기여

이 프로젝트는 강한 실용성을 우선하는 방식으로 빠르게 발전하고 있습니다. 문제가 있으면 [Issue](https://github.com/Panniantong/agent-reach/issues)를 열어 주세요.

**새 채널이 필요하다면** Issue로 요청하거나 직접 PR을 보내면 됩니다.

**로컬에서 실험하고 싶다면** Agent에게 저장소를 clone하게 한 뒤 채널 파일 하나를 추가하면 됩니다. 각 채널은 독립 파일이라 확장하기 쉽습니다.

[PR](https://github.com/Panniantong/agent-reach/pulls)은 언제든 환영입니다.

---

## ⭐ 왜 Star를 누를 만한가

이 프로젝트는 실제 사용을 전제로 계속 유지보수됩니다.

- 새 요구가 생기면 채널과 설정 가이드가 계속 추가됩니다
- 가능한 한 무료이고 실제로 쓸 수 있는 도구를 우선 채택합니다
- 플랫폼 반봇 정책이나 API 변화가 생기면 대응 방안이 문서와 코드에 반영됩니다

필요할 때 다시 찾기 쉽도록 Star를 남겨 두는 편이 좋습니다.

---

## 자주 묻는 질문

<details>
<summary><strong>AI Agent로 Twitter/X를 API 비용 없이 검색하려면?</strong></summary>

Agent Reach는 [xreach CLI](https://www.npmjs.com/package/xreach-cli)를 Cookie 인증과 함께 사용합니다. Twitter API 구독 없이도 검색이 가능하며, Cookie-Editor로 Twitter 쿠키를 내보낸 뒤 `agent-reach configure twitter-cookies "your_cookies"`를 실행하면 됩니다. 이후 Agent는 `xreach search "키워드" --json`으로 검색할 수 있습니다.
</details>

<details>
<summary><strong>Reddit이 403을 반환하거나 서버 IP가 차단되면?</strong></summary>

Reddit은 데이터센터 IP를 자주 차단합니다. `agent-reach configure proxy http://user:pass@ip:port`로 주거형 프록시를 설정하면 해결되는 경우가 많습니다. Webshare 같은 저가 프록시도 쓸 수 있고, 로컬 컴퓨터에서는 대체로 이 문제가 덜합니다.
</details>

<details>
<summary><strong>AI용 YouTube 자막이나 스크립트를 가져오려면?</strong></summary>

`yt-dlp --dump-json "https://youtube.com/watch?v=xxx"`로 메타데이터를 확인하고, `yt-dlp --write-sub --skip-download "URL"`로 자막을 추출할 수 있습니다. 여러 언어를 지원하며 별도 API Key가 필요 없습니다.
</details>

<details>
<summary><strong>AI Agent로 샤오홍슈 콘텐츠를 읽으려면?</strong></summary>

샤오홍슈는 MCP 서비스를 Docker로 띄워야 합니다. Docker 설치 후 `agent-reach install`을 실행하면 설정을 도와주고, 이후에는 `mcporter call 'xiaohongshu.get_feed_detail(...)'`로 노트를 읽거나 `mcporter call 'xiaohongshu.search_feeds(keyword: "키워드")'`로 검색할 수 있습니다.
</details>

<details>
<summary><strong>AI Agent로 Douyin 영상을 파싱하려면?</strong></summary>

`douyin-mcp-server`를 설치한 뒤 `mcporter call 'douyin.parse_douyin_video_info(share_link: "공유 링크")'`를 호출하면 비디오 정보와 워터마크 없는 다운로드 링크를 가져올 수 있습니다. 로그인 없이 동작합니다.
</details>

<details>
<summary><strong>Claude Code / Cursor / OpenClaw / Windsurf / Codex와 호환되나요?</strong></summary>

호환됩니다. Agent Reach는 설치와 구성에 초점을 둔 도구라서, 셸 명령을 실행할 수 있는 AI 코딩 Agent라면 사용할 수 있습니다. `pip install agent-reach` 후 `agent-reach install`을 실행하면 상위 도구를 바로 활용할 수 있습니다.

OpenClaw만 예외가 하나 있습니다. 2026년 1월 이후 기본적으로 `exec`가 꺼져 있으므로, 설치 전에 `/config set exec.allow true` 또는 `~/.openclaw/config.json` 수정이 필요합니다.
</details>

<details>
<summary><strong>정말 무료인가요? 추가 비용이 있나요?</strong></summary>

기본적으로는 무료입니다. xreach CLI, yt-dlp, Jina Reader, Exa 같은 백엔드는 모두 오픈소스 또는 무료 사용 범위를 기반으로 합니다. 선택 비용은 서버에서 Reddit/Bilibili에 접근할 때 필요한 프록시 정도입니다.
</details>

---

## 감사의 말씀

[Jina Reader](https://github.com/jina-ai/reader) · [yt-dlp](https://github.com/yt-dlp/yt-dlp) · [xreach](https://www.npmjs.com/package/xreach-cli) · [Exa](https://exa.ai) · [mcporter](https://github.com/steipete/mcporter) · [feedparser](https://github.com/kurtmckee/feedparser) · [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) · [mcp-server-weibo](https://github.com/Panniantong/mcp-server-weibo) · [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) · [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server) · [mcp-bosszp](https://github.com/mucsbr/mcp-bosszp)

## 연락처

협업, 기능 제안, AI Agent 활용에 관한 이야기를 하고 싶다면 아래 QR로 연락할 수 있습니다.

<p align="center">
  <img src="docs/wechat-qr.jpg" width="280" alt="WeChat QR">
</p>

> 버그 제보와 기능 요청은 [GitHub Issues](https://github.com/Panniantong/Agent-Reach/issues)를 사용하는 편이 추적이 쉽습니다.

## License

[MIT](LICENSE)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date)](https://star-history.com/#Panniantong/Agent-Reach&Date)
