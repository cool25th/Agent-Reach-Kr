# 번역 상태 / Translation Status

업스트림: https://github.com/Panniantong/agent-reach
업스트림 버전: v1.1.0
마지막 동기화: 2025-03-08

## 번역 완료된 파일

| 파일 | 상태 | 비고 |
|------|------|------|
| README.md | ✅ 완료 | 메인 문서 |
| CHANGELOG.md | ✅ 완료 | 변경 로그 |
| CONTRIBUTING.md | ✅ 완료 | 기여 가이드 |
| docs/install.md | ✅ 완료 | 설치 가이드 |
| docs/cookie-export.md | ✅ 완료 | 쿠키 내보내기 |
| docs/dependency-locking.md | ✅ 완료 | 의존성 잠금 |
| docs/troubleshooting.md | ✅ 완료 | 문제 해결 |
| docs/update.md | ✅ 완료 | 업데이트 가이드 |
| agent_reach/guides/setup-exa.md | ✅ 완료 | Exa 설정 |
| agent_reach/guides/setup-groq.md | ✅ 완료 | Groq 설정 |
| agent_reach/guides/setup-reddit.md | ✅ 완료 | Reddit 설정 |
| agent_reach/guides/setup-twitter.md | ✅ 완료 | Twitter 설정 |
| agent_reach/guides/setup-wechat.md | ✅ 완료 | WeChat 설정 |
| agent_reach/guides/setup-xiaohongshu.md | ✅ 완료 | XiaoHongShu 설정 |
| agent_reach/skill/SKILL.md | ✅ 완료 | 사용 가이드 |

## 번역하지 않는 파일

- `agent_reach/*.py` - Python 소스 코드
- `tests/*.py` - 테스트 코드
- `pyproject.toml` - 프로젝트 설정
- `constraints.txt` - 의존성 제약
- `scripts/*` - 스크립트 파일

## 향후 업스트림 동기화 워크플로우

```bash
# 1. 업스트림 변경사항 가져오기
git fetch upstream

# 2. 변경사항 확인
git log HEAD..upstream/main --oneline
git diff HEAD upstream/main --stat

# 3. 병합 (한국어 번역 보존)
git merge upstream/main

# 4. 충돌 해결
#    - 번역된 파일: 한국어 버전 유지 (ours)
#    - 코드 파일: 업스트림 변경사항 수용

# 5. Push
git push origin main
```
