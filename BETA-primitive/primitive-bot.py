#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 00:15:28 2019

@author: DavutOgulcanCelik
"""
import random
import tweepy

CONSUMER_KEY ="XXXX"
CONSUMER_SECRET = "XXXX"
ACCESS_KEY = "XXXX"
ACCESS_SECRET = "XXXX"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
#api.update_status('Updating using OAuth authentication via Tweepy!')

a = ['kitaplar','yetersiz olmak','yanlış bakmak','kör yaşamak','ritimle bütünleşmek','-docbot-','bot olmam','bot olarak','yanlış olmak','özen','düzen','düzene düzülmek','acabalar','kara bulutlar','kırılması gereken algılar','boş sorgulayan gözler','değişik takıntılar','antik yunan felsefesi','boş adamlar','benim yerime karar verenler','popüler kültür','astronotlar','mendiller','kaba düşünceler','steve jobs','ikindi','öğlen','sabah','sahip olmak','sabahın sahibi','bir dostum','dune evreni','ilginç şeyler','felsefeciler','köpekler','gezegenbilimciler','ışıksız odadakiler','asosyaller','ne için yaşadığını bilmeyenler']
b = ['herhalde','şu günlerde','iyi hoş güzelde','sabahtan','ileride','kafada','boşda','bulutlu günün ertesinde','anın gereklerine','akıllarda','kafalarda','değişik algılarda','kavram karmaşasında','bozuk beyinlerde','sulanmış gözlerde','siyasallarda','mantıksal çıkış yolları aramada','geriye dönüp bakamda','mitik düşüncelerde','milletde','kişilerde','ağzı bozuk insanlarda','eli cebinde gezenlerde','küçük bir köyde','niye böyle olduğunu bilmede','bazı sorunları aşmada','başına buyruk olmada','aynı hatayı ikincikez yapmada']
c =  ['değişmişcesine','','baştan','düşkün','itici','havalı','daima','bulutta','güzelce','ileri','anın gerektirdiği şekilde','boşlukta dolaşırcasına','sendeleyerek','bazı şeyleri unutarak','gerektiği gibi','olması gibi','gibi','öznelerde','edebiyat açısından zayıf','düşüncelere karşı set çekmiş biçimde','kafasını yormadan','geleceğe odaklanarak','beynindeki sınırları açarak','bozuk siyallerle','bencilce düşünerek','kafasına göre takılarak','umarsızca','kaybolmuşcasına','boş düşüncelerle','değişik kafalarla birlikte','eski sapiensce','gözü pek gibi','korkusuzca','kaygılanarak']
d = ['çoktur','kokuşmuştur','çürümüştür','boş düşüncedir','mistik bir yaklaşım gibidir','anladığımdır','düşüncemdir','ırgalamaz','ondan oldu','kafaya takmadı','sığ kaldı','düşündürttü','itici geldi','uzak kaldı','sorundur','altı boş imadır','içindedir','ileridedir','ufukta görünüyor','pek görünmüyor','bekledi','çekmişti','hata ediyor.','hareket ediyor.','ısrar ediyor','yaşadı','doğru buluyor','anlamsız buluyor','sığ kalıyor','dibe giriyor','kafasını boşa yoruyor','sınırları zorluyor','niye böyle bilmiyor','pek bilmiyor','boş yapıyo','aklını kullanmıyo'  ]

tweet = random.choice(a) + ' ' + random.choice(b) + ' ' + random.choice(c) + ' ' + random.choice(d)

api.update_status(tweet+'.' + ' #botolarakdüşüncem')
print(tweet)
