Нужен парсер, который сможет превратить сотни и тысячи судебных статистических отчетов.
*в датасеты в JSON, CSV или ином формате. 
*с простой структурой

Извлеченные данные могут стать основой для кучи разных исследовательских и журналистских проектов и будут полезны для анализа судебной практики.


Лирика
Проектный центр “Инфометр” (read.infometer.org) продвигает открытость в массы и ищет крутых спецов, которые умеют парсить и структурировать большие объемы статистических данных.

В России 2098 судов районного уровня. Каждый год они выносят сотни тысяч приговоров и решений. И каждый год они собирают статистику по утвержденным формам.

Каждый отчет по одним только уголовным делам содержит показатели, отвечающие на тысячи вопросов, например:
Сколько граждан осудили в суде за грабёж (или другой статье) в 2015?
Сколько человек в год оправдывают и по каким статьям?
Какие меры наказания чаще применяются в суде?
Как часто деятельное раскаяние становится причиной прекращения уголовного дела?
Сколько преступлений совершили граждане в состоянии алкогольного, а сколько - в состоянии наркотического опьянения?
Часто ли суд отправляет подсудимого в СИЗО?
Эти показатели можно сравнивать по отдельным судам, по регионам и во временном разрезе. Можно сделать карту. 

В чем проблемы? 

Данные не машиночитаемы. Их надо парсить и структурировать. Все отчеты - экселевские таблицы, предназначенные для печати. 
Данных мало и они плохо публикуюся судами. В прошлом году мы проверяли и убедились, что опубликовано 10% судебной статистики (12 из 120 тысяч отчетов!) http://read.infometer.org/rating_raisud_2016 


Что мы уже сделали?
В ходе аудита мы не только проверили, но и добились публикации судами дополнительных 4 тысяч отчетов. В этом году будем добиваться публикации новых отчетов. Есть регионы, в которых отчетность публикуется почти полностью: Забайкальский край, Ивановская, Костромская область, Мордовия (рейтинг есть в отчёте)
В рейтинге мы собрали ссылки на статотчеты http://system.infometer.org/ru/monitoring/379/rating/, их можно выгружать.
Сделали парсер на основе макроса в Эксель. К сожалению, у него плохо получается обрабатывать много отчётов одновременно.

