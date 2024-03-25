# Python環境構築 on Docker
## 概要
Docker での環境構築を体験するための脱初心者チュートリアルを提供する目的でこのリポジトリを作成しました。
このリポジトリでは Python の仮想環境構築をターゲットにしていますが、 Python に関心がない人でも十分学びのある内容になっています。
## ファイル構成
- /app
  - 　チュートリアルで使用する Python スクリプトがまとまったフォルダ。
- Dockerfile-example
  - Dockrfile のテンプレート。このファイルをコピーして問題に取り組んでください。

# チュートリアル内容
## 問題
### ( 問題1 ) main.pyをcontainer内で実行する
- ゴール
  - [ ] コンテナを実行すると main.py が実行され、data フォルダ (generated_data.csv, main01.png) が作成される & data folder has created!! が出力される。

### ( 問題2 ) main.pyを実行した後にhello.pyも実行できるようにする
- ゴール
  - [ ] コンテナを実行すると main.py が実行され、data フォルダ (generated_data.csv, main01.png) が作成される
  - [ ] コンテナを実行すると hello.py が実行され、Hello, world!! が出力される

### 補足
- コンテナ内でコマンドを打ちながら、うまくいったコマンドを Dockerfile に記載する形式で取り組むと手を動かしやすい
