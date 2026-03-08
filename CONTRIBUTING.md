# Contributing to Agent Reach

Agent Reach에 기여해 주셔서 감사합니다! 이 문서는 기여 가이드라인과 지침을 제공합니다.

## Getting Started / 시작하기

1. GitHub에서 저장소를 포크(Fork)합니다
2. 포크를 로컬에 클론합니다
3. 기여를 위한 새 브랜치를 만듭니다
4. 변경 사항을 적용합니다
5. 테스트와 린트(Lint)를 실행합니다
6. 풀 리퀘스트(PR)를 제출합니다

## Development Setup / 개발 환경 설정

```bash
# Clone your fork / 포크 클론
git clone https://github.com/YOUR_USERNAME/Agent-Reach.git
cd Agent-Reach

# Install in development mode / 개발 모드로 설치
pip install -e ".[dev]"

# Install pre-commit hooks (optional but recommended) / pre-commit 후크 설치 (선택사항 but 권장)
pre-commit install
```

## Code Style / 코드 스타일

다음 도구를 사용하여 코드 품질을 유지합니다:

- **ruff**: 린트(Linting) 및 임포트 정렬
- **mypy**: 타입 검사
- **pytest**: 테스트

PR 제출 전 모든 검사를 실행하세요:

```bash
# Linting / 린트
ruff check agent_reach tests
ruff format agent_reach tests

# Type checking / 타입 검사
mypy agent_reach

# Tests / 테스트
pytest
```

## Adding New Channels / 새 채널 추가

Agent Reach는 통합 채널 인터페이스를 사용합니다. 새 플랫폼을 추가하려면:

1. `agent_reach/channels/`에 새 파일을 만듭니다
2. 채널 계약을 구현합니다 (기존 채널을 예시로 참조)
3. `tests/test_channels.py`에 테스트를 추가합니다
4. `agent_reach/doctor.py`를 업데이트하여 새 채널을 포함합니다
5. 문서를 업데이트합니다

## Pull Request Guidelines / 풀 리퀘스트 가이드라인

- 대규모 리팩토링보다 **작고 집중된 변경**을 선호합니다
- 새 기능에 대한 테스트를 포함하세요
- 필요한 경우 문서를 업데이트하세요
- 기존 코드 스타일을 따르세요
- 관련 이슈(Issue)를 참조하세요

## Reporting Issues / 이슈 보고

버그를 보고할 때 다음을 포함하세요:

- Python 버전
- 운영체제
- 재현 단계
- 예상 동작 vs 실제 동작
- 에러 메시지 (있는 경우)

## Questions? / 질문이 있으신가요?

질문이나 토론을 위해 이슈를 열어주세요.
