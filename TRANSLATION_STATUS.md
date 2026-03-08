# 번역 상태 / Translation Status

업스트림 저장소: https://github.com/Panniantong/agent-reach
문서 동기화 기준 커밋: `3fe100cd9ab42b4c2474a69beebdc5c42fad8af2`
업스트림 문서 기준 시점: 2026-03-08
마지막 한글 문서 동기화: 2026-03-09

## 이번 동기화에서 반영한 핵심 변경

- 한국어 README를 업스트림 최신 문서 구조에 맞춰 재정리
- 설치/업데이트 안내의 진입 URL을 한국어 포크 문서로 변경
- OpenClaw `exec.allow` 선행 조건 반영
- 남아 있던 영어 FAQ와 어색한 표현 정리
- `docs/install.md`에 XiaoHongShu 최신 쿠키 설정 방식과 Weibo 설치 안내 반영
- `docs/wechat-qr.jpg` 정적 자산 추가

## 번역 관리 대상

| 파일 | 상태 | 비고 |
|------|------|------|
| [README.md](README.md) | ✅ 최신 반영 | 메인 한국어 문서 |
| [CHANGELOG.md](CHANGELOG.md) | ✅ 유지 | 변경 로그 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | ✅ 유지 | 기여 가이드 |
| [docs/install.md](docs/install.md) | ✅ 최신 반영 | 설치 가이드 |
| [docs/update.md](docs/update.md) | ✅ 최신 반영 | 업데이트 가이드 |
| [docs/README_en.md](docs/README_en.md) | ✅ 최신 반영 | 영문 README |
| [docs/cookie-export.md](docs/cookie-export.md) | ✅ 유지 | 쿠키 내보내기 |
| [docs/dependency-locking.md](docs/dependency-locking.md) | ✅ 유지 | 의존성 잠금 |
| [docs/troubleshooting.md](docs/troubleshooting.md) | ✅ 유지 | 문제 해결 |
| [agent_reach/guides/setup-exa.md](agent_reach/guides/setup-exa.md) | ✅ 유지 | Exa 설정 |
| [agent_reach/guides/setup-groq.md](agent_reach/guides/setup-groq.md) | ✅ 유지 | Groq 설정 |
| [agent_reach/guides/setup-reddit.md](agent_reach/guides/setup-reddit.md) | ✅ 유지 | Reddit 설정 |
| [agent_reach/guides/setup-twitter.md](agent_reach/guides/setup-twitter.md) | ✅ 유지 | Twitter 설정 |
| [agent_reach/guides/setup-wechat.md](agent_reach/guides/setup-wechat.md) | ✅ 유지 | WeChat 설정 |
| [agent_reach/guides/setup-xiaohongshu.md](agent_reach/guides/setup-xiaohongshu.md) | ✅ 유지 | XiaoHongShu 설정 |
| [agent_reach/skill/SKILL.md](agent_reach/skill/SKILL.md) | ✅ 링크 수정 | 사용 가이드 |

## 번역하지 않는 파일

- `agent_reach/*.py` - Python 소스 코드
- `tests/*.py` - 테스트 코드
- `pyproject.toml` - 프로젝트 설정
- `constraints.txt` - 의존성 제약
- `scripts/*` - 스크립트 파일

## 향후 동기화 워크플로우

```bash
# 1. 업스트림 변경 가져오기
git fetch upstream main

# 2. 문서 변경 확인
git log --oneline HEAD..upstream/main -- README.md docs agent_reach/guides agent_reach/skill/SKILL.md
git diff --stat HEAD upstream/main -- README.md docs agent_reach/guides agent_reach/skill/SKILL.md

# 3. 필요한 문서만 반영
#    - 한국어 README/가이드: 업스트림 구조를 기준으로 번역 갱신
#    - 영문 문서: 링크와 자산 경로 확인

# 4. 검증
rg -n "raw\\.githubusercontent\\.com/Panniantong/agent-reach/main" README.md docs agent_reach/skill/SKILL.md

# 5. 커밋 및 푸시
git add README.md docs agent_reach/guides agent_reach/skill/SKILL.md TRANSLATION_STATUS.md
git commit -m "docs: sync Korean translation with upstream docs"
git push origin main
```
