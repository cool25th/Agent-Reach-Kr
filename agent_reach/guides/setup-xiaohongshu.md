# 小红书配置指南 / 小红书(샤오홍슈/XiaoHongShu) 설정 가이드

## 功能说明 / 기능 설명
读取和搜索小红书笔记。通过 [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) 实现（⭐9K+，Go 语言，内置 Chrome 浏览器）。 / 小红书(샤오홍슈/XiaoHongShu) 노트를 읽고 검색합니다. [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)를 통해 구현됩니다(⭐9K+, Go 언어, 내장 Chrome 브라우저).

## 前置条件 / 전제 조건
- Docker（用来运行 xiaohongshu-mcp 服务） / Docker (xiaohongshu-mcp 서비스 실행용)
- mcporter CLI（MCP 协议桥接工具） / mcporter CLI (MCP 프로토콜 브리지 도구)

## Agent 可自动完成的步骤 / Agent가 자동으로 완료할 수 있는 단계

### 1. 安装 mcporter / mcporter 설치
```bash
npm install -g mcporter
```

### 2. 启动 xiaohongshu-mcp 服务 / xiaohongshu-mcp 서비스 시작
```bash
docker run -d \
  --name xiaohongshu-mcp \
  -p 18060:18060 \
  xpzouying/xiaohongshu-mcp
```

> 如需代理（服务器部署推荐）： / 프록시가 필요한 경우(서버 배포 권장):
> ```bash
> docker run -d \
>   --name xiaohongshu-mcp \
>   -p 18060:18060 \
>   -e XHS_PROXY=http://user:pass@ip:port \
>   xpzouying/xiaohongshu-mcp
> ```

### 3. 注册到 mcporter / mcporter에 등록
```bash
mcporter config add xiaohongshu http://localhost:18060/mcp
```

### 4. 验证 / 검증
```bash
agent-reach doctor
```

应该看到小红书显示为 ✅ 或 ⚠️（MCP 已连接但未登录）。 / 小红书가 ✅ 또는 ⚠️(MCP 연결됨 but 로그인 안됨)로 표시되어야 합니다.

## 需要用户手动做的步骤 / 사용자가 수동으로 수행해야 하는 단계

如果 doctor 显示"MCP 已连接但未登录" / doctor가 "MCP 연결됨 but 로그인 안됨"을 표시하는 경우:

> 小红书需要登录一次（之后会记住你的登录状态）。 / 小红书는 한 번 로그인해야 합니다(이후 로그인 상태가 저장됨).
>
> 打开 http://localhost:18060 ，用手机小红书 App 扫描二维码登录。 / http://localhost:18060을 열고 모바일 小红书 App으로 QR 코드를 스캔하여 로그인하세요.
> 登录后 cookie 会自动保存在 Docker 容器内，大约 1-3 个月有效。 / 로그인 후 쿠키는 Docker 컨테이너 내에 자동 저장되며 약 1-3개월 유효합니다.

## 常见问题 / 자주 묻는 질문

**Q: Docker 容器重启后 cookie 丢了？** / **Q: Docker 컨테이너 재시작 후 쿠키가 사라졌나요?**
A: 挂载数据卷持久化 / 데이터 볼륨 마운트로 지속성 확보:
```bash
docker run -d \
  --name xiaohongshu-mcp \
  -p 18060:18060 \
  -v xhs-data:/app/data \
  xpzouying/xiaohongshu-mcp
```

**Q: 服务器上小红书提示 IP 风险？** / **Q: 서버에서 小红书가 IP 위험을 표시하나요?**
A: 加代理参数 `-e XHS_PROXY=http://user:pass@ip:port`，推荐住宅代理。 / 프록시 파라미터 `-e XHS_PROXY=http://user:pass@ip:port` 추가, 주거용 프록시 권장.

**Q: Docker 镜像不支持 ARM64 / Apple Silicon？** / **Q: Docker 이미지가 ARM64/Apple Silicon을 지원하지 않나요?**
A: 上游镜像暂无 ARM64 版本，两种解决办法 / 업스트림 이미지는 아직 ARM64 버전이 없으며 두 가지 해결 방법이 있습니다:

方法一：使用 Rosetta 模拟运行（推荐，最简单） / 방법 1: Rosetta 에뮬레이션 사용 (권장, 가장 간단)
```bash
docker run -d \
  --name xiaohongshu-mcp \
  -p 18060:18060 \
  --platform linux/amd64 \
  xpzouying/xiaohongshu-mcp
```

方法二：从源码编译原生 ARM64 版本 / 방법 2: 소스에서 네이티브 ARM64 버전 컴파일
```bash
git clone https://github.com/xpzouying/xiaohongshu-mcp
cd xiaohongshu-mcp
docker build -t xiaohongshu-mcp .
docker run -d --name xiaohongshu-mcp -p 18060:18060 xiaohongshu-mcp
```

**Q: 我不想用 Docker？** / **Q: Docker를 사용하고 싶지 않나요?**
A: 可以从源码编译：https://github.com/xpzouying/xiaohongshu-mcp / 소스에서 컴파일 가능: https://github.com/xpzouying/xiaohongshu-mcp
