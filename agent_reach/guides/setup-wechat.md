# 微信公众号配置指南 / 위챗 공식계정 설정 가이드

## 功能说明 / 기능 설명
读取微信公众号文章。需要 Playwright 来处理微信的反爬机制。 / 위챗 공식계정(WeChat MP) 기사를 읽습니다. 위챗의 크롤링 방지 메커니즘을 처리하려면 Playwright가 필요합니다.

## Agent 可自动完成的步骤 / Agent가 자동으로 완료할 수 있는 단계

1. 检查 Playwright 是否安装 / Playwright 설치 확인:
```bash
python3 -c "import playwright; print('installed')" 2>&1
```

2. 安装 Playwright + 浏览器 / Playwright + 브라우저 설치:
```bash
pip install playwright
playwright install chromium
```

3. 安装完成后测试 / 설치 후 테스트:
```bash
curl -s "https://r.jina.ai/https://mp.weixin.qq.com/s/一个测试链接" -H "Accept: text/markdown"
```

## 需要用户手动做的步骤 / 사용자가 수동으로 수행해야 하는 단계

请告诉用户 / 사용자에게 다음을 알려주세요:

> 微信公众号的配置很简单，只需要安装一个浏览器组件（约 150MB）。 / 위챗 공식계정 설정은 간단하며 브라우저 컴포넌트(약 150MB)만 설치하면 됩니다.
>
> 我来帮你安装，你不需要做任何事情。安装过程大约 1-2 分钟。 / 제가 설치를 도와드리니 아무것도 하실 필요가 없습니다. 설치 과정은 약 1-2분 소요됩니다.
>
> 安装好之后就可以直接读取微信公众号文章了，不需要登录。 / 설치 후 위챗 공식계정 기사를 바로 읽을 수 있으며 로그인이 필요하지 않습니다.

## Agent 操作流程 / Agent 작업 흐름

1. 安装 Playwright：`pip install playwright` / Playwright 설치: `pip install playwright`
2. 安装 Chromium：`playwright install chromium` / Chromium 설치: `playwright install chromium`
3. 测试：读一篇微信文章 / 테스트: 위챗 기사 읽기
4. 反馈："✅ 微信公众号已配置！发给我任何公众号文章链接，我都能读取。" / 피드백: "✅ 위챗 공식계정이 구성되었습니다! 모든 공식계정 기사 링크를 보내주시면 읽을 수 있습니다."
5. 如果安装失败（空间不足等）："❌ 浏览器组件安装失败。可能是磁盘空间不足（需要约 150MB）。" / 설치 실패 시(공간 부족 등): "❌ 브라우저 컴포넌트 설치 실패. 디스크 공간이 부족할 수 있습니다(약 150MB 필요)."
