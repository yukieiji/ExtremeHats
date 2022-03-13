# ExtremeHat
Extreme RolesのアドオンであるExtreme Skinsのハットデータ管理用リポジトリ<br>
Extreme Skins以外のMOD(Extreme Skinsのフォーク等も含めて)でこのリポジトリのデータを使用する場合、このリポジトリ自体のライセンス(使用規約)を読み把握した上で各ハットのライセンス(使用規約、LICENCE.md)に従って下さい<br>
このリポジトリのライセンスは[こちら](https://github.com/yukieiji/ExtremeHats/blob/main/LICENSE.md)

## 新しいスキンの作り方
1. ExtremeHatの下に新しいフォルダを作る(ローマ字推奨、日本語等は使用しない)
2. 以下の名前の画像ファイルを作る、front.png以外は必要に応じて追加して下さい
  - front.png : 正面右向き前のレイヤーの画像ファイル
  - front_flip.png : 正面左向き前のレイヤーの画像ファイル
  - back.png : 正面右向き後ろのレイヤーの画像ファイル
  - back.png : 正面左向き後ろのレイヤーの画像ファイル
  - climb.png : 梯子使用中の画像ファイル(反転は必要ない)
3. 以下を記入したinfo.jsonを作る(#以降は消して下さい)<br>
{<br>
    "Author": , #製作者名、ローマ字スネークケースで記入、例"yukiEiji"<br>
    "Name": , #スキンの名、ローマ字スネークケースで記入、例"overLoading"<br>
    "FrontFlip": , #True(ある)かFalse(ない)か<br>
    "Back": , #True(ある)かFalse(ない)か<br>
    "BackFlip": , #True(ある)かFalse(ない)か<br>
    "Climb": , #True(ある)かFalse(ない)か<br>
    "Bound": , #True(ある)かFalse(ない)か<br>
    "Shader": , #これがTrue(オン)の時、一部の色が体の色とシンクロします。シンクロしてほしくない場合はFalse(オフ)に<br>
    "comitHash": "" # 記載しなくて大丈夫<br>
}
4. 追加後、ゲームを再起動するとスキンが追加されているはずです

- エラーが出た場合
  - AuthorとNameは""で囲って下さい
  - AmongUs.exeのあるフォルダのBepInExの下にLogOutput.txtがあります。正しくロードできているとそのログの途中に以下の様な出力が出ているはずです
    - [Info   :Extreme Skins] Skin Loaded:（スキン名）, from:（ロードしているフォルダ）

#### 身内内専用のスキンを追加して遊ぶ場合は[Impostor](https://github.com/Impostor/Impostor)等のカスタムサーバーの使用をおすすめします
