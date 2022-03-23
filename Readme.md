# ブクログ本棚に本を登録するスクリプト

ブクログ（ https://booklog.jp/ )の本棚に本を登録するPythonスクリプトです。<br>

ちなみにISBNやタイトルの一覧をまとめて登録したい場合は、以下のブクログサービスから登録ができます。<br>
https://booklog.jp/input <br>

Amazonなどの購入履歴や、他の情報を取得しながらブクログに登録したい場合の部品としてご利用ください。

## 1.セットアップ（Macbookを想定）

### pyenvのインストール

Python環境がない場合はPyenvのインストールをお薦めします。
brewが使える場合は下のコマンドを利用してもできます。

```shell
git clone git://github.com/yyuu/pyenv.git ~/.pyenv
brew install pyenv
```

### bash_profileの編集

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'if command -v pyenv 1>/dev/null 2>&1; then' >> ~/.bash_profile
echo '  eval "$(pyenv init --path)"' >> ~/.bash_profile
echo 'fi' >> ~/.bash_profile

source ~/.bash_profile
```

### Python 3.9のインストール

pyenvでpythonをインストール
現在ある3.9の中の最新版を入れてみました。

```shell
pyenv install 3.9.10
pyenv global 3.9.10
pyenv rehash
```

### GitHubからプログラムをダウンロード

```shell
cd （ソースコードを格納したい任意の場所）
git clone https://github.com/abenben/register_booklog.git
```

### Pythonパッケージのインストール

```shell
cd register_booklog
pip3 install -r requirements.txt
```

## 2.環境設定

ご自身の

```shell
export BOOKLOG_ID=(ブックログのID)
export BOOKLOG_PASSWORD=(ブックログのパスワード)
```

## 3.使い方

### 3.1.本のリスト（テキストファイル）を作成する

本のISBNコードで作成したい場合、1行づつコードを記入してください。
ISBN-10コード、ISBN-13コード、B09NKKXF27の3種類に対応しています。

[input/books1.txt]
```text
978-4140817902
B01NADS36I
```

本のタイトル名で作成したい場合、1行づつタイトルを記入してください。
タイトルの場合は、ブクログが検索を間違えてしまう場合があるのでご注意下さい。
kindle版などの区別ができないので確実に登録したい場合はISBNやASINコードをお薦めします。

[input/books2.txt]
```text 
ビッグ・ピボット―なぜ巨大グローバル企業が〈大転換〉するのか
コンテナ物語―世界を変えたのは「箱」の発明だった
```

### 3.2.スクリプトを実行する

--booklistパラメータには、上記で作成した本のリストのファイル名を指定してください。

```shell
python3 register_booklog.py --booklist=input/books1.txt
```

# License
The source code is licensed MIT.
