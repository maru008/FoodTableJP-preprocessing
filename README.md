# FoodTableJP-preprocessing
日本食品標準成分表の食材名を前処理するリポジトリです．
[日本食品標準成分表（八訂）増補2023年](https://www.mext.go.jp/a_menu/syokuhinseibun/mext_00001.html) に対応しています．
今の食品成分表の食材の表記は分類の情報も混ざっているので，分析等では非常に使いずらいです．
本リポジトリではそれを処理します．

## 処理方法
リポジトリルートファイルにdata/inputファイルを作りその直下に公式サイトから得られるエクセルファイルを保存してください．
設置が終わると全体のディレクトリ構造は以下のようになります．
```
.
├── LICENSE
├── README.md
├── data
│   └── input
│       ├── mtx_01
│       │   └── 20230428-mxt_kagsei-mext_00001_012.xlsx
│       ├── mtx_02
│       │   ├── 20230428-mxt_kagsei-mext_00001_022.xlsx
│       │   ├── 20230428-mxt_kagsei-mext_00001_023.xlsx
│       │   ├── 20230428-mxt_kagsei-mext_00001_024.xlsx
│       │   └── 20230428-mxt_kagsei-mext_00001_025.xlsx
│       ├── mtx_03
│       │   ├── 20230428-mxt_kagsei-mext_00001_032.xlsx
│       │   ├── 20230428-mxt_kagsei-mext_00001_033.xlsx
│       │   └── 20230428-mxt_kagsei-mext_00001_034.xlsx
│       └── mtx_04
│           ├── 20230428-mxt_kagsei-mext_00001_042.xlsx
│           ├── 20230428-mxt_kagsei-mext_00001_043.xlsx
│           └── 20230428-mxt_kagsei-mext_00001_044.xlsx
├── requirements.txt
└── src
    └── preprocessing.py
```

その後，以下のコマンドを実行することでdata/outputファイルに保存されます．(Python 3.10.10)

```
python src/preprocessing.py
```

正しく実行できればdata/outputに以下のファイル群が作成できます．

---
### 備考
プログラムの修正等は issue にお願いします．