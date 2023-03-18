"""
W pliku dane.txt znajduje się 200 wierszy. Każdy wiersz zawiera 320 liczb naturalnych
z przedziału od 0 do 255, oddzielonych znakami pojedynczego odstępu (spacjami).
Przedstawiają one jasności kolejnych pikseli czarno-białego obrazu o wymiarach 320 na 200
pikseli (od 0 – czarny do 255 – biały).
Napisz program(y), który(e) da(dzą) odpowiedzi do poniższych zadań. Odpowiedzi zapisz
w pliku wyniki6.txt, a każdą odpowiedź poprzedź numerem oznaczającym odpowiednie
zadanie.
Uwaga: plik przyklad.txt zawiera dane przykładowe spełniające warunki zadania (obraz
ma takie same rozmiary). Odpowiedzi dla danych z pliku przyklad.txt są podane pod
poleceniami. 
"""
import os
dane = "Dane_PR/dane.txt" #os.path.join('DANE_PR2', "dane.txt")
przyklad =  "Dane_PR/przyklad.txt" #os.path.join('DANE_PR2', "przyklad.txt")
MAX_NUMBER = 255
MIN_NUMBER = 0
ROW_NUMBER = 200
COLUMN_NUMBER = 320


def get_pixels(filepath):
    pixels = []
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip().split(' ')
            pixels.append([int(piksel) for piksel in line])
    return pixels

"""
Podaj jasność najjaśniejszego i jasność najciemniejszego piksela.
Dla danych z pliku przyklad.txt wynikiem jest 255 (najjaśniejszy) i 0 (najciemniejszy).
"""
def zad1(filepath):
    min_ans = MAX_NUMBER
    max_ans = MIN_NUMBER

    pixels = get_pixels(filepath=filepath)

    for line in pixels:
        for number in line:
            if int(number) > max_ans:
                max_ans = int(number)
            if int(number) < min_ans:
                min_ans = int(number)
    return min_ans, max_ans

"""
Podaj, ile wynosi najmniejsza liczba wierszy, które należy usunąć, żeby obraz miał pionową oś
symetrii. Obraz ma pionową oś symetrii, jeśli w każdym wierszu i-ty piksel od lewej strony
przyjmuje tę samą wartość, co i-ty piksel od prawej strony, dla dowolnego 1 ≤ i ≤ 320. 
"""
def zad2(filepath):
    min_rows_to_remove = 0
    pixels = get_pixels(filepath=filepath)

    for row in pixels:
        if not is_row_symmetrical(row):
            min_rows_to_remove+=1

    return min_rows_to_remove

def is_row_symmetrical(row):
    """
    Zaczynając od środka, idziemy jednocześnie do lewej i prawej krawędzi. Jak wyznaczyć środek? Mamy parzystą ilość liczb – 320. Zatem środek będą stanowiły dwie liczby: 320/2=160 oraz 159.
    Jeśli elementy po lewej i prawej stronie tablicy są różne, to znaczy że wiersz nie jest symetryczny. W takim wypadku przerywamy pętlę i zwracamy fałsz. Jeśli wszystko nam się zgadza kontynuujemy pętlę i sprawdzamy kolejne elementy. Robimy tak aż do momentu, gdy dotrzemy z jednej strony do początku, a z drugiej do końca wiersza.
    """
    middle_right = COLUMN_NUMBER//2 # 320/2=160
    middle_left = middle_right-1 # 160-1=159

    while (middle_left!=0 and middle_right !=COLUMN_NUMBER):
        if row[middle_right] != row[middle_left]:
            return False
        middle_left -= 1
        middle_right += 1
    return True

"""
Sąsiednie piksele to takie, które leżą obok siebie w tym samym wierszu lub w tej samej
kolumnie. Dwa sąsiednie piksele nazywamy kontrastującymi, jeśli ich wartości różnią się
o więcej niż 128. Podaj liczbę wszystkich takich pikseli, dla których istnieje przynajmniej jeden
kontrastujący z nim sąsiedni piksel.
Dla danych z pliku przyklad.txt wynikiem jest 5. 
"""
def zad3(filepath):
    contrasting = 0
    pixels = get_pixels(filepath=filepath)

    for i in range(ROW_NUMBER):
        for j in range(COLUMN_NUMBER):
            if is_pixel_contrasting(i, j, pixels=pixels):
                contrasting += 1
    return contrasting

def is_pixel_contrasting(x, y, pixels):
    if x != 0:
        if abs(pixels[x][y] - pixels[x-1][y]) > 128:
            return True
    if x != 199:
        if abs(pixels[x][y] - pixels[x + 1][y]) > 128:
            return True
    if y != 319:
        if abs(pixels[x][y] - pixels[x][y+1]) > 128:
            return True
    if y != 0:
        if abs(pixels[x][y] - pixels[x][y-1]) > 128:
            return True
    return False

"""
Podaj długość najdłuższej linii pionowej (czyli ciągu kolejnych pikseli w tej samej kolumnie
obrazka), złożonej z pikseli tej samej jasności. 
"""
def zad4(filepath):
    longest_line_counter = 0
    pixels = get_pixels(filepath=filepath)

    for column in range(COLUMN_NUMBER):
        counter = 1
        max_counter = 0
        for row in range(ROW_NUMBER-1):
            if pixels[row][column] == pixels[row+1][column]:
                counter+=1
            else:
                if counter > max_counter:
                    max_counter = counter
                counter = 1
        if longest_line_counter < max_counter:
            longest_line_counter = max_counter
    return longest_line_counter


results = ""

print("ZADANIE 1")
answer = zad1(przyklad)
print("Przyklad:")
print(f"\tWartość najjaśniejszego piksela : {answer[1]}")
print(f"\tWartość najciemniejszego piksela : {answer[0]}")

answer = zad1(dane)
print("Zadanie:")
print(f"\tWartość najjaśniejszego piksela : {answer[1]}")
print(f"\tWartość najciemniejszego piksela : {answer[0]}")

results += f"1\n{answer[1]} (najjaśniejszy) i {answer[0]} (najciemniejszy)\n\n"

##################################################
print("\nZADANIE 2")
answer = zad2(przyklad)
print("Przyklad:")
print(f"\tOdpowiedź: {answer}")

answer = zad2(dane)
print("Zadanie:")
print(f"\tOdpowiedź: {answer}")

results += f"2\n{answer}\n\n"

##################################################
print("\nZADANIE 3")
answer = zad3(przyklad)
print("Przyklad:")
print(f"\tOdpowiedź: {answer}")

answer = zad3(dane)
print("Zadanie:")
print(f"\tOdpowiedź: {answer}")

results += f"3\n{answer}\n\n"

##################################################
print("\nZADANIE 4")
answer = zad4(przyklad)
print("Przyklad:")
print(f"\tOdpowiedź: {answer}")

answer = zad4(dane)
print("Zadanie:")
print(f"\tOdpowiedź: {answer}")

results += f"4\n{answer}\n\n"


with open('wynik6.txt', 'w') as f:
    f.write(results)