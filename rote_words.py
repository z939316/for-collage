import random
import time

a=['admirable', 'admiration', 'admire', 'agreeable', 'amaze', 'amuse', 'annoy', 'anxiety', 'anxious', 'appeal', 'appreciate', 'appreciation', 'approval', 'ashamed', 'attitube', 'attract', 'attraction', 'attractive', 'awful', 'behave', 'blame', 'blush', 'boast', 'bore', 'cheer', 'cheerful', 'cherish', 'comfort', 'complaint', 'complex', 'confess', 'confuse', 'confusion', 'conscience', 'consequence', 'content', 'curiosity', 'curse', 'damn', 'dare', 'delight', 'delightful', 'depress', 'depression', 'desirable', 'desperate', 'determination', 'dignity', 'disappoint', 'disgust', 'dislike', 'dread', 'eager', 'embarrass', 'emotional', 'enjoyable', 'envious', 'envy', 'exaggerate', 'exhaust' , 'expectation', 'expression', 'expressive', 'fantasy', 'fond', 'fragrance', 'fragrant', 'frustrate', 'frustration', 'furious', 'giggle', 'glory', 'grace', 'grateful', 'gratitube', 'grief', 'grieve', 'grin', 'guilty', 'harsh', 'hatred', 'hesitation', 'hopeful', 'horrible', 'horrify', 'horror', 'hug', 'identify', 'impress', 'impression', 'impressive', 'inspiration', 'inspire', 'instinct', 'insult', 'jealous', 'jealousy', 'joyful', 'laughter', 'leisurely', 'lousy', 'mercy', 'merry', 'mischief', 'mislead', 'misunderstand', 'mood', 'neglect', 'nervous', 'offend', 'offense', 'offensive', 'panic', 'passion', 'pessimistic', 'pity', 'rage', 'regret', 'relieve', 'reluctant', 'satisfaction', 'scary', 'shame', 'shameful']
b=['令人欽佩的', '讚嘆(n.)', '欽佩(v.)', '令人愉悅的', '使吃驚', '使快樂', '使困擾', '焦慮(n.)', '焦慮的', '懇求;吸引', '感激', '鑑賞(n.)', '許可(v.)', '羞愧的', '態度', '吸引', '吸引力', '有吸引力的', '糟糕的', '表現(v.)', '責怪', '臉紅(v.)', '自誇', '使厭煩', '喝采(v.)', '愉快的', '珍惜', '安慰', '抱怨(n.)', '複雜的;情緒', '承認', '使困擾', '困惑(n.)', '良心', '影響', '滿足的', '好奇心', '詛咒(n.', '懲罰(下地獄', '膽敢', '使喜悅;欣喜', '愉快的', '使沮喪', '憂鬱', '合意的', '非常嚴重的', '決心', '尊嚴', '令人失望的', '使厭惡;厭惡', '不喜歡', '恐懼(n.);害怕(v.)', '熱切的', '使難堪', '情緒化的', '愉快的', '羨慕的', '嫉妒', '誇張(v.)', '使筋疲力盡', '預期(n.)', '表情', '表情生動的', '幻想(n.)', '喜歡的', '芳香', '芬芳的', '使挫折', '挫折(n.)', '憤怒的', '咯咯地笑(n.v.)', '光榮', '優雅(n.v.)', '感激的', '感激之情', '悲傷(n.)', '悲傷(v.)', '露齒地笑(v.n.)', '有罪的', '刺耳的', '仇恨', '猶豫(n.)', '抱有希望的', '可怕的', '驚嚇(v.)', '恐怖(n.)', '擁抱', '認出', '使印象深刻', '印象', '令人印象深刻的', '靈感', '鼓舞', '直覺', '侮辱(n.v.)', '忌妒的', '忌妒', '喜悅的', '笑(聲)', '悠閒的(a.)', '糟糕的', '仁慈', '歡樂的', '胡鬧', '誤導', '誤解', '心情', '疏忽', '緊張的', '激怒(v.)', '違規(n.)', '討厭的', '恐慌(n.a.v.)', '激情(n.)', '悲觀的', '憐憫(n.)', '盛怒(n.v.)', '後悔(n.v.)', '減輕(v.)', '不情願的', '滿足', '可怕的', '羞愧', '可恥的']
s=60#頭
q=len(a)-1


l=int(input("抽背字義請輸入0\n抽背拼寫請輸入1\n請輸入:"))
if l == 0:
    d=[]
    e=[]
    for i in range(q+1-s):
        c=random.randint(s,q-i)
        print(str(i+1)+". "+a[c])
        f=input()
        print(b[c])
        g=input()
        if g!='' and g!=' ':
            d.append(a[c])
            e.append(b[c])
        
        a.pop(c)
        b.pop(c)
    if len(d) != 0:
        for i in range(len(d)):
            print(d[i]+":"+e[i])
        b=input("input any key to continue")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while len(d)!=0 :
        for i in range(len(d)):
            c=random.randint(0,len(d)-1)
            print(str(i+1)+". "+d[c])
            f=input()
            print(e[c])
            g=input()
            if g=='' or g==' ':
                d.pop(c)
                e.pop(c)
        if len(d) != 0:
            for i in range(len(d)):
                print(d[i]+":"+e[i])  
            b=input("input any key to continue")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("背完囉~")
if l==1:
    d=[]
    e=[]
    for i in range(q+1-s):
        c=random.randint(s,q-i)
        print(str(i+1)+". "+b[c])
        f=input("英文:")
        if f!= a[c]:
            e.append(b[c])
            d.append(a[c])
            print("正確答案:"+a[c])
        else:
            print("對")
        a.pop(c)
        b.pop(c)
    if len(d) != 0:
        for i in range(len(d)):
            print(d[i]+":"+e[i])
        b=input("input any key to continue:")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while len(d)!=0 :
        for i in range(len(d)):
            c=random.randint(0,len(d)-1)
            print(str(i+1)+". "+e[c])
            g=input("英文:")
            if g != d[c]:
                print("正確答案:"+d[c])
            else:
                d.pop(c)
                e.pop(c)
                print("對")
        if len(d) != 0:
            for i in range(len(d)):
                print(d[i]+":"+e[i])  
            b=input("input any key to continue:")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("背完囉~")
