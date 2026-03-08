<h1 align="center">👁️ Agent Reach</h1>

<p align="center">
  <strong>AI Agent에 인터넷 능력을 원클릭으로 추가</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#빠른-시작">빠른 시작</a> · <a href="docs/README_en.md">English</a> · <a href="#지원-플랫폼">지원 플랫폼</a> · <a href="#설계-철학">설계 철학</a>
</p>

---

## Agent Reach가 필요한 이유

AI Agent는 이미 코드 작성, 문서 수정, 프로젝트 관리를 도와줄 수 있지만, 인터넷에서 정보를 찾으라면 막막해집니다:

- 📺 "이 YouTube 튜토리얼이 뭘 설명하는지 확인해줘" → **불가능**, 자막을 가져올 수 없음
- 🐦 "Twitter에서 이 제품에 대한 평가를 검색해줘" → **불가능**, Twitter API는 유료
- 📖 "Reddit에 같은 bug를 겪은 사람이 있는지 확인해봐" → **403 차단**, 서버 IP 거부
- 📕 "小红书(샤오홍슈)에서 이 제품 평가 확인해줘" → **접근 불가**, 로그인 필요
- 📺 "B站(비리빌리) 기술 비디오 요약해줘" → **연결 불가**, 해외/서버 IP 차단
- 🔍 "최신 LLM 프레임워크 비교 검색해줘" → **사용 가능한 검색 없음**, 유료이거나 품질 낮음
- 🌐 "이 웹페이지 내용 확인해줘" → **HTML 태그만 가져옴**, 읽을 수 없음
- 📦 "이 GitHub 저장소는 뭐하는 거야? Issue에는 뭐가 있어?" → 사용 가능하지만 인증 설정 복잡
- 📡 "이 RSS 소스들 구독하고 업데이트 알려줘" → 직접 라이브러리 설치하고 코드 작성 필요

**구현은 어렵지 않지만, 직접 설정을 다뤄야 합니다**

각 플랫폼마다 장벽이 있습니다 - 유료 API, 우회해야 할 차단, 로그인 필요한 계정, 정제해야 할 데이터. 하나씩 시행착오를 겪고, 도구를 설치하고, 설정을 조정해야 합니다. Agent가 트위터를 읽게 하려면 반나절은 걸릴 겁니다.

**Agent Reach는 이걸 한 문장으로 만듭니다:**

```
Agent Reach 설치 도와줘: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

Agent에 복사해서 붙여넣으면, 몇 분 뒤에는 트위터 읽기, Reddit 검색, YouTube 시청, 小红书(샤오홍슈) 둘러보기가 가능합니다.

**이미 설치했나요? 업데이트도 한 문장입니다:**

```
Agent Reach 업데이트 도와줘: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

> ⭐ **이 프로젝트에 Star를 눌러주세요**, 각 플랫폼의 변화를 추적하고 새로운 채널(Channel)을 계속 추가할 것입니다. 신경 쓸 필요 없어요 - 플랫폼에서 차단하면 우리가 고치고, 새로운 채널이 있으면 추가합니다.

### ✅ 사용 전 궁금할 수 있는 것들

| | |
|---|---|
| 💰 **완전 무료** | 모든 도구 오픈소스, 모든 API 무료. 유일한 비용은 서버 프록시(월 $1)일 수 있으며, 로컬 컴퓨터는 필요 없음 |
| 🔒 **프라이버시 보안** | Cookie는 로컬에만 저장, 업로드나 외부 전송 없음. 코드 완전 오픈소스, 언제든지 검증 가능 |
| 🔄 **지속 업데이트** | 기본 도구(yt-dlp, xreach, Jina Reader 등) 정기적으로 최신 버전으로 추적, 직접 신경 쓸 필요 없음 |
| 🤖 **모든 Agent 호환** | Claude Code, OpenClaw, Cursor, Windsurf... 명령줄을 실행할 수 있는 모든 Agent 사용 가능 |
| 🩺 **내장 진단** | `agent-reach doctor` 하나의 명령으로 무엇이 통하고 무엇이 막혔는지, 어떻게 고치는지 알려줌 |

