# TradeX

Trading system for cryptocurrency exchange.

## Install

### Local

```bash
pip 
```

## TODO

- [ ] 使用 aiohttp 实现 https://dev.binance.vision/t/how-to-implement-otoco-tp-sl-orders-using-api/1622/2?u=jay_chung 方法，SL一个，TP符合fib
- [x] 根据杠杆，计算保证金
- [x] 计算fib
- [ ] 计算止盈情况
- [ ] 获取最新价格
- [ ] 链接交易所下单
- [ ] 部署到 streamlit 实现手动下单，全仓、最大杠杆、有止损
- [x] 计算斐波那契数列，自动设定止盈，15；25；45；15
- [ ] 机构订单买区
- [ ] 上移止损
  - [ ] 当实现了 1.618 后，需要调整止损到 0.618
  - [ ] 当实现了 1.382 后，需要调整止损到 0.382
  - [ ] 当实现了 2 后，需要调整止损到 1
- [ ] 获取交易所价格数据
- [ ] 计算各个时间段的 vagas 通道，确定入场点
  - [ ] 其中包括
    - min: 5, 15, 30
    - hour: 1, 2, 3, 4
    - day: 1, 3
    - week: 1
    - month: 1
  - [ ] 如果 vagas 通道断了，就要找合适机会离场
- 趋势线计算
- 趋势线、vagas通道、fib 矛盾的时候，可以选择不做，或者以通道为主去做