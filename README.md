# ExtremeHat
Extreme RolesのアドオンであるExtreme Skinsのハットデータ管理用リポジトリ<br>
Extreme Skins以外のMOD(Extreme Skinsのフォーク等も含めて)でこのリポジトリのデータを使用する場合、このリポジトリ自体のライセンス(使用規約)を読み把握した上で各ハットのライセンス(使用規約、LICENCE.md)に従って下さい<br>
このリポジトリのライセンスは[こちら](https://github.com/yukieiji/ExtremeHats/blob/main/LICENSE.md)

## 新しいスキンの作り方
1. ExtremeHatの下に新しいフォルダを作る(ローマ字推奨、日本語等は使用しない)
2. 以下の名前の画像ファイルを作る、front.png以外は必要に応じて追加して下さい
   - front.png : 正面右向き前のレイヤーの画像ファイル(ピクセルサイズ：300×375)
   - front_flip.png : 正面左向き前のレイヤーの画像ファイル(ピクセルサイズ：300×375)
   - back.png : 正面右向き後ろのレイヤーの画像ファイル(ピクセルサイズ：300×375)
   - back.png : 正面左向き後ろのレイヤーの画像ファイル(ピクセルサイズ：300×375)
   - climb.png : 梯子使用中の画像ファイル(反転は必要ない)(ピクセルサイズ：300×375)
3. 以下を記入したinfo.jsonを作る(「,」の前に記載、#以降全ては消して下さい)
```
{
    "Author": , #製作者名、ローマ字スネークケースで記入、例"yukiEiji"
    "Name": , #スキンの名、ローマ字スネークケースで記入、例"overLoading"
    "FrontFlip": , #true(ある)かfalse(ない)か
    "Back": , #true(ある)かfalse(ない)か
    "BackFlip": , #true(ある)かfalse(ない)か
    "Climb": , #true(ある)かfalse(ない)か
    "Bound": , #true(ある)かfalse(ない)か
    "Shader": , #これがtrue(オン)の時、一部の色が体の色とシンクロします。シンクロしてほしくない場合はfalse(オフ)に
    "comitHash": "" # 記載しなくて大丈夫
}
```
4. 追加後、ゲームを再起動するとスキンが追加されているはずです
- エラーが出た場合
  - AuthorとNameは""で囲って下さい
  - AmongUs.exeのあるフォルダのBepInExの下にLogOutput.txtがあります。正しくロードできているとそのログの途中に以下の様な出力が出ているはずです
    - ```[Info   :Extreme Skins] Skin Loaded:（スキン名）, from:（ロードしているフォルダ）```

## 他のMODのハットをExtremeHats用に変換したい
- [TOHtoEXH Converter](https://github.com/yukieiji/ExtremeHats/tree/main/converter)を使用するとある程度自動変換してくれます


#### 身内内専用のスキンを追加して遊ぶ場合は[Impostor](https://github.com/Impostor/Impostor)等のカスタムサーバーの使用をおすすめします

## ハットを提供していただいた方々
- [猫野和錆](https://twitter.com/neko_wasa)様
- [ピロ彦](https://twitter.com/pirohiko)様
- [ひなにい](https://twitter.com/__xxhina)様
- [みやち](https://twitter.com/mii_yachi)様
- [YJ\*白桜](https://twitter.com/_Sakura_White_)様(ExtremeHatsで使えるようにデータ構造を変更しています(ハットデータがGNU General Public License v3.0ライセンスのため詳細を記載))
- アンハッピーセット様
- アドミン様
- おやきもん様
- ラプ様
- 竹饅様
- クロドル様
- Nyayuta様
