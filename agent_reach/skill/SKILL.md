---
name: agent-reach
description: >
  Use the internet: search, read, and interact with 13+ platforms including
  Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu (小红书/샤오홍슈), Douyin (抖音/더우인),
  WeChat Articles (微信公众号/위챗 공식계정), LinkedIn, Boss直聘 (보스즈핑), RSS, Exa web search, and any web page.
  Use when: (1) user asks to search or read any of these platforms,
  (2) user shares a URL from any supported platform,
  (3) user asks to search the web, find information online, or research a topic,
  (4) user asks to post, comment, or interact on supported platforms,
  (5) user asks to configure or set up a platform channel.
  Triggers: "搜推特", "搜小红书", "看视频", "搜一下", "上网搜", "帮我查", "全网搜索",
  "search twitter", "read tweet", "youtube transcript", "search reddit",
  "read this link", "看这个链接", "B站", "bilibili", "抖音视频",
  "微信文章", "公众号", "LinkedIn", "GitHub issue", "RSS",
  "search online", "web search", "find information", "research",
  "帮我配", "configure twitter", "configure proxy", "帮我安装".
---

# Agent Reach — 사용 가이드 / Usage Guide

13개 이상의 플랫폼을 위한 업스트림 도구입니다. 직접 호출하세요.
Upstream tools for 13+ platforms. Call them directly.

`agent-reach doctor`를 실행하여 사용 가능한 채널을 확인하세요.
Run `agent-reach doctor` to check which channels are available.

## ⚠️ 워크스페이스 규칙 / Workspace Rules

**절대로 에이전트 워크스페이스에 파일을 생성하지 마세요.** 임시 출력에는 `/tmp/`를, 영구 데이터에는 `~/.agent-reach/`를 사용하세요.
**Never create files in the agent workspace.** Use `/tmp/` for temporary output and `~/.agent-reach/` for persistent data.

## 웹 — 모든 URL / Web — Any URL

```bash
curl -s "https://r.jina.ai/URL"
```

## 웹 검색 (Exa) / Web Search (Exa)

```bash
mcporter call 'exa.web_search_exa(query: "query", numResults: 5)'
mcporter call 'exa.get_code_context_exa(query: "code question", tokensNum: 3000)'
```

## Twitter/X (xreach)

```bash
xreach search "query" -n 10 --json          # 검색 / search
xreach tweet URL_OR_ID --json                # 트윗 읽기 (/status/ 및 /article/ URL 지원) / read tweet (supports /status/ and /article/ URLs)
xreach tweets @username -n 20 --json         # 사용자 타임라인 / user timeline
xreach thread URL_OR_ID --json               # 전체 스레드 / full thread
```

## YouTube (yt-dlp)

```bash
yt-dlp --dump-json "URL"                     # 비디오 메타데이터 / video metadata
yt-dlp --write-sub --write-auto-sub --sub-lang "zh-Hans,zh,en" --skip-download -o "/tmp/%(id)s" "URL"
                                             # 자막 다운로드 후 .vtt 파일 읽기 / download subtitles, then read the .vtt file
yt-dlp --dump-json "ytsearch5:query"         # 검색 / search
```

## Bilibili (yt-dlp)

```bash
yt-dlp --dump-json "https://www.bilibili.com/video/BVxxx"
yt-dlp --write-sub --write-auto-sub --sub-lang "zh-Hans,zh,en" --convert-subs vtt --skip-download -o "/tmp/%(id)s" "URL"
```

> 서버 IP가 412 오류가 발생할 수 있습니다. `--cookies-from-browser chrome`을 사용하거나 프록시를 구성하세요.
> Server IPs may get 412. Use `--cookies-from-browser chrome` or configure proxy.

## Reddit

```bash
curl -s "https://www.reddit.com/r/SUBREDDIT/hot.json?limit=10" -H "User-Agent: agent-reach/1.0"
curl -s "https://www.reddit.com/search.json?q=QUERY&limit=10" -H "User-Agent: agent-reach/1.0"
```

> 서버 IP가 403 오류가 발생할 수 있습니다. 대신 Exa를 통해 검색하거나 프록시를 구성하세요.
> Server IPs may get 403. Search via Exa instead, or configure proxy.

