from django.shortcuts import render
from django.http import HttpResponse

Kategori=['Dünya Klasik','Çocuk','Polisiye','Fantastik','Türk Klasik','Romantik','Korku-Gerilim','Macera']
kitap=[
     {
         'id':1,
         'kitap_adi':'Seksen Günde Devriâlem',
         'yazar_adi':'Jules Verne',
         'aciklama':'Fileas Fogg, son derece düzenli, titiz ve dakik yaşayan, sakin yapıda bir İngiliz centilmenidir. Arkadaşlarıyla, dünyayı 80 günde dolaşacağına dair, gerçekleştirilmesi olanaksız gibi görünen bir iddiaya girer. Yanına, yardımcısı Paspartüyü de alarak yola çıkar. 80 Günde Devriâlem, Jules Vernein dünya edebiyatına kazandırdığı en önemli yapıtlarından biri. Verne, gemilerle, trenlerle ya da fillerin sırtında yapılan, heyecan dolu geziyle birlikte, dünyanın güzelliklerini de sergiliyor.',
         'resim':'1.jpg',
         'anasayfa':True

     },
 ]

def home(request):
    data={
        'Kategoriler':Kategori,
        'Kitaplar':kitap,
    
}
    return render(request,'home.html',data)

def books(request):
    data={
        'Kategoriler':Kategori,
        'Kitaplar':kitap,
    
}
    return render(request,'books.html',data)

def bookdetails(request,id):
    data={
        'id':id
    
}
    return render(request,'details.html',data)