---

## 지원 플랫폼

| 플랫폼 | 설치 후 즉시 사용 | 설정 후 해제 | 설정 방법 |
|------|---------|-----------|-------|
| 🌐 **웹페이지** | 모든 웹페이지 읽기 | — | 설정 불필요 |
| 📺 **YouTube** | 자막 추출 + 비디오 검색 | — | 설정 불필요 |
| 📡 **RSS** | 모든 RSS/Atom 소스 읽기 | — | 설정 불필요 |
| 🔍 **전체 검색** | — | 전체 시맨틱 검색 | 자동 설정(MCP 연동, 무료, Key 불필요) |
| 📦 **GitHub** | 공개 저장소 읽기 + 검색 | 비공개 저장소, Issue/PR 생성, Fork | Agent에게 "GitHub 로그인 도와줘"라고 요청 |
| 🐦 **Twitter/X** | 단일 트윗 읽기 | 트윗 검색, 타임라인 탐색, 트윗 게시 | Agent에게 "Twitter 설정 도와줘"라고 요청 |
| 📺 **B站(비리빌리/Bilibili)** | 로컬: 자막 추출 + 검색 | 서버에서도 사용 | Agent에게 "프록시 설정 도와줘"라고 요청 |
| 📖 **Reddit** | 검색(Exa 무료 통해) | 게시물과 댓글 읽기 | Agent에게 "프록시 설정 도와줘"라고 요청 |
| 📕 **小红书(샤오홍슈/XiaoHongShu)** | — | 읽기, 검색, 게시, 댓글, 좋아요 | Agent에게 "小红书 설정 도와줘"라고 요청 |
| 🎵 **抖音(더우인/Douyin)** | — | 비디오 파싱, 워터마크 없는 다운로드 링크 가져오기 | Agent에게 "抖音 설정 도와줘"라고 요청 |
| 💼 **LinkedIn** | Jina Reader로 공개 페이지 읽기 | Profile 상세, 회사 페이지, 채용 공고 검색 | Agent에게 "LinkedIn 설정 도와줘"라고 요청 |
| 🏢 **Boss直聘(보스즈핑)** | Jina Reader로 채용 공고 페이지 읽기 | 채용 공고 검색, HR에게 메시지 보내기 | Agent에게 "Boss直聘 설정 도와줘"라고 요청 |
| 💬 **微信公众号(위챗 공식계정/WeChat MP)** | 검색 + 공식계정 글 읽기(전체 Markdown) | — | 설정 불필요 |

> **설정 방법을 모르겠나요? 문서를 찾을 필요 없습니다.** Agent에게 "XXX 설정 도와줘"라고 직접 말하면 됩니다. 무엇이 필요한지 알고 있으며, 단계별로 안내해 줄 것입니다.
>
> 🍪 Cookie가 필요한 플랫폼(Twitter, 小红书(샤오홍슈) 등)은 Chrome 확장 프로그램 [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)를 사용하여 Cookie를 내보내고, Agent에 보내기만 하면 됩니다. 프로세스는 통일되어 있습니다: 브라우저 로그인 → Cookie-Editor 내보내기 → Agent에 전송. QR 코드 스캔보다 간단하고 신뢰할 수 있습니다.
>
> 🔒 Cookie는 로컬에만 저장되며, 업로드나 외부 전송 없음. 코드 완전 오픈소스, 언제든지 검증 가능.
> 💻 로컬 컴퓨터에는 프록시가 필요 없음. 프록시는 서버에 배포할 때만 필요함(~월 $1).
>
> ### 한국 사용자 추천 VPN/클라우드 서비스
> - 개인용: Cloudflare WARP (무료) - https://1.1.1.1/
> - 기업용: AWS Korea (ap-northeast-2), NCP (네이버 클라우드) - https://www.ncloud.com/

