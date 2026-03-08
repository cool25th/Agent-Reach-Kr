# Agent Reach — Update Guide / 업데이트 가이드

## For Humans / 사용자용

이 문장을 AI Agent에 복사하세요:

```text
Agent Reach 업데이트 도와줘: https://raw.githubusercontent.com/cool25th/Agent-Reach-Kr/main/docs/update.md
```

영문으로 요청하고 싶다면:

```text
Update Agent Reach: https://raw.githubusercontent.com/cool25th/Agent-Reach-Kr/main/docs/update.md
```

---

## For AI Agents / AI Agent용

### ⚠️ Workspace Rules / 워크스페이스 규칙

**Never create files, clone repos, or run commands in the agent workspace.** Use `/tmp/` for temporary work and `~/.agent-reach/` for persistent data.
**에이전트 워크스페이스 안에서는 파일 생성, 저장소 복제, 명령 실행을 하지 마세요.** 임시 작업은 `/tmp/`, 영구 데이터는 `~/.agent-reach/`를 사용하세요.

### Goal / 목표

Update Agent Reach to the latest version, then verify everything still works.
Agent Reach를 최신 버전으로 업데이트한 뒤 모든 채널이 계속 정상 동작하는지 검증합니다.

### Step 1: Check current version / 1단계: 현재 버전 확인

```bash
agent-reach check-update
```

If it says `"已是最新版本"`, you're done. Tell the user no update is needed.
출력에 `"已是最新版本"`이 보이면 이미 최신 버전입니다. 사용자에게 업데이트가 필요 없다고 알려주세요.

### Step 2: Update / 2단계: 업데이트

```bash
pip install --upgrade https://github.com/Panniantong/agent-reach/archive/main.zip
```

### Step 3: Verify / 3단계: 검증

```bash
agent-reach version
agent-reach doctor
```

Report the new version and channel status to the user. If any channel regressed from ✅ to ❌, investigate and fix it.
새 버전과 채널 상태를 사용자에게 보고하세요. 기존에 ✅였던 채널이 ❌로 바뀌었다면 원인을 조사하고 수정하세요.

### Step 4: Update SKILL.md if needed / 4단계: 필요 시 SKILL.md도 업데이트

If the user has the Agent Reach skill installed, update it too:
사용자가 Agent Reach 스킬을 설치해 두었다면 함께 업데이트하세요.

```bash
agent-reach install --skill-only
```

If `--skill-only` is unavailable, manually copy the latest `SKILL.md`:
`--skill-only` 플래그를 지원하지 않으면 최신 `SKILL.md`를 직접 복사하세요.

```bash
python3 -c "
import importlib.resources, os
skill = importlib.resources.files('agent_reach').joinpath('skill', 'SKILL.md').read_text()
for d in [os.path.expanduser('~/.openclaw/skills/agent-reach'),
          os.path.expanduser('~/.claude/skills/agent-reach')]:
    if os.path.isdir(d):
        with open(os.path.join(d, 'SKILL.md'), 'w') as f:
            f.write(skill)
        print(f'✅ Updated: {d}')
"
```

Done. Tell the user what version they're on now and how many channels are available.
완료되면 현재 버전과 사용 가능한 채널 수를 사용자에게 알려주세요.
