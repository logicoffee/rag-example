# 入力データの作成方法

[青空文庫収録ファイルの取り扱い基準](https://www.aozora.gr.jp/guide/kijyunn.html) で推奨される通り、入力データの作り方をまとめておく。

## ダウンロードと解凍

[こころの作品ページ](https://www.aozora.gr.jp/cards/000148/card773.html) から zip ファイルをダウンロード。

## 文字コードの変換

以下のコマンドで文字コードを変換。

```
iconv -f SHIFT_JIS -t UTF-8 kokoro.txt > kokoro_utf8.txt
```

## 記載事項等の削除

記号の判例や記載事項を削除。なお、記載事項は `kisai.txt` に別途ファイルを切り出している。

## ルビ等の削除

`data/process.py` を実行することでルビ等を削除。
