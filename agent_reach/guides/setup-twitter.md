# Twitter 高级功能配置指南（xreach CLI） / Twitter 고급 기능 설정 가이드 (xreach CLI)

Twitter 基础阅读通过 Jina Reader 免费可用，无需配置。 / Twitter 기본 읽기는 Jina Reader를 통해 무료로 제공되며 설정이 필요 없습니다.

高级功能需要 xreach CLI / 고급 기능에는 xreach CLI가 필요합니다:

- 搜索推文（`xreach search`）/ 트윗 검색 (`xreach search`)
- 读取完整推文和对话链（`xreach tweet`、`xreach thread`）/ 전체 트윗 및 대화 체인 읽기 (`xreach tweet`, `xreach thread`)
- 用户时间线（`xreach tweets`）/ 사용자 타임라인 (`xreach tweets`)

xreach 是免费开源工具（npm 包 xreach-cli），但需要你的 Twitter 账号 cookie。 / xreach는 무료 오픈소스 도구(npm 패키지 xreach-cli)이지만 Twitter 계정 쿠키가 필요합니다.

## 快速配置 / 빠른 설정

1. 检查 xreach 是否安装 / xreach 설치 확인:

```bash
which xreach && echo "installed" || echo "not installed"
```

2. 安装 xreach / xreach 설치:

```bash
npm install -g xreach-cli
```

3. 测试是否配置好 / 구성 테스트:

```bash
AUTH_TOKEN="xxx" CT0="yyy" xreach search "test" -n 1
```

## 获取 Cookie（Cookie-Editor 方式，推荐） / 쿠키 가져오기 (Cookie-Editor 방식, 권장)

1. 安装 [Cookie-Editor](https://cookie-editor.com/) 浏览器扩展 / [Cookie-Editor](https://cookie-editor.com/) 브라우저 확장 프로그램 설치
2. 登录 x.com / x.com 로그인
3. 点击 Cookie-Editor 图标 → Export → 复制全部 / Cookie-Editor 아이콘 클릭 → Export → 전체 복사
4. 运行配置命令 / 구성 명령 실행:

```bash
agent-reach configure twitter-cookies "粘贴的 cookie JSON"
```

这会自动提取 `auth_token` 和 `ct0`，并写入环境变量。 / 이렇게 하면 `auth_token`과 `ct0`가 자동으로 추출되어 환경 변수에 기록됩니다.

## 手动设置 Cookie / 수동 쿠키 설정

如果你已经知道 `auth_token` 和 `ct0` / 이미 `auth_token`과 `ct0`를 알고 있는 경우:

1. 安装 xreach（如果没装）：`npm install -g xreach-cli` / xreach 설치 (설치되지 않은 경우): `npm install -g xreach-cli`

2. 设置环境变量 / 환경 변수 설정:

```bash
export AUTH_TOKEN="你的auth_token"
export CT0="你的ct0"
```

3. 测试 / 테스트:

```bash
xreach search "test" --auth-token "$AUTH_TOKEN" --ct0 "$CT0" -n 1
```

## 代理配置 / 프록시 구성

> xreach CLI 内置代理支持，通过 `--proxy` 参数传入 / xreach CLI는 내장 프록시 지원을 제공하며 `--proxy` 파라미터로 전달:

```bash
xreach search "test" --auth-token "$AUTH_TOKEN" --ct0 "$CT0" --proxy "http://user:pass@host:port"
```

也支持代理轮换文件 / 프록시 로테이션 파일도 지원:

```bash
xreach search "test" --auth-token "$AUTH_TOKEN" --ct0 "$CT0" --proxy-file proxies.txt
```
