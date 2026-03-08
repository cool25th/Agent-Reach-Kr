# Exa Search 配置指南 / Exa 검색 설정 가이드

## 功能说明 / 기능 설명
Exa 是一个 AI 语义搜索引擎。通过 MCP 接入，**免费、无需 API Key**。配置后解锁： / Exa는 AI 시맨틱 검색 엔진입니다. MCP를 통해 연결하며 **무료, API Key 불필요**입니다. 설정 후 다음 기능이 활성화됩니다:
- 全网语义搜索 / 전체 웹 시맨틱 검색
- Reddit 搜索（通过 site:reddit.com）/ Reddit 검색 (site:reddit.com 통해)
- Twitter 搜索（通过 site:x.com）/ Twitter 검색 (site:x.com 통해)

## Agent 可自动完成的步骤 / Agent가 자동으로 완료할 수 있는 단계

`agent-reach install --env=auto` 会自动完成以下步骤，通常不需要手动操作 / 다음 단계를 자동으로 완료하므로 일반적으로 수동 작업이 필요하지 않습니다.

### 1. 安装 mcporter / mcporter 설치
```bash
npm install -g mcporter
```

### 2. 注册 Exa MCP / Exa MCP 등록
```bash
mcporter config add exa https://mcp.exa.ai/mcp
```

### 3. 验证 / 검증
```bash
agent-reach doctor | grep "Search"
mcporter call 'exa.web_search_exa(query: "test", numResults: 1)'
```

## 需要用户手动做的步骤 / 사용자가 수동으로 수행해야 하는 단계

**无 / 없음。** Exa 通过 MCP 接入，免费、无需注册、无需 API Key。 / Exa는 MCP를 통해 연결되며 무료, 가입 불필요, API Key 불필요입니다.

如果 `agent-reach install` 因为网络问题没有自动配置 Exa，手动运行上面两条命令即可。 / 네트워크 문제로 `agent-reach install`이 Exa를 자동 구성하지 못한 경우 위 두 명령을 수동으로 실행하면 됩니다.

## 常见问题 / 자주 묻는 질문

**Q: 有搜索次数限制吗？ / 검색 횟수 제한이 있나요?**
A: MCP 端点由 Exa 官方提供（mcp.exa.ai），当前免费无限制。如果未来有变化，会在 agent-reach 更新中适配。 / MCP 엔드포인트는 Exa 공식(mcp.exa.ai)에서 제공하며 현재 무료 제한 없습니다. 변화가 있으면 agent-reach 업데이트에서 반영됩니다.

**Q: mcporter 是什么？ / mcporter란 무엇인가요?**
A: MCP 协议的命令行桥接工具，用来调用 MCP Server。Agent Reach 用它来连接 Exa 和小红书。 / MCP 프로토콜의 명령행 브리지 도구로, MCP Server를 호출하는 데 사용합니다. Agent Reach는 이를 통해 Exa와 小红书(XiaoHongShu)에 연결합니다.
