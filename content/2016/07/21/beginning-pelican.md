Title: Pelicanを使ってみることにする
Date: 2016-07-21 22:43
Category: tech
Tags: pelican
Slug: beginning-pelican
Author: aojs53


# インストール

pelicanのインストールは
http://blog.sotm.jp/2014/01/04/Pelican-Markdown-GithubPages-install-guide/
を参照。


# github pagesを復習

なんかまだよくわかっていなかったので復習。

* githubで静的なページを公開するためのサービスがgithub pages。
* markdownなどをpushして、自動でhtmlを生成することも可能。あるいはローカルでjekyllやpelicanをつかって静的ページを生成してからpushする。
* github pagesを公開する方法はふたつ。ユーザ/組織ページと、プロジェクトページ。
* ユーザ/組織ページ -- リポジトリの名前を、ユーザ名.github.io としてファイルをコミットすると、このリポジトリのmasterブランチの内容がページとして公開される。
* プロジェクトページ -- ふつうのリポジトリに内容を空なgh-pagesブランチをつくる(git checkout --orphan gh-pages)。でこのブランチにコミットした内容が公開される。

今回自分は、ユーザページを公開している。つまりaojs53.github.ioというリポジトリをつくって、そのリポジトリのmasterブランチにコンテンツをつくっていくかたち。



# リポジトリをつくるところからの手順

* mkdir aojs53.github.io
* pelican-quickstart で新規プロジェクト作成 (github pagesをつかう & user pageか?にyes)
* git add .
* .gitignoreの作成とgit add
* git commit
* git branch -m master source
* git branch master
* git remote add https://github.com/aojs53/aojs53.github.io.git
* コンテンツをかく
* make html
* make github

でよくなった。



# pelicanでテーマを変更する

* pelicanconf.py
  * THEMEに、相対パスでテーマディレクトリを指定すると、そのテーマを利用する。
    http://pelicanthemes.com/ にサンプル多数。ここからたどって、pelican-themeディレクトリにgit cloneしてくる。




# わからないことを調べる

## ghp-importってなんだ?

https://github.com/davisp/ghp-import
のREADME.mdをみるとわかった。
プロジェクトのgithub pagesはgh-pagesブランチにドキュメントをおかないといけないけど、いちいち切り替えたりするの面倒。
だから、masterとかコードと同じブランチでドキュメントを書いて、公開目的でgh-pagesブランチにコピーだけすればいいじゃん、と。
そのためのスクリプトがghp-import。

## git pushはなにをしている?

ghp-importコマンドでoutputの内容をgh-pagesブランチにコピーしてある状態で、git push ...を実行すると
ローカルリポジトリのgh-pagesブランチの内容をaojs53.github.ioのmasterブランチにpushする。
つまり、ユーザページが更新される。
https://github.com/davisp/ghp-import
をみると、pelican-quickstartで生成されたMakefileのtargetに、githubというのがあるとのこと。
ただしデフォルトだと、プロジェクトページをpublishする内容になっている。
ユーザページ向けは、なおして使ってね、というかんじみたい。

## ブランチの管理をどうしたらよいかわからない

上記の例だと、ローカルにあるリポジトリとgithub上のリポジトリは別もの。
できれば同じリポジトリでソースと公開すべきhtmlの両方を管理したいところ。
プロジェクトページであれば、masterでソースを管理して、gh-pagesにコピーというので
よいのだろうけど、ユーザページを使いたい。

http://blog.sotm.jp/2014/01/04/Pelican-Markdown-GithubPages-install-guide/
をみたら、以下のようにすればよい、とかいてあった。

```
$ git init .
$ git branch -m master source      # masterブランチをsourceという名前に変更
$ git remote add origin <自分のGitHubリポジトリでコピーしてきたなにか>
```

でも結局、pelicanが生成してくれるMakefileでmake githubとすれば同じことをしてくれたのでそれをつかう。


## git remoteってなんだ?

gitではローカルの自分のリポジトリと、リモートリポジトリを強調させながら開発を
すすめていくようなつくりになっている。

ふつうは、git cloneしてくると、clone元が”origin”となる。
以下、今の自分のリポジトリは、githubからcloneしてきているだけ。

```
$ git remote
origin
git remote -v
origin    https://github.com/aojs53/aojs53.github.io.git (fetch)
origin    https://github.com/aojs53/aojs53.github.io.git (push)
```

共同開発者のremoteリポジトリを複数登録して、pushしたりpullしたりしあう
ことが可能になる。git remote add <name> <url>で追加できる。

git fecth remote-name -- ローカルリポジトリに更新をとりこみ
git pull remote-name -- fetch & mergeを自動でやる
git push orign master -- ローカルのmasterをoriginにpushする




## pelican-themeは自分のリポジトリにいれたくない

git submoduleをつかえばいいようだ。
http://qiita.com/sotarok/items/0d525e568a6088f6f6bb

```
$ git submodule add https://github.com/jody-frankowski/blue-penguin.git
```

でできた。




