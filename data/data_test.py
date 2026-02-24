from .urls import UrlsNav




class DataTestLinks:

    # test_navigation_menu

    MENU_ITEMS = [
        ("Калькуляторы", UrlsNav.JOURNAL_CALCULS, "Калькуляторы"),
        ("Игры", UrlsNav.JOURNAL_TESTS, "Игры"),
        ("Подкасты и видео", UrlsNav.JOURNAL_SHOWS, "Подкасты и видео"),
        ("Письма", UrlsNav.JOURNAL_LETTERS, "Письма"),
        ("Шопинг", UrlsNav.JOURNAL_SHOPPING, "Шопинг"),
        ("Сравнятор", UrlsNav.JOURNAL_SRAVNATOR, "Сравнятор"),
        ("Аптечка", UrlsNav.JOURNAL_APTECHKA, "Проверьте эффективность лекарств"),
        ("Новости", UrlsNav.JOURNAL_NEWS, "Новости"),
        ("Дневники трат", UrlsNav.JOURNAL_DIARY, "Дневники трат"),
        ("Инвестиции", UrlsNav.JOURNAL_INVEST, "Инвестиции"),
        ("Права и обязанности", UrlsNav.JOURNAL_PRAVO, "Права и обязанности"),
        ("Недвижимость", UrlsNav.JOURNAL_REALTY, "Недвижимость"),
        ("Медицина и здоровье", UrlsNav.JOURNAL_HEATH, "Медицина и здоровье"),
        ("Путешествия", UrlsNav.JOURNAL_TRAVEL, "Путешествия"),
        ("Мозг", UrlsNav.JOURNAL_MOZG, "Мозг"),
        ("Образование", UrlsNav.JOURNAL_STUDY, "Образование"),
        ("Поп-культура", UrlsNav.JOURNAL_CULTURE, "Поп-культура"),
        ("Еда", UrlsNav.JOURNAL_FOOD, "Еда"),
        ("Смотреть все", UrlsNav.JOURNAL_FLOWS, "Потоки")
    ]



class DataTestSearch:

    # test_search_result_negative_bad_params

    NEGATIVE_QUERIES = [
        ("!@#$%^&*()_+", "Ничего не нашлось"),
        ("~`\"';:,.<>?/\\|", "Ничего не нашлось"),
        ("№[]{}-=", "Ничего не нашлось"),
        ("99999999999999999990000000000", "Ничего не нашлось"),
        ("   ", "Ничего не нашлось"),           
        ("<script>alert('xss')</script>", "Ничего не нашлось"), 
        ("SELECT * FROM users", "Ничего не нашлось"),           
        ("'; DROP TABLE posts; --", "Ничего не нашлось"),       
        ("а" * 256, "Ничего не нашлось"),   
        ("😂🚀🔥", "Ничего не нашлось"),
        (" ", ""), 
        ("Z", ""), 
        ("{", ""),        
    ]

    # test_search_result_positive

    POSITIVE_QUERIES = [
        ("Ипотека?", "ипотек"),          
        ("налОги", "налог"),            
        ("Apple", "Apple"),             
        ("2025", "2025"),               
        ("кредит на авто", "кредит"), 
        ("  вклады  ", "вклад"), 
        ("vvv", "vvv"),
        ("ставка", "ставка")
    ]

    # test paginator

    search_text = POSITIVE_QUERIES[-1]



    

class DataTestAverageIncomeCalcs:

    # Текст загаловка в контейнере, role_name, value

    header_family = "сколько вас в семье"
    header_period = "за какой период нужно посчитать доход"
    header_your = "ваш доход"
    header_husband = "у мужа или жены есть доход"
    header_child = "есть дети с официальным доходом"

    result = r"110\s?875"

   
    # поля числа человек в семье и количества месяцев
    data_test_family_period = [
                            "5",
                            "-6",
                            "0",
                            "qhjku",
                            "13fdgh",
                        ]
    # Данные для теста: (текстовое_поле, цифровое_поле)
    data_test_income = [
        ("зарплата", "300000"),
        ("income", "125ffj"),
        ("     откаты!", "  5600"),
        ("-110005000", "200000000"),
        ("!!!!!!", "77  000"),
    ]