---

## 빠른 시작

AI Agent(Claude Code, OpenClaw, Cursor 등)에게 이 문장을 복사해서 보내세요:

```
Agent Reach 설치 도와줘: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

이걸로 끝입니다. Agent가 나머지 모든 것을 자동으로 완료합니다.

> 🔄 **이미 설치했나요?** 업데이트도 한 문장입니다:
> ```
> Agent Reach 업데이트 도와줘: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
> ```
>
> 🛡️ **보안이 걱정되나요?** 안전 모드를 사용할 수 있습니다 - 시스템 패키지를 자동으로 설치하지 않고 필요한 것만 알려줍니다:
> ```
> Agent Reach 설치 도와줘 (안전 모드): https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
> 설치할 때 --safe 파라미터 사용
> ```

<details>
<summary>무슨 일을 하나요?(클릭하여 펼치기)</summary>

1. **CLI 도구 설치** — `pip install`로 `agent-reach` 명령줄 도구 설치
2. **시스템 의존성 설치** — Node.js, gh CLI, mcporter, xreach 등을 자동 감지하고 설치
3. **검색 엔진 설정** — MCP를 통해 Exa 연동(무료, API Key 불필요)
4. **환경 감지** — 로컬 컴퓨터인지 서버인지 판단, 해당하는 설정 제안
5. **SKILL.md 등록** — Agent의 skills 디렉토리에 사용 가이드 설치, 이후 Agent가 "트위터 검색", "비디오 시청" 같은 요구를 만나면 자동으로 어떤 상위 도구를 호출해야 할지 알게 됨

설치 후 `agent-reach doctor` 명령 하나로 각 채널의 상태를 알려줍니다.
</details>

---

## 설치 후 즉시 사용

설정이 필요 없으며, Agent에게 말하면 됩니다:

- "이 링크 확인해줘" → `curl https://r.jina.ai/URL`로 모든 웹페이지 읽기
- "이 GitHub 저장소는 뭐 하는 거야?" → `gh repo view owner/repo`
- "이 비디오는 뭘 설명하나?" → `yt-dlp --dump-json URL`로 자막 추출
- "이 트윗 확인해줘" → `xreach tweet URL --json`
- "이 RSS 구독해줘" → `feedparser`로 파싱
- "GitHub에서 LLM 프레임워크 검색해줘" → `gh search repos "LLM framework"`

**명령어를 외울 필요가 없습니다.** Agent가 SKILL.md를 읽은 후 스스로 무엇을 호출해야 할지 알게 됩니다.

---

## 설계 철학

**Agent Reach는 스캐폴딩(scaffolding)이지 프레임워크가 아닙니다.**

새 Agent에 환경을 설정할 때마다 도구를 찾고, 의존성을 설치하고, 설정을 조정하는 데 시간을 써야 합니다 - Twitter는 무엇으로 읽나요? Reddit은 어떻게 차단을 우회하나요? YouTube 자막은 어떻게 추출하나요? 매번 다시 시행착오를 겪어야 합니다.

Agent Reach가 하는 일은 간단합니다: **도구 선택과 설정 작업을 완료해 줍니다.**

설치 완료 후 Agent는 상위 도구(xreach CLI, yt-dlp, mcporter, gh CLI 등)를 직접 호출하며, Agent Reach의 래퍼 계층을 거칠 필요가 없습니다.

### 🔌 각 채널은 플러그인 가능

각 플랫폼 뒤에는 독립적인 상위 도구가 있습니다. **마음에 안 들나요? 교체하면 됩니다.**

