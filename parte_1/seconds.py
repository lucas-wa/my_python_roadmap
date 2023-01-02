# -- coding: UTF-8 -- #

secIn = int(input());

d = secIn//86400;

secIn = secIn%86400;

h = secIn//3600;

secIn = secIn % 3600;

m = secIn//60;

secIn = secIn % 60;

print(d, "dias,", h, "horas,", m, "minutos e", secIn, "segundos.");