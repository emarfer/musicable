import src.listas as lis

holi = lis.check_tempos()
if holi == 'listas de rep al día':
    print(holi)
elif type(holi) == list:
    juntico = ', '.join(holi)
    print(f"creating lists for {juntico}")
    lis.create_datframe(holi)