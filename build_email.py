
import json, base64
from datetime import datetime

with open('/sessions/beautiful-peaceful-hamilton/charts_b64.json') as f:
    charts = json.load(f)

today = datetime.now().strftime('%Y年%m月%d日')

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>股票新闻 - PLTR & 英伟达每日简报</title>
<style>
  body{{margin:0;padding:0;background:#0d1117;font-family:'Segoe UI',Arial,sans-serif;color:#e6edf3}}
  .wrap{{max-width:780px;margin:0 auto;padding:20px}}
  /* Header */
  .hdr{{background:linear-gradient(135deg,#1f2d3d,#0d1f33);border-radius:14px;padding:28px 30px;text-align:center;border:1px solid #1e4a6e;margin-bottom:22px}}
  .hdr h1{{margin:0 0 6px;font-size:26px;color:#58a6ff;letter-spacing:1px}}
  .hdr p{{margin:0;color:#8b949e;font-size:13px}}
  .hdr .badge{{display:inline-block;background:#1e4a6e;color:#58a6ff;padding:4px 14px;border-radius:20px;font-size:12px;margin-top:10px}}
  /* Section */
  .sec{{background:#161b22;border-radius:12px;padding:22px 24px;margin-bottom:18px;border:1px solid #21262d}}
  .sec-title{{font-size:17px;font-weight:700;color:#58a6ff;border-bottom:1px solid #21262d;padding-bottom:10px;margin:0 0 16px}}
  /* Stock tag */
  .tag-pltr{{display:inline-block;background:#1c2e42;color:#79c0ff;padding:2px 10px;border-radius:12px;font-size:11px;font-weight:700;margin-bottom:10px}}
  .tag-nvda{{display:inline-block;background:#1a2f1a;color:#56d364;padding:2px 10px;border-radius:12px;font-size:11px;font-weight:700;margin-bottom:10px}}
  /* News item */
  .news{{background:#0d1117;border-left:3px solid #58a6ff;border-radius:6px;padding:12px 16px;margin-bottom:10px}}
  .news.nvda{{border-left-color:#56d364}}
  .news-title{{font-size:13px;font-weight:700;color:#e6edf3;margin-bottom:5px}}
  .news-sum{{font-size:12px;color:#8b949e;line-height:1.6;margin-bottom:6px}}
  .news-src a{{font-size:11px;color:#58a6ff;text-decoration:none}}
  .news-src a:hover{{text-decoration:underline}}
  /* Reddit */
  .reddit{{background:#0d1117;border-left:3px solid #ff4500;border-radius:6px;padding:12px 16px;margin-bottom:10px}}
  .reddit-title{{font-size:13px;font-weight:700;color:#e6edf3;margin-bottom:5px}}
  .reddit-sum{{font-size:12px;color:#8b949e;line-height:1.6;margin-bottom:6px}}
  .reddit-link a{{font-size:11px;color:#ff6b35;text-decoration:none}}
  /* Sentiment grid */
  .sent-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:4px}}
  .sent-card{{background:#0d1117;border-radius:8px;padding:14px;text-align:center;border:1px solid #21262d}}
  .sent-card .ticker{{font-size:18px;font-weight:800;margin-bottom:4px}}
  .sent-card .price{{font-size:22px;font-weight:700;color:#e6edf3;margin-bottom:2px}}
  .sent-card .chg-up{{color:#56d364;font-size:13px}}
  .sent-card .chg-dn{{color:#f85149;font-size:13px}}
  .badge-strong-buy{{background:#1a3a1a;color:#56d364;padding:3px 12px;border-radius:12px;font-size:11px;font-weight:700}}
  .badge-buy{{background:#1c2e42;color:#79c0ff;padding:3px 12px;border-radius:12px;font-size:11px;font-weight:700}}
  .badge-hold{{background:#2d2a1a;color:#d29922;padding:3px 12px;border-radius:12px;font-size:11px;font-weight:700}}
  .target{{font-size:12px;color:#8b949e;margin-top:6px}}
  .target span{{color:#e6edf3;font-weight:600}}
  /* Analyst opinions */
  .opinion{{background:#0d1117;border-radius:6px;padding:10px 14px;margin:8px 0;font-size:12px;color:#8b949e;border:1px solid #21262d}}
  .opinion strong{{color:#e6edf3}}
  /* Charts */
  .chart-wrap{{text-align:center;margin-top:12px}}
  .chart-wrap img{{width:100%;max-width:720px;border-radius:10px;border:1px solid #21262d}}
  /* Divider */
  .divider{{border:none;border-top:1px solid #21262d;margin:16px 0}}
  /* Footer */
  .ftr{{text-align:center;color:#484f58;font-size:11px;margin-top:24px;padding-top:16px;border-top:1px solid #21262d}}
</style>
</head>
<body>
<div class="wrap">

<!-- HEADER -->
<div class="hdr">
  <h1>📈 股票每日简报</h1>
  <p>Palantir (PLTR) &amp; 英伟达 (NVDA) · {today}</p>
  <span class="badge">自动生成 · 数据来源：公开金融信息</span>
</div>

<!-- SECTION 1: NEWS -->
<div class="sec">
  <div class="sec-title">📰 今日重要新闻与研究报告</div>

  <span class="tag-pltr">PLTR · Palantir</span>

  <div class="news">
    <div class="news-title">① 伊朗冲突推动军事AI需求，Palantir本周大涨10.8%</div>
    <div class="news-sum">随着美国与伊朗紧张局势升级，军事级AI需求急剧上升，Palantir凭借其国防AI软件平台成为最大受益者。本周股价上涨10.8%，分析师普遍认为地缘政治风险将持续利好公司订单。</div>
    <div class="news-src">来源：<a href="https://www.tipranks.com/stocks/pltr" target="_blank">TipRanks · Mar 4, 2026</a></div>
  </div>

  <div class="news">
    <div class="news-title">② 五角大楼要求Palantir从军事软件中移除Anthropic Claude模型</div>
    <div class="news-sum">美国国防部将Anthropic列为"供应链风险"，要求Palantir从关键军事软件平台中移除Claude AI模型。此事件短期造成市场不确定性，Piper Sandler警告可能出现近期波动，但维持长期看涨立场。</div>
    <div class="news-src">来源：<a href="https://www.gurufocus.com/news/8672002" target="_blank">GuruFocus · Mar 2026</a></div>
  </div>

  <div class="news">
    <div class="news-title">③ Rosenblatt上调目标价至$200，维持买入评级；花旗更激进喊价$260</div>
    <div class="news-sum">Rosenblatt分析师John McPeake于3月3日将PLTR目标价从$150上调至$200，继续维持"买入"评级，理由是美国商业AI业务137%的同比增速超出预期。花旗分析师更为乐观，目标价达$260，较当前股价有约70%上行空间。</div>
    <div class="news-src">来源：<a href="https://www.marketbeat.com/stocks/NASDAQ/PLTR/forecast/" target="_blank">MarketBeat &amp; Techi.com · Mar 3, 2026</a></div>
  </div>

  <hr class="divider">
  <span class="tag-nvda">NVDA · 英伟达</span>

  <div class="news nvda">
    <div class="news-title">① 英伟达Q4财年2026营收$681亿，同比增长73%；Q1指引$780亿</div>
    <div class="news-sum">英伟达公布创纪录财季业绩：FY2026全年营收$2159亿（同比+65%），其中第四季度$681亿（同比+73%）。公司给出下季度$780亿±2%的营收指引，显示AI基础设施需求仍处于爆发阶段。</div>
    <div class="news-src">来源：<a href="https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026" target="_blank">NVIDIA Newsroom · 官方公告</a></div>
  </div>

  <div class="news nvda">
    <div class="news-title">② Meta $1150亿AI豪赌将英伟达推向多年增长周期核心</div>
    <div class="news-sum">Meta宣布2026年资本支出达$1150亿至$1350亿，其中绝大部分流向英伟达GPU采购。分析师指出，包括微软、谷歌、亚马逊在内的超大规模云厂商的AI基建投资将持续支撑英伟达数据中心业务，形成多年增长周期。</div>
    <div class="news-src">来源：<a href="https://247wallst.com/investing/2026/02/19/metas-115-billion-ai-bet-puts-nvidia-at-the-center-of-a-multi-year-spending-cycle/" target="_blank">24/7 Wall St. · Feb 19, 2026</a></div>
  </div>

  <div class="news nvda">
    <div class="news-title">③ GTC 2026大会在即：Jensen Huang将展示"AI时代"——分析师预测3月或成转折点</div>
    <div class="news-sum">英伟达GTC 2026年度开发者大会即将召开，CEO黄仁勋将联合全球科技领袖展示下一代AI架构与Blackwell Ultra芯片路线图。Motley Fool分析师认为，GTC大会往往是英伟达股价的重要催化剂，3月可能成为本轮反弹的关键转折点。</div>
    <div class="news-src">来源：<a href="https://www.fool.com/investing/2026/03/04/why-march-could-be-a-turning-point-for-nvidia/" target="_blank">The Motley Fool · Mar 4, 2026</a></div>
  </div>
</div>

<!-- SECTION 2: REDDIT -->
<div class="sec">
  <div class="sec-title">💬 Reddit 社区热议</div>

  <span class="tag-pltr">PLTR Reddit</span>

  <div class="reddit">
    <div class="reddit-title">r/PLTR — "Papa Karp" 粉丝社区：估值之争 vs. 持股到瓦尔哈拉</div>
    <div class="reddit-sum">近5万成员的r/PLTR社区对Q4业绩（营收$14亿，YoY+70%）反应极为热烈。社区形成了围绕CEO Alex Karp的"信仰文化"，自称"Palantards"，坚持长期持有。核心争论在于：传统PE估值是否适用于AI软件公司？多数成员认为不适用，预期2026年$7.2B营收指引将持续吸引机构资金。</div>
    <div class="reddit-link">来源：<a href="https://www.reddit.com/r/PLTR/" target="_blank">r/PLTR subreddit</a> &amp; <a href="https://www.bitget.com/en-CA/wiki/palantir-stock-reddit" target="_blank">Bitget PLTR Reddit分析</a></div>
  </div>

  <div class="reddit">
    <div class="reddit-title">r/wallstreetbets — PLTR出现在本周热门股票列表，与Alibaba、英伟达并列</div>
    <div class="reddit-sum">WallStreetBets本周热议榜单显示PLTR与NVDA、BABA、Moderna同时上榜，散户情绪因伊朗事件而显著升温。部分帖子讨论五角大楼/Anthropic事件是否构成买入良机，多数观点认为短期利空已被过度解读。</div>
    <div class="reddit-link">来源：<a href="https://finance.yahoo.com/news/pfizer-alibaba-nvidia-moderna-palantir-105348563.html" target="_blank">Yahoo Finance WallStreetBets报道</a></div>
  </div>

  <hr class="divider">
  <span class="tag-nvda">NVDA Reddit</span>

  <div class="reddit">
    <div class="reddit-title">r/wallstreetbets &amp; r/stocks — 散户情绪从极度看涨转向中性观望</div>
    <div class="reddit-sum">此前NVDA在WallStreetBets情绪评分一度高达78-88，近期随中国H200芯片出口管制收紧而回落至中性。Jensen Huang警告中国AI基础设施竞争加剧后，部分散户开始观望。但主流观点仍认为Blackwell GPU全球需求旺盛，长期逻辑未变。</div>
    <div class="reddit-link">来源：<a href="https://finance.yahoo.com/news/reddit-traders-cool-nvda-stock-183054273.html" target="_blank">Yahoo Finance Reddit情绪报道</a></div>
  </div>

  <div class="reddit">
    <div class="reddit-title">Reddit年度最佳AI股票：NVDA排名第1，预测2030年市值超苹果+微软总和</div>
    <div class="reddit-sum">多个Reddit投资社区将NVDA列为2026年最值得持有的AI股票。Motley Fool援引Reddit观点预测英伟达2030年市值有望超越Alphabet、Apple、Amazon、Tesla、Meta和Microsoft的总和，认为AI算力需求将在未来十年保持指数级增长。</div>
    <div class="reddit-link">来源：<a href="https://www.fool.com/investing/2026/03/03/prediction-nvidia-nvda-will-be-worth-more-than-alp/" target="_blank">Motley Fool · Mar 3, 2026</a></div>
  </div>
</div>

<!-- SECTION 3: SENTIMENT -->
<div class="sec">
  <div class="sec-title">🎯 市场情绪 &amp; 分析师预测</div>

  <div class="sent-grid">
    <div class="sent-card">
      <div class="ticker" style="color:#79c0ff">PLTR</div>
      <div class="price">$152.67</div>
      <div class="chg-up">▲ 本周 +10.8%</div>
      <div style="margin:8px 0"><span class="badge-buy">综合评级：买入</span></div>
      <div class="target">分析师共识目标价 <span>$192.68</span></div>
      <div class="target">最高目标价 <span style="color:#56d364">$260（Citi）</span></div>
      <div class="target">52周区间 <span>$66.12 – $207.52</span></div>
    </div>
    <div class="sent-card">
      <div class="ticker" style="color:#56d364">NVDA</div>
      <div class="price">$183.34</div>
      <div class="chg-dn">▼ 年初至今承压</div>
      <div style="margin:8px 0"><span class="badge-strong-buy">综合评级：强力买入</span></div>
      <div class="target">分析师共识目标价 <span>$263.29</span></div>
      <div class="target">最高目标价 <span style="color:#56d364">$300（Cantor Fitzgerald）</span></div>
      <div class="target">上行空间 <span style="color:#56d364">~48%</span></div>
    </div>
  </div>

  <div style="margin-top:14px">
    <div style="font-size:13px;color:#8b949e;margin-bottom:8px;font-weight:600">📊 华尔街主流观点</div>

    <div class="opinion"><strong>PLTR · Rosenblatt (Buy, $200)</strong>：美国商业AI业务137%同比增速为公司提供了坚实的基本面支撑，政府合同组合持续扩张，长期增长逻辑清晰。</div>
    <div class="opinion"><strong>PLTR · Citi (Buy, $260)</strong>：认为五角大楼/Anthropic事件是短期噪音，Palantir的AIP平台在商业客户中渗透率快速提升，给予最高目标价$260。</div>
    <div class="opinion"><strong>NVDA · Goldman Sachs &amp; Morgan Stanley (目标价$250)</strong>：Blackwell架构GPU需求持续超出预期，数据中心业务增长可见性高，维持强力买入。</div>
    <div class="opinion"><strong>NVDA · Bank of America &amp; Wedbush (目标价$275)</strong>：Meta $1150亿CapEx和全球超大规模云厂商扩张将支撑英伟达2026-2027年收入增长，看好GTC大会催化效应。</div>
    <div class="opinion"><strong>整体市场判断</strong>：华尔街目前更倾向于NVDA（强力买入，约48%上行空间），PLTR虽基本面强劲但估值偏高（仍有约26%上行空间）。两者均属AI主题核心标的，机构资金在科技股回调中通常首选这两只作为配置标的。</div>
  </div>
</div>

<!-- SECTION 4: CHARTS -->
<div class="sec">
  <div class="sec-title">📊 近30天股价走势图表</div>

  <span class="tag-pltr">PLTR · Palantir — 30天行情</span>
  <div class="chart-wrap">
    <img src="data:image/png;base64,{charts['PLTR']}" alt="PLTR Stock Chart">
  </div>

  <div style="height:18px"></div>

  <span class="tag-nvda">NVDA · 英伟达 — 30天行情</span>
  <div class="chart-wrap">
    <img src="data:image/png;base64,{charts['NVDA']}" alt="NVDA Stock Chart">
  </div>

  <div style="margin-top:12px;font-size:11px;color:#484f58;text-align:center">
    图表说明：蓝/绿线为收盘价，金线为MA5均线，红线为MA20均线；成交量绿色=上涨日，红色=下跌日；资金流向基于每日价格变动×成交量估算。
  </div>
</div>

<div class="ftr">
  <p>本邮件由 Claude AI 自动生成 · {today} 21:00 发送</p>
  <p>数据来源：Yahoo Finance, MarketBeat, TipRanks, NVIDIA Newsroom, Reddit, Motley Fool</p>
  <p style="color:#f85149">⚠️ 本简报仅供参考，不构成投资建议。投资有风险，入市需谨慎。</p>
</div>

</div>
</body>
</html>"""

out = '/sessions/beautiful-peaceful-hamilton/mnt/email/stock_news_preview.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"HTML saved to {out}, size: {len(html)//1024}KB")
