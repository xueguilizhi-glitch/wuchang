# 股票量化交易应用程序

一个功能完整的量化交易系统，包含数据获取、策略开发、回测、风险管理和实盘交易功能。

## 🎯 核心功能

### 1. 数据模块 (`data/`)
- ✅ 多源数据获取（Yahoo Finance、AKShare、Wind API等）
- ✅ 数据清洗与预处理
- ✅ 实时行情获取
- ✅ 数据缓存与增量更新
- ✅ K线合成（多周期）

### 2. 策略模块 (`strategy/`)
- ✅ 双均线策略
- ✅ 均值回归策略
- ✅ 动量策略
- ✅ MACD策略
- ✅ RSI策略
- ✅ 机器学习策略（随机森林、XGBoost、LightGBM）
- ✅ 深度学习策略（LSTM、Transformer）
- ✅ 多因子模型
- ✅ 配对交易
- ✅ 期权策略

### 3. 回测模块 (`backtest/`)
- ✅ 高效回测引擎
- ✅ 多种成本模型
- ✅ 滑点模拟
- ✅ 风险指标计算（Sharpe、Sortino、Calmar等）
- ✅ 结果可视化
- ✅ 参数优化
- ✅ 蒙特卡洛模拟

### 4. 风险管理 (`risk/`)
- ✅ 仓位管理（固定、百分比、凯利公式）
- ✅ 动态止损止盈
- ✅ 风险限制与告警
- ✅ 对冲策略
- ✅ 相关性分析

### 5. 实盘交易 (`broker/`)
- ✅ 多券商支持（富途、腾讯自选股、币安等）
- ✅ 订单管理
- ✅ 实时行情推送
- ✅ 账户查询
- ✅ 仓位管理

### 6. Web服务 (`app/`)
- ✅ REST API
- ✅ 实时Dashboard
- ✅ 策略管理UI
- ✅ 回测分析UI
- ✅ 风险监控UI

### 7. 数据库 (`database/`)
- ✅ 历史数据持久化
- ✅ 交易记录管理
- ✅ 策略参数保存

## 📁 项目结构

```
stock-quant-trading/
├── data/                      # 数据模块
│   ├── fetcher.py            # 数据获取
│   ├── cleaner.py            # 数据清洗
│   ├── cache.py              # 数据缓存
│   ├── realtime.py           # 实时行情
│   └── kline.py              # K线合成
├── strategy/                  # 策略模块
│   ├── base.py               # 策略基类
│   ├── signals.py            # 信号生成
│   ├── indicators.py         # 技术指标
│   ├── classic/              # 经典策略
│   ├── ml/                    # 机器学习
│   ├── dl/                    # 深度学习
│   ├── multifactor/           # 多因子
│   └── options/               # 期权策略
├── backtest/                  # 回测模块
│   ├── engine.py             # 回测引擎
│   ├── metrics.py            # 性能指标
│   ├── visualizer.py         # 可视化
│   ├── optimizer.py          # 参数优化
│   ├── monte_carlo.py        # 蒙特卡洛
│   └── analyzer.py           # 深度分析
├── risk/                      # 风险管理
│   ├── position.py           # 仓位管理
│   ├── limits.py             # 风险限制
│   ├── hedging.py            # 对冲
│   ├── correlation.py        # 相关性
│   └── alerts.py             # 告警
├── broker/                    # 实盘交易
│   ├── base.py               # 基类
│   ├── futu.py               # 富途
│   ├── tencent.py            # 腾讯
│   ├── binance.py            # 币安
│   ├── order.py              # 订单
│   └── account.py            # 账户
├── app/                       # Web服务
│   ├── main.py               # Flask应用
│   ├── api/                  # REST API
│   └── static/               # 前端资源
├── database/                  # 数据库
│   ├── models.py             # 数据模型
│   └── connection.py         # 连接
├── utils/                     # 工具函数
│   ├── logger.py             # 日志
│   ├── config.py             # 配置
│   ├── time_utils.py         # 时间
│   └── math_utils.py         # 数学
├── tests/                     # 单元测试
├── notebooks/                 # Jupyter示例
├── docker-compose.yml        # Docker配置
├── main.py                    # 主程序
└── requirements.txt           # 依赖
```

## 🚀 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行示例
```bash
python main.py
```

### 启动Web服务
```bash
cd app
python main.py
```

### 使用Jupyter notebook
```bash
jupyter notebook notebooks/quick_start.ipynb
```

## 📊 性能指标

支持的回测指标：
- Sharpe Ratio（夏普比率）
- Sortino Ratio（索提诺比率）
- Calmar Ratio（卡玛比率）
- Maximum Drawdown（最大回撤）
- Win Rate（胜率）
- Profit Factor（利润因子）
- Information Ratio（信息比率）
- Omega Ratio（欧米茄比率）
- Value at Risk（风险价值）
- Conditional Value at Risk（条件风险价值）

## 🔧 配置

见 `config/settings.py` 和 `.env.example`。

## 📝 许可证

MIT License

## 👨‍💻 贡献

欢迎提交 Issue 和 Pull Request！

## 📧 联系方式

如有问题，请提交 GitHub Issue。
