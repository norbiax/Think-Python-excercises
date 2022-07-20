import time
t = time.time()
ts = int(t // 1)
tm = int(t // 60)
th = int(tm // 60)
td = int(th // 24)
print(t)
print('From the beginning of "the epoch" it has been: ', ts, 's.')
print('From the beginning of "the epoch" it has been: ', tm, 'min.')
print('From the beginning of "the epoch" it has been: ', th, 'h.')
print('From the beginning of "the epoch" it has been: ', td, 'days')
thours = th - td * 24
tmin = tm - th * 60
tsek = ts - tm * 60
print('From the beginning of "the epoch" it has been: ',
      td,
      ' days, ',
      thours,
      ' hours, '
      , tmin,
      ' min and '
      , tsek,
      'sek')

print(td*24*60*60+thours*60*60+tmin*60+tsek)


