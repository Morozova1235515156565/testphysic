t = None
s = None
v = None
F = None
M = None
g = 10


def calculate_speed(t, s):
    return s / t


def calculate_distance(v, t):
    return v * t


def calculate_time(v, s):
    return s / v


def calculate_taga(m, g):
    return m * g


def calculate_masscherztaga(F, g):
    return F / g


def calculate_pltnost(m, V):
    return m / V


def calculate_obhom(ρ, m):
    return m / ρ


def calculate_moment_force(F, l):
    return F * l


def calculate_lever_arm_length(M, F):
    return M / F


def calculate_sila(M, l):
    return M / l


def calculate_dav(F, S):
    return F / S


def calculate_sila_dav(p, S):
    return p * S


def calculate_pl_pov(P, f):
    return P * f


def calculate_dav_odnorod_dzid(ρ, g, h):
    return ρ * g * h


def calculate_visot(pa, g, ρ):
    return pa / (ρ * g)


def calculate_daviznach(pa, g, h):
    return pa / (g * h)


def calculate_zakon_arkhimeda(ρ, g, V):
    return ρ * g * V


def calculate_dav_iz_arkhimeda(F, g, V):
    return F / (g * V)


def calculate_obhkom_arkh(F, g, ρ):
    return F / (ρ * g)


def calculate_rabota(F, S):
    return F * S


def calculate_sila_iz_rabota(A, S):
    return A / S


def calculate_put_iz_rabota(A, F):
    return A / F


def calculate_Kpd(Apol, Azat):
    return (Apol / Azat) * 100


def calculate_Apol(η, Azat):
    return (η * Azat) / 100


def calculate_Azat(η, Apol):
    return (η * Apol) / 100
def calculate_energy_pot(m ,g , h):
    return m * g * h
def calculate_visot_ep(ep,g,m):
    return ep/(g*m)

def calculate_sila_trenia(μ, P):
    return μ *P
def calculate_koef(Ftren,P):
    return Ftren/P
formulas = {
    'Найти скорость': calculate_speed,
    'найти скорость': calculate_speed,
    'Найти расстояние': calculate_distance,
    'найти расстояние': calculate_distance,
    'Найти время': calculate_time,
    'найти время': calculate_time,
    'Найти силу тяжести': calculate_taga,
    'найти силу тяжести': calculate_taga,
    'Найти массу': calculate_masscherztaga,
    'найти массу': calculate_masscherztaga,
    'Найти плотность': calculate_pltnost,
    'найти плотность': calculate_pltnost,
    'Найти объём': calculate_obhom,
    'найти объём': calculate_obhom,
    'Найти вес': calculate_taga,
    'найти вес': calculate_taga,
    'Найти массу через вес': calculate_masscherztaga,
    'найти массу через вес': calculate_masscherztaga,
    'Найти момент силы': calculate_moment_force,
    'найти момент силы': calculate_moment_force,
    'Найти длинну плеча': calculate_lever_arm_length,
    'найти длинну плеча': calculate_lever_arm_length,
    'Найти силу через момент силы': calculate_sila,
    'найти силу через момент силы': calculate_sila,
    'Найти давление': calculate_dav,
    'найти давление': calculate_dav,
    'Найти силу давления': calculate_sila_dav,
    'найти силу давления': calculate_sila_dav,
    'Найти площадь поверхности оказывающая давление': calculate_pl_pov,
    'найти площадь поверхности оказывающая давление': calculate_pl_pov,
    'Найти давление однородной жидкости': calculate_dav_odnorod_dzid,
    'найти давление однородной жидкости': calculate_dav_odnorod_dzid,
}

task = input("Введите задачу: ")
words = task.split()

