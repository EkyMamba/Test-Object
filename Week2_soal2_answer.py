klub1 = (input("Klub A : "))
klub2 = (input("Klub B : "))

match = 1 
hasil = []

teamA, teamB = input(f'Pertandingan {match} : ').split()
teamA = int(teamA)
teamB = int(teamB)

while (teamA) >= 0 and (teamB) >= 0:

    if teamA > teamB:
        hasil.append(klub1)
    elif teamA < teamB:
        hasil.append(klub2)
    else:
        hasil.append('Draw')
    match += 1

    teamA, teamB = input(f'Pertandingan {match} : ').split()
    teamA = int(teamA)
    teamB = int(teamB)

x = 1
for i in hasil:
    if teamA > teamB:
        print(f'Hasil round ke-{x} : {hasil[0]}')
    elif teamA < teamB:
        print(f'Hasil round ke-{x} : {hasil[1]}')
    else:
        print(f'Hasil round ke-{x} : {hasil[2]}')
    x += 1

print('===Pertandingan selesai===')