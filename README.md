# rag-example

夏目漱石の「こころ」について答えてくれる RAG の実装例です。

## 構成

- ドキュメント
  - 夏目漱石「こころ」
- 埋め込みモデル
  - OpenAI text-embedding-3-small
- 回答生成モデル
  - OpenAI gpt-4o-mini
- ベクトルストア
  - インメモリ

## 準備

OpenAI API の API Key を発行し、`.env` に転記します。

```
cp .env.template .env
edit .env
```

## 使い方

```
docker compose up --build
access localhost:7860
```
