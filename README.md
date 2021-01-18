# JapanTrafficAccident
Output: https://nyoshimura.github.io/JapanTrafficAccident/JapanTrafficAccident.html

![image](https://user-images.githubusercontent.com/10651438/104105694-400c2380-52f3-11eb-8e28-69f3d6293ca6.png)

### To Do
* Associate close-points as cluster
* Define risky road from cluster and overlay
* Create ranking of risky road in Japan/area
* Load dangerous area from SNS (e.g. Instagram, Twitter) by using hash-tag (if possible)

### Log
2021/1/10: gps location, pedestrian age, link to google street view are added as pop-up

### Notes
* 出典:警察庁ウェブサイト(https://www.npa.go.jp/rules/index.html)
* データ元: (https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html)

### Index
Helper to copy index name
```
df = pd.read_csv("./honhyo_2019.csv", encoding='cp932')
print(df.columns)
'''
Index(['資料区分', '都道府県コード', '警察署等コード', '本票番号', '事故内容', '死者数', '負傷者数', '路線コード',
       '上下線', '地点コード', '市区町村コード', '発生日時　　年', '発生日時　　月', '発生日時　　日', '発生日時　　時',
       '発生日時　　分', '昼夜', '天候', '地形', '路面状態', '道路形状', '環状交差点の直径', '信号機',
       '一時停止規制　標識（当事者A）', '一時停止規制　表示（当事者A）', '一時停止規制　標識（当事者B）',
       '一時停止規制　表示（当事者B）', '車道幅員', '道路線形', '衝突地点', 'ゾーン規制', '中央分離帯施設等', '歩車道区分',
       '事故類型', '年齢（当事者A）', '年齢（当事者B）', '当事者種別（当事者A）', '当事者種別（当事者B）',
       '用途別（当事者A）', '用途別（当事者B）', '車両形状（当事者A）', '車両形状（当事者B）',
       '速度規制（指定のみ）（当事者A）', '速度規制（指定のみ）（当事者B）', '車両の衝突部位（当事者A）',
       '車両の衝突部位（当事者B）', '車両の損壊程度（当事者A）', '車両の損壊程度（当事者B）', 'エアバッグの装備（当事者A）',
       'エアバッグの装備（当事者B）', 'サイドエアバッグの装備（当事者A）', 'サイドエアバッグの装備（当事者B）',
       '人身損傷程度（当事者A）', '人身損傷程度（当事者B）', '地点　緯度（北緯）', '地点　経度（東経）', '曜日(発生年月日)',
       '祝日(発生年月日)']
'''
```
