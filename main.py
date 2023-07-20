meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
     
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print("O KELİMENİN ANLAMINI BU:", meme_dict[word])
else:
    print("BU SÖZLÜKTE ARADIĞINIZ KELİME YOK")
