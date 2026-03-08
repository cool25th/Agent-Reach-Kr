# Cookie Export Guide — For Server Users / 쿠키 내보내기 가이드 — 서버 사용자용

Your Agent is on a server and can't access your browser directly.
Here's how to export cookies from your local computer — **fastest method first**.
에이전트가 서버에 있어 브라우저에 직접 접근할 수 없습니다.
로컬 컴퓨터에서 쿠키를 내보내는 방법입니다 — **가장 빠른 방법부터**.

## Method 1: Cookie-Editor Extension (Recommended — 30 seconds per site) / 방법 1: Cookie-Editor 확장 프로그램 (권장 — 사이트당 30초)

1. Install **Cookie-Editor** for Chrome / Chrome용 **Cookie-Editor** 설치: https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm
   (Also available for Firefox, Edge / Firefox, Edge에서도 사용 가능)

2. Go to the website (e.g. https://x.com) and make sure you're logged in / 웹사이트로 이동(예: https://x.com)하고 로그인되어 있는지 확인

3. Click the Cookie-Editor icon in your toolbar / 툴바에서 Cookie-Editor 아이콘 클릭

4. Click **Export** → **Header String** / **내보내기** → **헤더 문자열** 클릭

5. Paste the result to your Agent / 결과를 에이전트에 붙여넣기

That's it! Your Agent will run: / 이게 끝입니다! 에이전트가 다음을 실행합니다:
```bash
agent-reach configure twitter-cookies <your_pasted_string>
```

### Sites to export / 내보낼 사이트:

| Site / 사이트 | URL to visit / 방문할 URL | What to tell Agent / 에이전트에게 알릴 내용 |
|------|-------------|-------------------|
| Twitter/X | https://x.com | "Here are my Twitter cookies: [paste]" / "제 Twitter 쿠키입니다: [붙여넣기]" |
| XiaoHongShu | https://www.xiaohongshu.com | "Here are my XHS cookies: [paste]" / "제 XHS 쿠키입니다: [붙여넣기]" |
| Bilibili | https://www.bilibili.com | "Here are my Bilibili cookies: [paste]" / "제 Bilibili 쿠키입니다: [붙여넣기]" |

## Method 2: Manual (No extension needed) / 방법 2: 수동 (확장 프로그램 불필요)

1. Open the site in Chrome, make sure you're logged in / Chrome에서 사이트 열기, 로그인되어 있는지 확인
2. Press **F12** (or right-click → Inspect) / **F12** 누름 (또는 마우스 오른쪽 클릭 → 검사)
3. Click the **Network** tab / **네트워크** 탭 클릭
4. Refresh the page (F5) / 페이지 새로고침 (F5)
5. Click any request in the list / 목록에서 요청 하나 클릭
6. In the right panel, scroll to **Request Headers** / 오른쪽 패널에서 **요청 헤더**로 스크롤
7. Find the line starting with `Cookie:` / `Cookie:`로 시작하는 줄 찾기
8. Copy the entire value after `Cookie: ` / `Cookie: ` 뒤의 전체 값 복사
9. Paste to your Agent / 에이전트에 붙여넣기
