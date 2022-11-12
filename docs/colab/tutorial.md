# Google Colaboratory

## Colaboratoryとは

Colaboratory（略称: Colab）ではブラウザからPythonを記述し実行できるほか、Markdown形式によるテキストを記述し、表示ができるサービスです。コードと実行結果およびテキストはノートブック（.ipynb）という形式に保存され、容易に共有できます。クラウド上に環境が用意されているため、ユーザは実行環境を用意することなく、すぐにPythonを実行できます。また、あらかじめデータ分析に必要なライブラリがインストールされており、環境構築を手間がかからないのも利点のひとつです。

## Colaboratoryの使い方

早速、Colaboratoryを使ってみましょう。ブラウザから次のリンクにアクセスします。

[https://colab.research.google.com/](https://colab.research.google.com/)

Googleアカウントによるログインを行っていない場合には「ログイン」ボタンよりログインし（ {numref}`colab_not_login` ①）、「ノートブックを新規作成」を選択します（ {numref}`colab_recent` ②）。

```{figure} ./images/colab_not_login.png
:name: colab_not_login

未ログイン時の画面
```

```{figure} ./images/colab_recent.png
:name: colab_recent

Colaboratoryの初期画面
```

ノートブックが作成され、このノートブックにコードやテキストを記述できます（ {numref}`colab_new_notebook` ）。

```{figure} ./images/colab_new_notebook.png
:name: colab_new_notebook

新規ノートブック
```

Colaboratoryの設定を変更します。「ツール」から「設定」を選択します（ {numref}`colab_config` ）。

```{figure} ./images/colab_config.png
:name: colab_config

設定
```

インデント幅を変更します。「エディタ」から「インテント幅（スペース）」の値を4に変更して保存します（ {numref}`colab_editor` ）。

```{figure} ./images/colab_editor.png
:name: colab_editor

エディタの設定
```

作成されたノートブックは名前の変更ができます。ノートブック名を変更するには {numref}`colab_new_notebook` ③の「Untitled#.ipynb」（#は数値）を任意の名前に変更します。

{numref}`colab_new_notebook` ④はコードセルと呼ばれ、Pythonのコードが実行できます。コードセルに次のコードを記述し、実行してみましょう。 コードの実行は {numref}`colab_new_notebook` ⑤のボタンをクリックするか、「Shift+Enter」または「Ctrl+Enter」を入力します。

```python
1 + 2
```

コードセルを実行すると {numref}`colab_run_code` のようにノートブックにコードと実行結果が表示されます。このようにノートブックにコードと実行結果を保存することで、あとで読み返したり、第三者に共有するのに便利です。

コードセルを追加するには {numref}`colab_new_notebook` ⑥をクリックするかセルの上下にカーソルを移動し、「＋ コード」をクリックします（ {numref}`colab_cell` ）。

```{figure} ./images/colab_run_code.png
:name: colab_run_code

Pythonコードを実行
```

```{figure} ./images/colab_cell.png
:name: colab_cell

セルの追加
```

次にテキストセルにテキストを記述します。テキストセルを作成するには {numref}`colab_new_notebook` ⑦をクリックするかセルの上下にカーソルを移動し、「＋ テキスト」をクリックします（ {numref}`colab_cell` ）。
テキストセルに次のように記述し、実行すると数式が表示されます 。

```
円周$c$は円周率を${\pi}$、半径を$r$とした場合に次の式で表される

$c = 2{\pi}r$
```

{numref}`colab_text` のようにテキストセルに数式を記述し、この数式をPythonコードに実装することで、数式をプログラムに実装する方法を記録に残しながら学べるようになります。

```{figure} ./images/colab_text.png
:name: colab_text

テキストセルに数式を記述
```