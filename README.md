ファインチューニングプログラム

modelフォルダ、corpusフォルダ、dataフォルダを作成してほしいです
dataフォルダの直下に元になるexcelファイルを置いてください

config.py<br>
ファインチューニングするための設定ファイル

requirements.txt<br>
必要なパッケージのリスト。できない可能性があるからantigravity君に。。。

excel_to_alpaca.py<br>
ExcelファイルをAlpaca形式のJSONLファイルに変換するスクリプト

fine_turning.py<br>
ファインチューニングを行うスクリプト

generate.py<br>
ファインチューニングしたモデルを元にテキスト生成するテストスクリプト
