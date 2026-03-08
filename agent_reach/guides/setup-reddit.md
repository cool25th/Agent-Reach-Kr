# Reddit 代理配置指南 / Reddit 프록시 설정 가이드

## 功能说明 / 기능 설명
Reddit 封锁了大量服务器 IP，直接访问会返回 403。需要 ISP 代理（Residential/ISP Proxy）才能读取完整的 Reddit 帖子和评论。 / Reddit은 많은 서버 IP를 차단하므로 직접 접근하면 403을 반환합니다. 전체 Reddit 게시물과 댓글을 읽으려면 ISP 프록시(Residential/ISP Proxy)가 필요합니다.

**注意 / 주의**：即使没有代理，也可以通过 Exa 搜索找到 Reddit 内容（只需要配 Exa API key）。代理只是用于读取完整帖子+评论。 / 프록시가 없어도 Exa 검색으로 Reddit 콘텐츠를 찾을 수 있습니다(Exa API key만 필요). 프록시는 전체 게시물+댓글 읽기용입니다.

## Agent 可自动完成的步骤 / Agent가 자동으로 완료할 수 있는 단계

1. 检查当前状态 / 현재 상태 확인:
```bash
agent-reach doctor | grep "Reddit"
```

2. 如果用户提供了代理，测试连通性 / 사용자가 프록시를 제공한 경우 연결성 테스트:
```bash
curl -s --proxy "用户提供的代理" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
  "https://www.reddit.com/r/test.json?limit=1" \
  -o /dev/null -w "%{http_code}"
```
返回 200 = 可用，403 = 代理被封，其他 = 配置错误 / 200 반환 = 사용 가능, 403 = 프록시 차단됨, 기타 = 구성 오류

3. 写入配置 / 구성에 작성:
```python
from agent_reach.config import Config
c = Config()
c.set("reddit_proxy", "http://用户名:密码@IP:端口")
```

## 需要用户手动做的步骤 / 사용자가 수동으로 수행해야 하는 단계

请告诉用户 / 사용자에게 다음을 알려주세요:

> 要完整阅读 Reddit 帖子和评论，需要一个 ISP 代理（约 $3-10/月）。 / Reddit 게시물과 댓글을 완전히 읽으려면 ISP 프록시가 필요합니다(약 $3-10/월).
>
> 推荐代理服务商（选一个就行）： / 추천 프록시 서비스 제공자(하면 선택):
> 1. **Smartproxy** (https://smartproxy.com) — ISP 代理，按流量计费 / ISP 프록시, 트래픽 기반 과금
> 2. **Bright Data** (https://brightdata.com) — 大厂，ISP 代理 / 대기업, ISP 프록시
> 3. **IPRoyal** (https://iproyal.com) — 便宜，适合入门 / 저렴, 초보자 적합
> 4. **ProxyEmpire** (https://proxyempire.io) — 有 Reddit 专用代理 / Reddit 전용 프록시 보유
>
> 购买时选择： / 구매 시 선택:
> - 类型：**ISP Proxy**（不要选 Datacenter，会被封） / 유형: **ISP Proxy** (Datacenter 선택 금지, 차단됨)
> - 地区：**美国** / 지역: **미국**
> - 协议：**HTTP** / 프로토콜: **HTTP**
>
> 购买后你会得到一个代理地址，格式类似： / 구매 후 다음 형식의 프록시 주소를 받게 됩니다:
> `http://用户名:密码@IP地址:端口号`
>
> 把这个地址发给我就行。 / 이 주소를 저에게 보내주시면 됩니다.
>
> ⚠️ 如果不想花钱，可以跳过。我仍然可以通过搜索引擎找到 Reddit 上的内容，只是不能读完整的帖子和评论。 / ⚠️ 비용을 지출하지 않으려면 건너뛰세요. 여전히 검색 엔진으로 Reddit 콘텐츠를 찾을 수 있지만 전체 게시물과 댓글은 읽을 수 없습니다.

## Agent 收到代理后的操作 / Agent가 프록시를 받은 후 작업

1. 测试代理：用 curl 测试 reddit.com 是否返回 200 / 프록시 테스트: curl로 reddit.com이 200을 반환하는지 테스트
2. 如果成功，写入配置：`config.set("reddit_proxy", proxy_url)` / 성공하면 구성에 작성: `config.set("reddit_proxy", proxy_url)`
3. 反馈："✅ Reddit 完整阅读已开启！现在我可以读取 Reddit 帖子和所有评论了。" / 피드백: "✅ Reddit 전체 읽기가 활성화되었습니다! 이제 Reddit 게시물과 모든 댓글을 읽을 수 있습니다."
4. 如果失败，告诉用户："❌ 这个代理无法访问 Reddit，请检查代理是否有效，或换一个试试。" / 실패하면 사용자에게: "❌ 이 프록시로 Reddit에 접근할 수 없습니다. 프록시가 유효한지 확인하거나 다른 것으로 시도해보세요."
