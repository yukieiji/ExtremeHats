# TOHtoEXH Converter

TheOtherHat形式で保存されているデータを一括でExtremeHatのデータ形式に変更するコンバーターです<br>
複数のデータフォルダも一括で変換してくれます

## 使い方
1. Pythonをインストールします(Anaconda、WinPythonなんでも可)
2. このリポジトリ全体をダウンロードして展開します
   1. https://github.com/yukieiji/ExtremeHats　を開き
   2. 緑色の「Code」をクリック
   3. 「Download ZIP」をクリックでダウンロードできます
3. 上で展開したフォルダからこのフォルダ(converterフォルダ)を開きます
4. 「repo」フォルダの中に変換したいTheOtherHat形式で保存されているデータを一括で入れて下さい(ない場合は作って下さい)
   - 以下のようなフォルダ形式になっていればOKです
     - converter
      - repo
        - (データフォルダ1)
           - hats
           - CustomHats.json
         - (データフォルダ2)
           - hats
           - CustomHats.json
5. そこでコマンドプロンプトを開きます
6. 「pip install -r requirements.txt」と入力してエンター
7. 「python convert.py」と入力してエンター
8. 変換完了
   - hatフォルダやHatTransData.xlsxに自動変換されたデータが追加、格納されてます