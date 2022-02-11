# 从字典中提取子集

# 股价
prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# 提取一个股价大于200的字典
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

# 提取一个科技业的企业
tech_companies = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
tech_companies2 = [ 'AAPL', 'IBM', 'HPQ', 'MSFT' ]
tech_companies3 = ( 'AAPL', 'IBM', 'HPQ', 'MSFT' )

p2 = {key: value for key, value in prices.items() if key in tech_companies2}
print(p2)

p3 = {key: prices[key] for key in prices.keys() & tech_companies}
print(p3)