```
channels/
├── web.py          → Jina Reader     ← Firecrawl, Crawl4AI 등으로 교체 가능...
├── twitter.py      → xreach            ← Nitter, 공식 API 등으로 교체 가능...
├── youtube.py      → yt-dlp          ← YouTube API, Whisper 등으로 교체 가능...
├── github.py       → gh CLI          ← REST API, PyGithub 등으로 교체 가능...
├── bilibili.py     → yt-dlp          ← bilibili-api 등으로 교체 가능...
├── reddit.py       → JSON API + Exa  ← PRAW, Pushshift 등으로 교체 가능...
├── xiaohongshu.py  → mcporter MCP    ← 다른 XHS 도구로 교체 가능...
├── douyin.py       → mcporter MCP    ← 다른 抖音 도구로 교체 가능...
├── linkedin.py     → linkedin-mcp    ← LinkedIn API 등으로 교체 가능...
├── bosszhipin.py   → mcp-bosszp      ← 다른 채용 도구로 교체 가능...
├── wechat.py       → camoufox+miku   ← 검색+읽기 공식계정 글
├── rss.py          → feedparser      ← atoma 등으로 교체 가능...
├── exa_search.py   → mcporter MCP    ← Tavily, SerpAPI 등으로 교체 가능...
└── __init__.py     → 채널 등록(doctor 검색용)
```

각 채널 파일은 해당 상위 도구의 사용 가능 여부만 확인(`check()` 메서드)하며, `agent-reach doctor`에 상태 정보를 제공합니다. 실제 읽기와 검색은 Agent가 상위 도구를 직접 호출하여 완료합니다.

### 현재 선택

