#1
import re
text = str(input('Ну ладно, на это мне фантазии не хватило... Но сюды вы можете вписать любой текст -> '))
text1 = r"[A-Z]"
text2 = re.findall(text1, text)
for x in text2:
    print(x, end="")
    
 

#2
symbols = ['!','@','#','$','%',]
text = ('напишите@что!нибудь$')
text = text.replace('@','').replace('!','').replace('#','').replace('$','').replace('%','')
print(text)



#3
mylist = ['hello, how, are, u'] 
user_input= str(input('Скажи ка мне милок: А ты сейчас в поисках какой буквы? ->')) 
result = [word for word in mylist if word.lower().startswith(user_input)] 
print(len(result)) 
print(result) 
#P.S Тут если не ошибаюсь можно ещё сделать так, что бы вы сам список создавали. Но лень всему голова)

#4
user_input = "Что то на своё чсвшное усмотрение (не и всех оно чсвшное)" 
# Можно и просто через input сделать (user_input = str или же без str (input(':'))), но я показал именно так 
#т.к я считаю, что это задание описано не правильно, потому что там не сказано по какому принципу слова должно разделяться 
print(user_input.split())


#5
