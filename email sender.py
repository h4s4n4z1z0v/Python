import smtplib
# Set up the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('your_email@gmail.com', 'your_password')
# Send the email
message = """\
From: your_email@gmail.com
To: recipient_email@gmail.com
Subject: Subject of your email
Body of your email
"""
server.sendmail('your_email@gmail.com', 'recipient_email@gmail.com', message)
# Close the connection
server.quit()

Bu kod, Gmail hesabı üzərindən Sadə Poçt Transfer Protokolu (SMTP) istifadə edərək e-poçtun necə göndərilməsini nümayiş etdirən Python skriptidir. Burada hər bir kod parçasının nə etdiyini addım-addım izah edirik:

**smtplib modulunun importu:**
Smtplib modulu SMTP protokolundan istifadə edərək e-poçt göndərmək üçün interfeys təmin edən daxili Python kitabxanasıdır.

**E-poçt serverinin qurulması:**
Kod smtplib.SMTP('[smtp.gmail.com](http://smtp.gmail.com/)', 587) istifadə edərək Gmail SMTP serverinə qoşulur. '[smtp.gmail.com](http://smtp.gmail.com/)' Gmail üçün SMTP server ünvanıdır və 587 təhlükəsiz rabitə (TLS) üçün ümumi istifadə edilən port nömrəsidir. Starttls() metodu Transport Layer Security (TLS) istifadə edərək təhlükəsiz əlaqəni başlatmaq üçün çağırılır. Bu addım məlumatları qorumaq üçün e-poçt ötürülməsini şifrələmək üçün çox vacibdir.

**Gmail hesabınıza daxil olun:**
Gmail serveri vasitəsilə e-poçtu təsdiqləmək və göndərmək üçün etibarlı Gmail hesabı ilə daxil olmalısınız. 'your_email@gmail.com' və 'your_password' sözlərini müvafiq olaraq faktiki Gmail e-poçt ünvanınız və parolunuzla əvəz edin. Bu məlumatlara diqqət yetirmək vacibdir və praktikada kodunuzdakı parollar kimi həssas məlumatlardan qaçınmalısınız.

**E-poçt mesajını tərtib edin:**
Mesaj dəyişəni e-poçtun məzmununu ehtiva edir. Bu, göndərənin e-poçt ünvanını (Kimdən:), alıcının e-poçt ünvanını (Kimə::), e-poçtun mövzusunu (Mövzu:) və e-poçtun mətnini ehtiva edən çoxsətirli sətirdir. Siz lazım olduqda göndərəni, alıcını, mövzunu və e-poçt orqanını fərdiləşdirmək üçün bu sətri dəyişdirə bilərsiniz.

**E-poçtun göndərilməsi:**
E-poçt göndərmək üçün server.sendmail() metodundan istifadə olunur. Bunun üçün üç arqument tələb olunur: göndərənin e-poçt ünvanı ('your_email@gmail.com'), alıcının e-poçt ünvanı ('recipient_email@gmail.com') və e-poçtun məzmununu saxlayan mesaj dəyişəni.

**Bağlantının bağlanması:**
E-poçt göndərildikdən sonra server.quit() funksiyasından istifadə edərək SMTP serveri ilə əlaqəni bağlamaq vacibdir. Bu addım əlaqənin düzgün şəkildə kəsilməsini təmin edir.

Nəzərə alın ki, bu kod Gmail ayarlarınızda "Az Təhlükəsiz Tətbiqlərə" icazə verdiyinizi güman edir və bu, təhlükəsizlik səbəbi ilə tövsiyə edilmir. Daha təhlükəsiz alternativlər üçün OAuth2 autentifikasiyası və ya proqram parolundan istifadə etməli və birbaşa kodda sərt kodlaşdırma parollarından qaçınmalısınız.
