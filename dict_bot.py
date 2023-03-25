# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в объект DEFINITOINS на 13 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='5654259068:AAGh9Bl_v_itXLRNhXd_eJbb9LYefDK1GCs', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
'авторизация': '(от англ. «authorization») — предоставление определенному лицу или группе лиц прав на выполнение определенных действий',
'адаптив': '(или «адаптивный дизайн», от англ. «adaptation») — процесс адаптации веб-страниц или веб-интерфейса к использованию на экранах различных устройств',
'аджайл': '(от англ. «Agile») — Философия, подход к организации труда, характериз-ся гибкостью в разработке программного обеспечения, который часто применяют в небольших командах и больших организациях. Процесс работы «по эджайлу» делится на итерации — короткие циклы по две-три недели. Каждый цикл решает серию задач',
'айди': '(или «айдишник», от англ. «id», «identificator») — уникальный признак объекта, который позволяет отличить его от других объектов, то есть идентифицировать',
'айпи': '(или «айпишник», «айпи-адрес», от англ. «IP», «Internet Protocol Address») — уникальный адрес компьютера в Сети, который присваивается провайдером индивидуально каждому устройству и даёт возможность выхода в Интернет',
'аккаунт': '(или «акаунт», «ак», от англ. «account») — учетная запись, совокупность данных пользователя, необходимых для его аутентификации. Обычно создается после регистрации на каком-либо ресурсе (на сайте / в приложении/ в программе)',
'альфа': 'Это внутренний/непубличный этап разработки ПО, во время которого разработчики дополняют программу новыми функциями, после чего тестировщики проверяют/испытывают измененную программу',
'анрег': 'незарегистрированный пользователь, ранее не проходивший аутентификацию на ресурсе/программе',
'апгрейд': '(от англ. «upgrade») — усовершенствование / обновление и модернизация компьютерной техники (железа), программного обеспечения, аппаратуры и т.д.',
'апдейт': 'обновление/модернизация программного обеспечения (софта)',
'апи': '(от англ. «API», «Application Programming Interface») — описание способов, которыми одна компьютерная программа может взаимодействовать с другой программой. АПИ определяет, как программы взаимодействуют друг с другом, используя запросы и ответы',
'аттач': 'файл, который прикреплён к электронному письму или XML',
'аутентификация': 'процедура проверки подлинности, например: проверка подлинности пользователя путём сравнения введённого им пароля (для указанного логина) с паролем, сохранённым в базе данных пользовательских логинов',
'аутсорс': 'распространенная практика, когда компания передает часть рабочих задач специалистам вне своего штата (фрилансерам / работникам других компаний)',
'баг': 'некая ошибка/дефект в написанном коде/программе, из-за которой программа ведет себя неожиданно, и, как следствие, выдает неправильные результаты',
'баг репорт': 'это отчёт, который информирует об ошибке в работе приложения. Сам документ доложен быть хорошо структурирован и содержать необходимую информацию.',
'баг-репорт': 'это отчёт, который информирует об ошибке в работе приложения. Сам документ доложен быть хорошо структурирован и содержать необходимую информацию.',
'база данных': 'программный или программно-аппаратный комплекс, разработанный для хранения большого объема различной информации',
'бэкенд': 'непосредственно сама программно-аппаратная или серверная часть приложения, а также разработка этой «внутренней части» сайтов/ПО/приложений',
'бэклог продукта' :'перечень рабочих задач, расположенных в порядке важности, для команды разработчиков. Его составляют на основе дорожной карты и требований в ней. Наиболее важные задачи расположены в начале бэклога продукта, чтобы команда понимала, какую работу следует выполнить в первую очередь',
'валидация': '(validation) — это определение соответствия разрабатываемого ПО ожиданиям и потребностям пользователя, его требованиям к системе.',
'верификация': '(verification) — это процесс оценки системы, чтобы понять, удовлетворяют ли результаты текущего этапа разработки условиям, которые были сформулированы в его начале.',
'вкладки': 'элемент интерфейса, так же как и аккордеон, состоит из заголовка и скрытого контента, на который можно попасть при обращении к заголовку',
'груминг': 'это собрание представителей Scrum-команды, во время которого обсуждаются детали бэклога продукта и готовится очередное планирование спринта',
'гит': 'Система контроля версиями, ветками',
'гитхаб': 'крупный веб-сервис для хранения (хостинга) репозиториев IT-проектов и совместной работы над ними. GitHub является своеобразной соц. сетью для программистов, которая позволяет им ознакомится с кодом друг друга, прокомментировать его и помочь в разработке',
'дейли': 'От англ. daily (дословно — ежедневно) — ежедневные короткие (от 5 до 30 минут) встречи команды с целью поделиться прогрессом по выполненным задачам за предыдущий день и озвучить план работ на текущий день. Также дейли могут называть стендапом.',
'идентификация': 'процедура, в результате выполнения которой для субъекта идентификации выявляется его идентификатор, однозначно определяющий этого субъекта в информационной системе',
'канбан': 'Kanban — методология гибкого управления, предполагает обсуждение производительности в режиме реального времени и полную прозрачность рабочих процессов. Рабочие задачи визуально представлены на доске Kanban, что позволяет участникам команды видеть состояние каждой задачи в любой момент времени',
'курл': 'cURL - это программа, утилита  командной строки для Linux или Windows, смысл которойв том, чтобы сделать какой-то запрос и получить ответ. CURL - это клиент, который выполняет запросы к какому-то серверу',
'локализовать багу': 'процесс "расследования" произошедшего бага (ошибки): поиск ее в коде, выяснение причины произошедшего, изучение последствий',
'линуксовая консоль': 'консоль, которая позволяет вводить текстовые данные с клавиатуры и отображать их на экране.',
'линтер css': 'проверка на соблюдение стандарта синтаксиса css',
'майлстоун': 'Milestone показывает зачем мы вообще тестируем. Например, потому что вышла новая версия',
'нагрузочное тестирование': 'это тестирование в пределах значений нагрузки, которые должна выдерживать система, а стрессовое – это тестирования за ее пределами.',
'пагинация': 'порядковая нумерация страниц',
'пофиксить': '(или «фиксить», от англ. «fix») — исправить/наладить работу, внести необходимые правки',
'превью': '(от англ. «Preview») — компактные/уменьшенные в несколько раз изображения (миниатюры) для более удобного предварительного просмотра',
'предпрод': '(Preprod Env) – среда, которая максимально приближена к продакшену. Здесь проводится заключительное тестирование функционала.',
'прод': 'Ветка с рабочей версией продукта, которую видят пользователи. Это окончательная точка куда попадает результат разработки. Иногда так же называют мастер.',
'продакшн': '(Production Env) – среда, в которой работают пользователи.',
'ревью': '(или «кодревью», от англ. «review») — рецензирование/вычитка/проверка кода с целью обнаружения и исправления ошибок',
'регресс': 'проверить, что новый функционал не сломал существующий',
'регрес': 'проверить, что новый функционал не сломал существующий',
'редизайн': '(от англ. «redesign») — обновление и модификация визуальной графической или структурно-функциональной составляющей приложения/сайта/интерфейса и т.д.',
'редирект': '(от англ. «redirect») — автоматическое перенаправление/переадресация юзера куда-либо: на другой сайт, на другую страницу, на другую почту и т.д.',
'релиз': '(от англ. «release») — выпуск окончательной версии программы — готового для использования продукта.',
'ресёрч': '(или «ресерч», от англ. «research») — поиск полезной информации, изучение определенной темы с целью разобраться в ней, понять суть, детали',
'рефакторинг кода': '(от англ. «refactoring») — корректировка исходного кода ПО для того, чтобы сделать его "чистым", т.е. простым и легким для понимания и последующей поддержки.',
'cаппорт': '(или «супорт», «поддержка», «сап», от англ. «support») — служба технической поддержки, в которую пользователи продукта или услуги могут обратиться за оказанием помощи по разрешению возникших трудностей и получением дополнительной информации.',
'скрам': '(от англ. «scrum») — один из методов управления проектами, является частью гибкой методологии разработки Agile. Обычно используется в сфере разработки ПО, но может применятся и в других производственных отраслях.',
'слэйв': 'реплика базы данных (на случай, если что-то сломается в основной(мастере) – можно из Slave сделать мастера',
'таска': 'От англ. task — задача, заведенная или планируемая на любого работника.',
'стресс тестирование': 'это тестирования за  пределами значений предусмотренной  нагрузки',
'смоук тестирование': 'проверка программного обеспечения на стабильность и наличие явных ошибок. Тест должен подтвердить или опровергнуть правильность выполнения ПО своих основных функций перед его передачей на более глубокое тестирование',
'сниффер': 'инструменты, позволяющие перехватывать, анализировать и модифицировать все запросы, которые через них проходят. Они позволяют исследовать сетевое взаимодействие клиента и сервера (это, грубо говоря, высветляет наш черный ящик), а также эмулировать различные тестовые сценарии, модифицируя трафик',
'тестовая документация': 'тестовая документация включает в себя: тест план; тестовая стратегия; чек-лист; тестовый сценарий; тестовый комплект; пользовательская история (User Story); отчет о дефекте',
'тмс': 'системы управления тестированием (Test Management System, TMS) используются для хранения информации о том, как должным образом проводить тестирование, осуществление очередности проведения тестирования в соответствии с его планом, а также для получения информации в виде отчетов о стадии тестирования и качестве тестируемого продукта',
'тест кейс': 'четкое описание действий, кот. необх выполнить в рамках проверки данного функционала',
'тест сьюит': 'Набор тест кейсов, в рамках одного  тестируемого модуля, объединенных по какому-то признаку (например кейсы регресса, или тесты смоук тестирования). Каждый тест сьют состоит из более чем одного тест кейса и зачастую выполняется всей «пачкой» в процессе тестирования',
'тест план': 'это документ, описывающий весь объем работ по тестированию, начиная с описания объекта, стратегии, расписания, критериев начала, подготовка к тестированию, чек листы, регресс, время на тестирование, подготовка к релизу',
'урл': '(или «урла», «урээл», от англ. «URL») — унифицированный указатель ресурса, определенный шаблон записи гипертекстовых ссылок на объекты в Интернете. Простыми словами, это адрес странички в Сети.',
'факап': '(или «облом», «фиаско», от англ. «fuck up») — неудача/провал/облом (чаще имеют ввиду крупные/серьёзные ошибки.', 
'фиксить': 'от англ. «fix» — исправить/наладить работу, внести необходимые правки.',
'фидбек': '(от англ. «feedback») — 1) обратная связь, отзыв, рецензия о чем-либо',
'фича': '(от англ. «feature») — уникальная особенность/свойство/функция какого либо объекта (ПО, приложения, ОС).',
'фронтенд': '(от англ. «front-end») — создание «внешней оболочки» веб-сайта/приложения (то, что видит пользователь).',
'хост': '(от англ. «hosting») — центральный сервер сети (любой компьютер), подключённый к локальной или глобальной сети.',
'хэдер': '(или «хедер», от англ. «header») — 1) элемент веб-страницы, расположенный в верхней его части и содержащий: логотип, меню, служебную информацию и т.д. 2) заголовочный файл библиотеки (.h)',
'чекать': '(от англ. «check») — что-то проверять, просматривать на предмет необходимой информации или для поиска ошибок.',
'чекбокс': '(или «флажок», «флаговая кнопка», «галка», от англ. «check box») — элемент графического интерфейса, который дает пользователю возможность управлять параметром с двумя состояниями (например, ☑ включено и ☐ отключено).',
}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе расшифровать сложные термины \nВведи интересующий термин, например, фича', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='Я пока не знаю такого определения',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
