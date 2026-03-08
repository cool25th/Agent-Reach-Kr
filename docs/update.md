# Agent Reach — Update Guide / 업데이트 가이드

## For Humans / 사용자용

Copy this to your AI Agent / 이 내용을 AI Agent에 복사하세요:

```
帮我更新 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

Or in English / 또는 영어로:

```
Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

---

## For AI Agents / AI Agent용

### ⚠️ Workspace Rules / 워크스페이스 규칙

**Never create files, clone repos, or run commands in the agent workspace. Use `/tmp/` for temporary work and `~/.agent-reach/` for persistent data.** / **에이전트 워크스페이스에 파일을 생성하거나 리포지토리를 복제하거나 명령을 실행하지 마세요. 임시 작업은 `/tmp/`를, 영구 데이터는 `~/.agent-reach/`를 사용하세요.**

### Goal / 목표

Update Agent Reach to the latest version, then verify everything still works. / Agent Reach를 최신 버전으로 업데이트한 다음 모든 것이 정상 작동하는지 확인합니다.

### Step 1: Check current version / 1단계: 현재 버전 확인

```bash
agent-reach check-update
```

If it says "已是最新版本", you're done — tell the user. / "已是最新版本"(이미 최신 버전입니다)라고 표시되면 완료된 것입니다 — 사용자에게 알려주세요.

### Step 2: Update / 2단계: 업데이트

```bash
pip install --upgrade https://github.com/Panniantong/agent-reach/archive/main.zip
```

### Step 3: Verify / 3단계: 검증

```bash
agent-reach version
agent-reach doctor
```

Report the new version and channel status to the user. If any channel changed status (was ✅ now ❌), investigate and fix. / 새 버전과 채널 상태를 사용자에게 보고하세요. 채널 상태가 변경된 경우(✅이었는데 ❌가 된 경우) 조사하고 수정하세요.

### Step 4: Update SKILL.md (if installed) / 4단계: SKILL.md 업데이트 (설치된 경우)

If the user has the Agent Reach skill installed, update it too / 사용자가 Agent Reach 스킬을 설치한 경우 업데이트도 해주세요:

```bash
agent-reach install --skill-only
```

If the `--skill-only` flag is not available, manually copy the latest SKILL.md / `--skill-only` 플래그를 사용할 수 없는 경우 최신 SKILL.md를 수동으로 복사하세요:

```bash
python3 -c "
import importlib.resources, shutil, os
skill = importlib.resources.files('agent_reach').joinpath('skill', 'SKILL.md').read_text()
for d in [os.path.expanduser('~/.openclaw/skills/agent-reach'),
          os.path.expanduser('~/.claude/skills/agent-reach')]:
    if os.path.isdir(d):
        with open(os.path.join(d, 'SKILL.md'), 'w') as f:
            f.write(skill)
        print(f'✅ Updated: {d}')
"
```

Done. Tell the user what version they're now on and how many channels are available. / 완료되었습니다. 사용자에게 현재 버전과 사용 가능한 채널 수를 알려주세요.