| 시나리오 | 선택 | 선택한 이유 |
|------|------|-----------|
| 웹페이지 읽기 | [Jina Reader](https://github.com/jina-ai/reader) | 9.8K Star, 무료, API Key 불필요 |
| 트위터 읽기 | [xreach](https://www.npmjs.com/package/xreach-cli) | Cookie 로그인, 무료. 공식 API는 종량제(읽기 1건당 $0.005) |
| 비디오 자막 + 검색 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | 148K Star, YouTube + B站 + 1800개 사이트 지원 |
| 전체 검색 | [Exa](https://exa.ai) via [mcporter](https://github.com/steipete/mcporter) | AI 시맨틱 검색, MCP 연동으로 Key 불필요 |
| GitHub | [gh CLI](https://cli.github.com) | 공식 도구, 인증 후 완전한 API 기능 |
| RSS 읽기 | [feedparser](https://github.com/kurtmckee/feedparser) | Python 생태계 표준 선택, 2.3K Star |
| 小红书 | [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | ⭐9K+, Go 언어, Docker 원클릭 배포 |
| 抖音 | [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) | MCP 서비스, 로그인 불필요, 비디오 파싱 + 워터마크 없는 다운로드 |
| LinkedIn | [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server) | ⭐900+, MCP 서비스, 브라우저 자동화 |
| Boss直聘 | [mcp-bosszp](https://github.com/mucsbr/mcp-bosszp) | MCP 서비스, 채용 공고 검색 및 메시지 전송 지원 |
| 공식계정 | [wechat-article-for-ai](https://github.com/bzd6661/wechat-article-for-ai) + [miku_ai](https://github.com/GobinFan/Miku_Spider) | Camoufox 스텔스 브라우저로 전체 읽기 + Sogou 검색 |

> 📌 이것들은 "현재 선택"입니다. 마음에 안 들나요? 해당 파일을 교체하면 됩니다. 이것이 바로 스캐폴딩의 의미입니다.

---

## 보안성

Agent Reach는 설계 시 보안을 중시합니다:

| 조치 | 설명 |
|------|------|
| 🔒 **로컬 자격 증명 저장** | Cookie, Token은 로컬 `~/.agent-reach/config.yaml`에만 저장, 파일 권한 600(소유자만 읽기/쓰기 가능), 업로드나 외부 전송 없음 |
| 🛡️ **안전 모드** | `agent-reach install --safe`는 시스템을 자동으로 수정하지 않고 필요한 것만 나열, 사용자가 설치 여부 결정 |
| 👀 **완전 오픈소스** | 코드 투명, 언제든지 검증 가능. 모든 의존 도구도 오픈소스 프로젝트 |
| 🔍 **Dry Run** | `agent-reach install --dry-run`으로 모든 작업을 미리보기, 어떤 변경도 하지 않음 |
| 🧩 **플러그인 가능 아키텍처** | 특정 구성 요소를 신뢰하지 않나요? 해당 channel 파일만 교체하면 되며, 다른 부분에 영향 없음 |

### 🍪 Cookie 보안 권장사항

> ⚠️ **계정 정지 위험 알림:** Cookie 로그인이 필요한 플랫폼(Twitter, 小红书 등)은 스크립트/API 호출을 통해 **플랫폼에서 감지되어 계정이 정지될 위험이 있습니다**. 반드시 **전용 소계정**을 사용하시고, 메인 계정은 사용하지 마세요.

Cookie가 필요한 플랫폼(Twitter, 小红书)은 **전용 소계정** 사용을 권장하며, 메인 계정은 사용하지 마세요. 이유는 두 가지입니다:
1. **계정 정지 위험** — 플랫폼이 비정상 브라우저의 API 호출 동작을 감지하여 계정이 제한되거나 차단될 수 있음
2. **보안 위험** — Cookie는 완전한 로그인 권한과 동일하며, 소계정을 사용하면 자격 증명 유출 시 영향 범위를 제한할 수 있음

### 📦 설치 방법

| 방식 | 명령 | 적합한 시나리오 |
|------|------|---------|
| 원클릭 자동(기본값) | `agent-reach install --env=auto` | 개인 컴퓨터, 개발 환경 |
| 안전 모드 | `agent-reach install --env=auto --safe` | 프로덕션 서버 |
| 미리보기만 | `agent-reach install --env=auto --dry-run` | 먼저 무엇을 할지 확인 |

### 🗑️ 제거

```bash
agent-reach uninstall
```

삭제되는 항목: `~/.agent-reach/`(모든 token/cookie 포함), 각 Agent의 skill 파일, mcporter의 MCP 설정.

```bash
# 미리보기만, 실제로는 삭제하지 않음
agent-reach uninstall --dry-run

# skill 파일만 삭제, token 설정 보존(재설치 시 사용)
agent-reach uninstall --keep-config
```

Python 패키지 자체 제거: `pip uninstall agent-reach`

---

## 기여

이 프로젝트는 완전히 vibe coding으로 만들어졌습니다 🎸 완벽하지 않을 수 있으니, 문제가 발생하면 너그럽게 이해해 주세요. 버그가 있으면 [Issue](https://github.com/Panniantong/agent-reach/issues)를 제출해 주세요, 최대한 빨리 수정하겠습니다.

**새로운 채널이 원하시나요?** Issue를 제출해서 알려주시거나 직접 PR을 보내주세요.

**로컬에 추가하고 싶으신가요?** Agent가 저장소를 clone 하도록 하면 되며, 각 채널은 독립 파일이므로 추가하기 간단합니다.

[PR](https://github.com/Panniantong/agent-reach/pulls)도 언제든 환영합니다!

---

## ⭐ Star를 누를 가치가 있는 이유

이 프로젝트는 매일 사용하고 있으므로, 계속 유지 관리할 것입니다.

- 새로운 요구사항이나 원하시는 채널이 있으면 계속 추가할 것입니다
- 각 채널은 **사용 가능, 사용하기 쉬움, 무료**를 최대한 보장할 것입니다
- 플랫폼에서 anti-scraping을 변경하거나 API가 변경되면 해결 방법을 찾을 것입니다

Web 4.0 인프라에 기여하고 있습니다.

Star를 눌러두시면 다음에 필요할 때 찾을 수 있습니다.⭐

---

## 자주 묻는 질문 / FAQ

<details>
<summary><strong>AI Agent로 Twitter/X를 어떻게 검색하나요? API 요금을 내고 싶지 않아요</strong></summary>

Agent Reach는 [xreach CLI](https://www.npmjs.com/package/xreach-cli)를 사용하여 Cookie 인증으로 Twitter에 접근하며, 완전 무료입니다. Agent Reach 설치 후, Cookie-Editor로 Twitter Cookie를 내보내고, `agent-reach configure twitter-cookies "your_cookies"`를 실행하면 됩니다. 이후 Agent가 `xreach search "키워드" --json`으로 트윗을 검색할 수 있습니다.
</details>

<details>
<summary><strong>Reddit이 403을 반환하거나 서버 IP가 차단되면 어떻게 하나요?</strong></summary>

Reddit은 데이터센터 IP를 차단합니다. 주거용 프록시를 설정하면 해결됩니다: `agent-reach configure proxy http://user:pass@ip:port`. Webshare(월 $1)를 추천합니다. 로컬 컴퓨터는 일반적으로 이 문제가 발생하지 않습니다.
</details>

<details>
<summary><strong>How to get YouTube video transcripts for AI?</strong></summary>

`yt-dlp --dump-json "https://youtube.com/watch?v=xxx"` extracts video metadata; `yt-dlp --write-sub --skip-download "URL"` extracts subtitles. Uses yt-dlp under the hood, supports multiple languages. No API key needed.
</details>

<details>
<summary><strong>AI Agent로 小红书(샤오홍슈)를 읽게 하려면 어떻게 하나요?</strong></summary>

小红书는 Docker로 MCP 서비스를 실행해야 합니다. Docker 설치 후 `agent-reach install`을 실행하면 자동으로 설정됩니다. 이후 Agent가 `mcporter call 'xiaohongshu.get_feed_detail(...)'`로 노트를 읽거나 `mcporter call 'xiaohongshu.search_feeds(keyword: "키워드")'`로 검색할 수 있습니다.
</details>

<details>
<summary><strong>AI Agent로 抖音(더우인) 비디오를 파싱하려면 어떻게 하나요?</strong></summary>

douyin-mcp-server 설치 후, Agent가 `mcporter call 'douyin.parse_douyin_video_info(share_link: "공유 링크")'`로 비디오 정보를 파싱하고 워터마크 없는 다운로드 링크를 가져올 수 있습니다. 로그인이 필요 없으며, 抖音 공유 링크를 Agent에 보내기만 하면 됩니다. 자세한 내용은 https://github.com/yzfly/douyin-mcp-server
</details>

<details>
<summary><strong>Claude Code / Cursor / OpenClaw / Windsurf와 호환되나요?</strong></summary>

Yes! Agent Reach is an installer + configuration tool — any AI coding agent that can run shell commands can use it. Works with Claude Code, Cursor, OpenClaw, Windsurf, Codex, and more. Just `pip install agent-reach`, run `agent-reach install`, and the agent can start using the upstream tools immediately.
</details>

<details>
<summary><strong>Is this free? Any API costs?</strong></summary>

100% free. All backends are open-source tools (xreach CLI, yt-dlp, Jina Reader, Exa, etc.) that don't require paid API keys. The only optional cost is a residential proxy (~$1/month) if you need Reddit/Bilibili access from a server.
</details>

---

## 감사의 말씀

[Jina Reader](https://github.com/jina-ai/reader) · [yt-dlp](https://github.com/yt-dlp/yt-dlp) · [xreach](https://www.npmjs.com/package/xreach-cli) · [Exa](https://exa.ai) · [mcporter](https://github.com/steipete/mcporter) · [feedparser](https://github.com/kurtmckee/feedparser) · [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) · [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) · [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server) · [mcp-bosszp](https://github.com/mucsbr/mcp-bosszp)

## License

[MIT](LICENSE)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Panniantong/Agent-Reach&type=Date)](https://star-history.com/#Panniantong/Agent-Reach&Date)
