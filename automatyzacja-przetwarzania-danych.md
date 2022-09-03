# Automatyzacja przetwarzania danych

## Cel
Celem wyzwania jest sprawdzenie umiejętności automatyzacji przetwarzania danych z wykorzystaniem dockerów.

##  Opis zadania
1. Stwórz skrypt wykonywalny w pythonie z przetwarzaniem opisu COCO do dataframe i zapisujący dane do formatu csv.
    - argumentem wejściowym do skryptu ma być link do opisu danych w formacie COCO i ścieżka do pliku gdzie skrypt ma zapisać przekształcone dane;
    - pobierz dane i wypakuj z podanego linku;
    - wczytaj wypakowane dane (plik person_keypoints_val2017.json);
    - przekształć dane do dataframe:
        - każdy wiersz w dataframe ma być osobną obwiednią obiektu (bounding box) na zdjęciu, wszystkie opisy mają być w jednym dataframe;
        - kolumny w dataframe: label, image_name, image_width, image_height, x_min, y_min, x_max, y_max, image_url;
        - kolumna label ma zawierać nazwę klasy danej obwiedni obiektu;
        - kolumna image_name ma zwierać nazwę zdjęcia;
        - kolumna image_width ma zwierać szerokość zdjęcia w pikselach;
        - kolumna image_height ma zwierać wysokość zdjęcia w pikselach;
        - kolumna x_min ma zwierać pozycję lewej krawędzi obwiedni obiektu w pikselach;
        - kolumna y_min ma zwierać pozycję górnej krawędzi obwiedni obiektu w pikselach;
        - kolumna x_max ma zwierać pozycję prawej krawędzi obwiedni obiektu w pikselach;
        - kolumna y_max ma zwierać pozycję dolnej krawędzi obwiedni obiektu w pikselach;
        - kolumna image_url ma zwierać adres URL zdjęcia (pole coco_url);
    - przekształcone dane zapisz do formatu csv;
    - zadbaj o prawidłowy shebang;
    - zapisz komendę uruchamiającą skrypt;
2. Stwórz plik requirements w którym będą pakiety i ich wersje wymagane do poprawnego działania skryptu.
3. Stwórz plik dockerfile tworzący obraz zawierający powyższy skrypt.
    - wykorzystaj obraz pythona 3;
    - zaktualizuj pip, setuptools i wheel w obrazie (ewentualnie wskaż wersję tych pakietów wymaganych do poprawnego działania skryptu);
    - zainstaluj pakiety z pliku requirements;
    - skopiuj skrypt do poprawnego katalogu w obrazu;
    - wybuduj obraz z dockerfile;
    - sprawdź czy kontener uruchomiony z obrazu działa prawidłowo;
    - zapisz komendę budującą obraz i uruchamiającą kontener;

Dane wejściowe dla skryptu do przekształcenia:
    http://images.cocodataset.org/annotations/annotations_trainval2017.zip

## Wynik
Do oceny prześlij nastepujące pliki:
- skrypt pythonowy
- plik dockerfile
- plik tekstowy ze spisem komend wymienionych w zadaniu

## Przydatne linki
[COCO data format](https://cocodataset.org/#format-data)  
[Pandas](https://pandas.pydata.org/docs/)  
[Skrypty Pythonowe](https://betterprogramming.pub/write-better-python-scripts-ce58c1ebf690)  
[Dockerfile](https://docs.docker.com/engine/reference/builder/)  
[Docker Build](https://docs.docker.com/engine/reference/commandline/build/)  
[Docker Run](https://docs.docker.com/engine/reference/run/)  