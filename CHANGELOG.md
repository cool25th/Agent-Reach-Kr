# Changelog / 변경 로그

All notable changes to this project will be documented in this file.

이 프로젝트의 모든 중요한 변경 사항은 이 파일에 기록됩니다.

---

## [1.1.0] - 2025-02-25

### 🆕 New Channels / 새로운 채널

#### ~~📷 Instagram~~ (removed — upstream blocked)
- ~~Read public posts and profiles via [instaloader](https://github.com/instaloader/instaloader)~~
- **Removed:** Instagram's aggressive anti-scraping measures broke all available open-source tools (instaloader, etc.). See [instaloader#2585](https://github.com/instaloader/instaloader/issues/2585). Will re-add when upstream recovers.
- **제거됨:** Instagram의 공격적인 스크래핑 방지 조치로 인해 모든 오픈소스 도구(instaloader 등)가 작동하지 않습니다. [instaloader#2585](https://github.com/instaloader/instaloader/issues/2585) 참조. 업스트림이 복구되면 다시 추가 예정입니다.

#### 💼 LinkedIn
- Read person profiles, company pages, and job details via [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server)
- Search people and jobs via MCP, with Exa fallback
- Fallback to Jina Reader when MCP is not configured
- [linkedin-scraper-mcp](https://github.com/stickerdaniel/linkedin-mcp-server)를 통해 개인 프로필, 회사 페이지, 채용 공고 읽기
- MCP를 통해 인재 및 채용 공고 검색, Exa를 통해 대체 처리
- MCP가 구성되지 않은 경우 Jina Reader를 통해 대체 처리

#### 🏢 Boss直聘 (보스즈핑/BossZhiPin)
- QR code login via [mcp-bosszp](https://github.com/mucsbr/mcp-bosszp)
- Job search and recruiter greeting via MCP
- Fallback to Jina Reader for reading job pages
- [mcp-bosszp](https://github.com/mucsbr/mcp-bosszp)를 통해 QR코드 로그인
- MCP를 통해 채용 공고 검색, HR에게 메시지 전송
- Jina Reader를 통해 채용 공고 페이지 읽기 대체 처리

### 📈 Improvements / 개선 사항

- Channel count: 9 → 11 (Instagram 제거됨)
- `agent-reach doctor` now detects all 11 channels
- CLI: added `search-linkedin`, `search-bosszhipin` subcommands
- Updated install guide with setup instructions for new channels
- 채널 수: 9 → 11
- `agent-reach doctor`가 이제 모든 11개 채널을 감지
- CLI: `search-linkedin`, `search-bosszhipin` 하위 명령어 추가
- 새로운 채널에 대한 설정 설명을 설치 가이드에 추가

---

## [1.0.0] - 2025-02-24

### 🎉 Initial Release / 초기 릴리스

- 9 channels: Web, Twitter/X, YouTube, Bilibili, GitHub, Reddit, XiaoHongShu, RSS, Exa Search
- CLI with `read`, `search`, `doctor`, `install` commands
- Unified channel interface — each platform is a single pluggable Python file
- Auto-detection of local vs server environments
- Built-in diagnostics via `agent-reach doctor`
- Skill registration for Claude Code / OpenClaw / Cursor
- 9개 채널: 웹, Twitter/X, YouTube, B站(Bilibili), GitHub, Reddit, 小红书(XiaoHongShu), RSS, Exa 검색
- CLI는 `read`, `search`, `doctor`, `install` 명령어 지원
- 통합 채널 인터페이스 — 각 플랫폼은 단일 플러그인 가능한 Python 파일
- 로컬/서버 환경 자동 감지
- `agent-reach doctor`를 통한 내장 진단
- Claude Code / OpenClaw / Cursor를 위한 Skill 등록 지원