if 'найти' in words:
    if 'время' in words:
        if 'км/ч' in words and 'км' in words:
            index_v = words.index('км/ч')
            v = float(words[index_v - 1])
            index_s = words.index('км')
            s = float(words[index_s - 1])
            result = formulas['Найти время'](v, s)
            print('Время равно', result, 'ч')
        else:
            print('Неверные данные или поставленный вопрос')

    elif 'расстояние' in words:
        if 'ч' in words and 'км/ч' in words:
            index_t = words.index('ч')
            t = float(words[index_t - 1])
            index_v = words.index('км/ч')
            v = float(words[index_v - 1])
            result = formulas['Найти расстояние'](v, t)
            print('Расстояние равно', result, 'км')
        else:
            print('Неверные данные или поставленный вопрос')

    elif 'скорость' in words:
        if 'ч' in words and 'км' in words:
            index_t = words.index('ч')
            t = float(words[index_t - 1])
            index_s = words.index('км')
            s = float(words[index_s - 1])
            result = formulas['Найти скорость'](t, s)
            print('Скорость равна', result, 'км/ч')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'силу' in words and 'тяжести' in words:
        if 'кг' in words:
            index = words.index('кг')
            m = float(words[index - 1])
            result = formulas['Найти силу тяжести'](m, g)
            print('Сила тяжести равна', result, 'Н')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'массу' in words and 'через' in words and 'тягу' in words:
        if 'Н' in words or 'H' in words:
            index = words.index('Н')
            F = float(words[index - 1])
            result = formulas['Найти массу'](F, g)
            print('Масса через силу тяжести равна', result, 'кг')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'плотность' in words:
        if 'кг' in words and 'м^3' in words:
            index_m = words.index('кг')
            m = float(words[index_m - 1])
            index_V = words.index('м^3')
            V = float(words[index_V - 1])
            result = formulas['найти плотность'](m, V)
            print('Плотность равна', result, 'кг/м^3')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'объём' in words and 'из' in words and 'силы' in words and 'Архимеда' in words:
        if 'Па' in words and 'Н' in words or 'H' in words:
            index_ρ = words.index('Па')
            ρ = float(words[index_ρ - 1])
            index_F = words.index('Н')
            F = float(words[index_F - 1])
            result = calculate_obhkom_arkh(F, g, ρ)
            print('Обёъём равен', result, 'м^3')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'объём' in words:
        if 'кг/м^3' in words and 'кг' in words:
            index_p = words.index('кг/м^3')
            ρ = float(words[index_p - 1])
            index_m = words.index('кг')
            m = float(words[index_m - 1])
            result = formulas['Найти объём'](ρ, m)
            print('Объём равен', result, 'м^3')
        else:
            print("Некорректный ввод.")
    elif 'вес' in words:
        if 'кг' in words:
            index = words.index('кг')
            m = float(words[index - 1])
            result = formulas['Найти вес'](m, g)
            print('Вес равен', result, 'Н')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'массу' in words:
        if 'Н' in words or 'H' in words:
            index = words.index('Н')
            F = float(words[index - 1])
            result = formulas['Найти массу через вес'](F, g)
            print('Масса через вес равна', result, 'кг')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'длинну' in words and 'плеча' in words:
        if 'Hm' in words and 'H' in words or 'Н' in words:
            index = words.index('Hm')
            M = float(words[index - 1])
            index = words.index('H' or 'Н')
            F = float(words[index - 1])
            result = formulas['Найти длинну плеча'](M, F)
            print('Длинна плеча равна', result, 'м')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'момент' in words and 'силы' in words:
        if 'м' in words and 'H' in words or 'Н' in words:
            index = words.index('м')
            l = float(words[index - 1])
            index = words.index('Н')
            F = float(words[index - 1])
            result = formulas['Найти момент силы'](F, l)
            print('Момент силы равен', result, 'Hm')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'силу' in words and 'Архимеда' in words:
        if 'Па' in words or 'па' in words and 'м^3' in words:
            index_ρ = words.index('Па')
            ρ = float(words[index_ρ - 1])
            index_V = words.index('м^3')
            V = float(words[index_V - 1])
            result = calculate_zakon_arkhimeda(ρ, g, V)
            print('Сила Архимеда равна', result, 'H')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'силу' in words and 'из' in words and 'механической' in words and 'работы' in words:
        if 'Дж' in words and 'м' in words:
            index_A = words.index('Дж')
            A = float(words[index_A - 1])
            index_S = words.index('м')
            S = float(words[index_S - 1])
            result = calculate_sila_iz_rabota(A, S)
            print('Сила из механической работы равна', result, 'Н')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'силу' in words:
        if 'м' in words and 'Hm' in words:
            index = words.index('м')
            l = float(words[index - 1])
            index = words.index('Hm')
            M = float(words[index - 1])
            result = formulas['Найти силу через момент силы'](M, l)
            print('Сила', result, 'H')
        else:
            print('Неверные данные или поставленный вопрос')
    if 'первоначальное' in words and 'давление' in words:
        if 'см' in words and 'па' in words:
            index_h = words.index('см')
            h = float(words[index_h - 1])
            index_pa = words.index('па')
            pa = float(words[index_pa - 1])
            result = calculate_daviznach(pa, g, h)
            print('Первоначальное давление:', result, 'Па')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'Силу' in words and 'давления' in words:
        if 'Па' in words and 'м^2' in words:
            index = words.index('Па')
            p = float(words[index - 1])
            index = words.index('м^2')
            S = float(words[index - 1])
            result = formulas['Найти силу давления'](p, S)
            print('Сила давления равна', result, 'H')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'площадь' in words and 'поверхности' in words:
        if 'Па' in words and 'H' in words or 'Н' in words:
            index_p = words.index('Па')
            P = float(words[index_p - 1])
            index_h = words.index('Н')
            f = float(words[index_h - 1])
            result = formulas['найти площадь поверхности оказывающая давление'](P, f)
            print('Площадь поверхности оказывающее давление', result, 'м^2')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'давление' in words and 'из' in words and 'силы' in words and 'Архимеда' in words:
        if 'Н' in words and 'м^3' in words:
            index_F = words.index('Н')
            F = float(words[index_F - 1])
            index_v = words.index('м^3')
            V = float(words[index_v - 1])
            result = calculate_dav_iz_arkhimeda(F, g, V)
            print('Давление равно', result, 'Па')
        else:
            print('Неверные данные или поставленный вопрос')


    elif 'давление' in words and 'однородной' in words and 'жидкости' in words:
        if 'Па' in words and 'см' in words:
            index_ρ = words.index('Па')
            ρ = float(words[index_ρ - 1])
            index = words.index('см')
            h = float(words[index - 1])
            result = formulas['Найти давление однородной жидкости'](ρ, g, h)
            print('Сила давления однородной жидкости равна', result, 'Па')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'высоту' in words and 'жидкости' in words:
        if 'Па' in words and 'па' in words:
            index_ρ = words.index('Па')
            ρ = float(words[index_ρ - 1])
            index_pa = words.index('па')
            pa = float(words[index_pa - 1])
            result = calculate_visot(pa, g, ρ)
            print('Высота однородной жидкости равна', result, 'см')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'давление' in words:
        if 'H' in words or 'Н' in words and 'м^2' in words:
            index = words.index('Н' or 'H')
            F = float(words[index - 1])
            index = words.index('м^2')
            S = float(words[index - 1])
            result = formulas['Найти давление'](F, S)
            print('Давление равно', result, 'Па')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'механическую' in words and 'работу' in words:
        if 'H' in words or 'Н' in words and 'м' in words:
            index_F = words.index('Н')
            F = float(words[index_F - 1])
            index_S = words.index('м')
            S = float(words[index_S - 1])
            result = calculate_rabota(F, S)
            print('Механическая работа равна', result, 'Дж')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'путь' in words and 'пройденный' in words and 'телом' in words and 'под' in words and 'воздействием' in words and 'силы' in words:
        if 'Н' in words and 'Дж' in words:
            index_A = words.index('Дж')
            A = float(words[index_A - 1])
            index_F = words.index('Н')
            F = float(words[index_F - 1])
            result = calculate_put_iz_rabota(A, F)
            print('Пройденный путь телом под воздействием силы', result, 'м')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'полезную' in words and 'работу' in words and 'через' in words and 'кпд' in words:
        if '%' in words and 'Дж' in words:
            index_η = words.index('%')
            η = float(words[index_η - 1])
            index_Azat = words.index('Дж')
            Azat = float(words[index_Azat - 1])
            result = calculate_Apol(η, Azat)
            print('Полезная работа равна из КПД', result, 'Дж')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'затраченную' in words and 'работу' in words and 'через' in words and 'кпд' in words:
        if '%' in words and 'дж' in words:
            index_Apol = words.index('дж')
            Apol = float(words[index_Apol - 1])
            index_η = words.index('%')
            η = float(words[index_η - 1])
            result = calculate_Azat(η, Apol)
            print('Затраченная работа полученная из КПД равна', result, 'ДЖ')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'кпд' in words:
        if 'Дж' in words and 'дж' in words:
            index_Apol = words.index('Дж')
            Apol = float(words[index_Apol - 1])
            index_Azat = words.index('дж')
            Azat = float(words[index_Azat - 1])
            result = calculate_Kpd(Apol, Azat)
            print('Коэффициент полезного действия равен', result, '%')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'высоту' in words and 'на' in words and 'которой' in words and 'находится' in words and 'объект' in words:
        if 'Дж' in words and 'кг' in words:
            index_ep = words.index('Дж')
            ep = float(words[index_ep-1])
            index_m = words.index('кг')
            m = float(words[index_m-1])
            result = calculate_visot_ep(ep, g, m)
            print('Высота равна',result,'см')
        else:
            print('Неверные данные или поставленный вопрос')

    elif 'потенциальную' in words and 'энергию' in words:
        if 'кг' in words and 'см' in words:
            index_m = words.index('кг')
            m = float(words[index_m - 1])
            index_h = words.index('см')
            h = float(words[index_h -1])
            result = calculate_energy_pot(m, g, h)
            print('Потенциальная энергия равна',result,'ДЖ')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'силу' in words and 'трения' in words:
        if 'Н' in words and 'мю' in words:
            index_P = words.index('Н')
            P = float(words[index_P - 1])
            index_μ = words.index('мю')
            μ = float(words[index_μ + 1])
            result = calculate_sila_trenia(μ,P)
            print('Сила трения',result,'Н')
        else:
            print('Неверные данные или поставленный вопрос')
    elif 'коэффициент' in words and 'трения' in words:
        if 'Н' in words and 'H' in words:
            index_P = words.index('Н')
            P = float(words[index_P - 1])
            index_Ftren = words.index('H')
            Ftren = float(words[index_Ftren -1])
            result = calculate_koef(Ftren,P)
            print('Коэффициент трения равен',result)
        else:
            print('Неверные данные или поставленный вопрос')






else:
    print("Некорректный ввод")
