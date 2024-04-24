text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in text:
    print (i)



meme_dict = {
            "HMM": "Birçok anlamda kullanlıbilir genellikle anladım, öylemiymiş",
            "EDİBLE": "EDİBLE kelimesini sınıfımdakiler dışında kimsenin kullanmadığına eminim ingilizcede anlamı Yenilebilir olsada bizdeki anlamı olabilir, neden olmasın,yapılabilir",
            }
        
        
        
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word in meme_dict:
        print(word, "kelimesinin anlamı =" , meme_dict[word])
else:
    print("Maalesef verdiğiniz kelime listemde yok ;(")
