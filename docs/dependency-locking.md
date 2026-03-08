# Dependency Locking Guide / 의존성 잠금 가이드

Agent Reach uses `constraints.txt` as a reproducible dependency baseline.
Agent Reach는 `constraints.txt`를 재현 가능한 의존성 기준선으로 사용합니다.

## Why / 왜 필요한가

- Keep local/CI dependency graph stable / 로컬/CI 의존성 그래프 안정성 유지
- Reduce "works on my machine" drift / "내 컴퓨터에서는 되는데" 현상 감소
- Make regression results easier to compare / 회귀 결과 비교 용이성

## Install with constraints / 제약조건으로 설치

```bash
pip install -c constraints.txt -e .[dev]
```

## Update workflow / 업데이트 워크플로우

1. Update `pyproject.toml` dependency ranges as needed / 필요에 따라 `pyproject.toml` 의존성 범위 업데이트
2. Validate against latest compatible versions locally / 로컬에서 최신 호환 버전으로 검증
3. Update pinned versions in `constraints.txt` / `constraints.txt`의 고정 버전 업데이트
4. Run validation / 검증 실행:

```bash
pytest -q
ruff check agent_reach tests
mypy agent_reach
```

5. Open PR with dependency and validation notes / 의존성 및 검증 노트와 함께 PR 열기
