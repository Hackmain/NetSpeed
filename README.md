# NetSpeed
This a simple code for beginners to learn how the codes calculate the internet download &amp; upload speed using libs
دعوني أشرح لك خطوات هذا الكود:

استيراد المكتبة:
يتم استيراد مكتبة speedtest باستخدام السطر التالي:
Python

import speedtest
AI-generated code. Review and use carefully. More info on FAQ.
إنشاء دالة get_speed:
تم إنشاء دالة تسمى get_speed.
تُستخدم هذه الدالة لقياس سرعة الإنترنت الفعلية.
تُنفذ الدالة عن طريق إنشاء كائن من الفئة Speedtest (المقدمة من مكتبة speedtest).
تُحسب سرعة التنزيل وسرعة الرفع بالميجابت في الثانية (Mbps).
العرض:
يتم عرض سرعة التنزيل وسرعة الرفع باستخدام الدالة print.
يتم تحويل القيم من بايت إلى ميجابايت.
التنفيذ الرئيسي:
يتم تنفيذ الدالة get_speed عند تشغيل البرنامج.