## GitHub (gh CLI)

```bash
gh search repos "query" --sort stars --limit 10
gh repo view owner/repo
gh search code "query" --language python
gh issue list -R owner/repo --state open
gh issue view 123 -R owner/repo
```

## 小红书 / XiaoHongShu (샤오홍슈) (mcporter)

```bash
mcporter call 'xiaohongshu.search_feeds(keyword: "query")'
mcporter call 'xiaohongshu.get_feed_detail(feed_id: "xxx", xsec_token: "yyy")'
mcporter call 'xiaohongshu.get_feed_detail(feed_id: "xxx", xsec_token: "yyy", load_all_comments: true)'
mcporter call 'xiaohongshu.publish_content(title: "제목/标题", content: "본문/正文", images: ["/path/img.jpg"], tags: ["tag"])'
```

> 로그인이 필요합니다. 쿠키를 가져오려면 Cookie-Editor를 사용하세요.
> Requires login. Use Cookie-Editor to import cookies.

## 抖音 / Douyin (더우인) (mcporter)

```bash
mcporter call 'douyin.parse_douyin_video_info(share_link: "https://v.douyin.com/xxx/")'
mcporter call 'douyin.get_douyin_download_link(share_link: "https://v.douyin.com/xxx/")'
```

> 로그인이 필요하지 않습니다. / No login needed.

## 微信公众号 / WeChat Articles (위챗 공식계정)

**검색 / Search** (miku_ai):
```python
python3 -c "
import asyncio
from miku_ai import get_wexin_article
async def s():
    for a in await get_wexin_article('query', 5):
        print(f'{a[\"title\"]} | {a[\"url\"]}')
asyncio.run(s())
"
```

**읽기 / Read** (Camoufox — 위챗 봇 탐지 우회 / bypasses WeChat anti-bot):
```bash
cd ~/.agent-reach/tools/wechat-article-for-ai && python3 main.py "https://mp.weixin.qq.com/s/ARTICLE_ID"
```

> 위챗 공식계정 글은 Jina Reader나 curl로 읽을 수 없습니다. Camoufox를 사용해야 합니다.
> WeChat articles cannot be read with Jina Reader or curl. Must use Camoufox.

## LinkedIn (mcporter)

```bash
mcporter call 'linkedin.get_person_profile(linkedin_url: "https://linkedin.com/in/username")'
mcporter call 'linkedin.search_people(keyword: "AI engineer", limit: 10)'
```

대안 / Fallback: `curl -s "https://r.jina.ai/https://linkedin.com/in/username"`

## Boss直聘 (보스즈핑/BossZhiPin) (mcporter)

```bash
mcporter call 'bosszhipin.get_recommend_jobs_tool(page: 1)'
mcporter call 'bosszhipin.search_jobs_tool(keyword: "Python", city: "Beijing/北京")'
```

대안 / Fallback: `curl -s "https://r.jina.ai/https://www.zhipin.com/job_detail/xxx"`

## RSS

```python
python3 -c "
import feedparser
for e in feedparser.parse('FEED_URL').entries[:5]:
    print(f'{e.title} — {e.link}')
"
```

## 문제 해결 / Troubleshooting

- **채널이 작동하지 않나요? / Channel not working?** `agent-reach doctor`를 실행하세요 — 상태와 수정 방법을 표시합니다. / Run `agent-reach doctor` — shows status and fix instructions.
- **Twitter 가져오기 실패? / Twitter fetch failed?** `undici`가 설치되어 있는지 확인하세요: `npm install -g undici`. 프록시 구성: `agent-reach configure proxy URL`. / Ensure `undici` is installed: `npm install -g undici`. Configure proxy: `agent-reach configure proxy URL`.

## 채널 설정 / Setting Up a Channel ("XXX 설정 도와줘" / "帮我配 XXX")

채널 설정이 필요한 경우 (쿠키, Docker 등), 설치 가이드를 가져오세요:
If a channel needs setup (cookies, Docker, etc.), fetch the install guide:
https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md

사용자는 쿠키만 제공합니다. 그 외 모든 것은 당신의 작업입니다.
User only provides cookies. Everything else is your job.
