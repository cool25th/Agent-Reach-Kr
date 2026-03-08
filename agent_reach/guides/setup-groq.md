# Groq Whisper 配置指南 / Groq Whisper 설정 가이드

## 功能说明 / 기능 설명
当 YouTube/Bilibili 视频没有字幕时，用 Groq 的 Whisper API 进行语音转文字。Groq 提供免费额度。 / YouTube/Bilibili 동영상에 자막이 없을 때 Groq의 Whisper API를 사용하여 음성을 텍스트로 변환합니다. Groq는 무료 할당량을 제공합니다.

## Agent 可自动完成的步骤 / Agent가 자동으로 완료할 수 있는 단계

1. 检查是否已配置 / 구성되어 있는지 확인:
```bash
agent-reach doctor | grep -i "groq\|whisper"
```

2. 如果用户提供了 key，写入配置 / 사용자가 키를 제공한 경우 구성에 작성:
```python
from agent_reach.config import Config
c = Config()
c.set("groq_api_key", "用户提供的KEY")
```

3. 测试（可选） / 테스트 (선택사항):
```bash
curl -s https://api.groq.com/openai/v1/models \
  -H "Authorization: Bearer 用户提供的KEY" \
  -o /dev/null -w "%{http_code}"
```
返回 200 = 可用 / 200 반환 = 사용 가능

## 需要用户手动做的步骤 / 사용자가 수동으로 수행해야 하는 단계

请告诉用户 / 사용자에게 다음을 알려주세요:

> 视频语音转文字需要一个 Groq API Key（免费）。 / 동영상 음성을 텍스트로 변환하려면 Groq API Key가 필요합니다(무료).
>
> 步骤 / 단계:
> 1. 打开 https://console.groq.com / https://console.groq.com 열기
> 2. 用 Google 账号或邮箱注册 / Google 계정 또는 이메일로 가입
> 3. 点击左侧 "API Keys" / 왼쪽 "API Keys" 클릭
> 4. 点击 "Create API Key" / "Create API Key" 클릭
> 5. 复制生成的 Key，发给我 / 생성된 키를 복사하여 저에게 보내주세요
>
> Groq 提供免费额度，日常使用完全够用。 / Groq는 무료 할당량을 제공하며 일상 사용에 충분합니다.

## Agent 收到 key 后的操作 / Agent가 키를 받은 후 작업

1. 写入配置：`config.set("groq_api_key", key)` / 구성에 작성: `config.set("groq_api_key", key)`
2. 测试 API 可用性 / API 사용 가능성 테스트
3. 反馈："✅ 语音转文字已开启！现在遇到没有字幕的视频，我也能帮你提取内容了。" / 피드백: "✅ 음성을 텍스트로 변환하는 기능이 활성화되었습니다! 이제 자막이 없는 동영상도 내용을 추출할 수 있습니다."
