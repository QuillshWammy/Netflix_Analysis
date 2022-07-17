# 動画配信サブスクについて

## Data

- [情報通信統計データベース](https://www.soumu.go.jp/johotsusintokei/field/index.html)
- [Netflix Top10](https://top10.netflix.com/)
- [Netflix Investors](https://ir.netflix.net/ir-overview/profile/default.aspx)
- [Wiki](https://en.wikipedia.org/wiki/Netflix)

## Question

- 一週間ごとの視聴時間の時系列データはどんな分布に従うのか
  - 相関のある時系列データはあるか(株価など)
  - 周期性、トレンドはあるのか
  - Netflixの会員数が減少した影響を受けているか

- Top10になる作品同士に相関のある作品があるのか
  - 新作の以前のシーズン
  - 同じ俳優、監督の作品

- Netflixにおいて映画とTVシリーズの視聴時間に統計的な有意な差があるのか
  - 一般的に作品としての長さはTVシリーズが長い

- 言語が英語でない作品は視聴時間または株価に寄与しているか
  - イカゲームなど話題の作品が多い

## Model

- 週間視聴時間についての回帰モデル
  - Netflixオリジナルシリーズが多いほど週間視聴時間は多いのか

- 作品の連続top10入り回数についての回帰モデル
  - Netflixオリジナルシリーズのほうがtop10入り回数が多いのか

- 今週のTop10作品が次週も入るかどうかの予測モデル
