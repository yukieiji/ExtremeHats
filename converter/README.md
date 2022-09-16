# TOHtoEXH Converter

TheOtherHat形式で保存されているデータを一括でExtremeHatのデータ形式に変更するコンバーターです<br>
複数のデータフォルダも一括で変換してくれます

## 使い方
1. Pythonをインストールします(Anaconda、WinPythonなんでも可、型アノテーションを使っているのでPython3.7以降が必要です)
2. このリポジトリ全体をダウンロードして展開します
   1. まずは[リポジトリ](https://github.com/yukieiji/ExtremeHats)を開き
   2. 緑色の「Code」をクリック
   3. 「Download ZIP」をクリックでダウンロードできます
3. ダウンロードしたZipを展開します
4. 上で展開したフォルダからこのフォルダ(converterフォルダ)を開きます
5. 「repo」フォルダ(ない場合は作って下さい)の中に変換したいTheOtherHat形式で保存されているデータを一括で入れて下さい
   - 以下のようなフォルダ形式になっていればOKです
     - converter
       - repo
         - (データフォルダ1)
            - hats
              - ハット画像1
              - ハット画像2
              - ハット画像3....
            - CustomHats.json
          - (データフォルダ2)
            - hat
              - ハット画像1
              - ハット画像2
              - ハット画像3....
            - CustomHats.json
6. converterフォルダでコマンドプロンプトを開きます(もしくはコマンドプロントを開き、converterフォルダまで移動します)
7. 「pip install -r requirements.txt」と入力してエンター
8. 「python convert.py」と入力してエンター
9. 変換完了
   - hatフォルダやHatTransData.xlsxに自動変換されたデータが追加、格納されてます
   - hatフォルダの中身をそのままAmong UsのExtremeHatフォルダにコピーすると正しく動作します
