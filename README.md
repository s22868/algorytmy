# Algorytmy

## Tabelka

<hr>

<table>
  <tr>
    <th></th>
    <th>tablica losowych liczb</th>
    <th>tablica posortowanych liczb</th>
    <th>tablica odwrotnie posortowanych liczb</th>
  </tr>
  <tr>
    <td>Heapsort</td>
    <td>2.12961745262146</td>
    <td><b>1.911107063293457</b></td>
    <td>1.9774904251098633</td>
  </tr>
  <tr>
    <td>Quicksort</td>
    <td >6.771024703979492</td>
    <td style="color:red"><b>Limit wywołań rekurencji</b></td>
    <td style="color:red"><b>Limit wywołań rekurencji</b></td>
  </tr>
  <tr>
    <td>Merge-sort</td>
    <td>1.3170526027679443</td>
    <td>1.086014518737793</td>
    <td><b>1.0530023574829102</b></td>
  </tr>
    <tr>
    <td>Counting sort</td>
    <td>0.13400053977966309</td>
    <td><b>0.1200716495513916</b></td>
    <td>0.12500667572021484</td>
  </tr>
</table>

<hr>

## Wnioski

<hr>

Okazało się, że na tablicy <b>300 000</b> elementów należacych do zbioru liczb całkowitych <b>(0..1000)</b> najszybciej poradził sobie algorytm <b>Counting sort</b> co było zgodne z oczekiwaniami a najwolniej poradził sobie <b>Quicksort</b> co już nie było zgodne z oczekiwaniami, myślę że powodem takich wyników, że <b>Merge-sort</b> i <b>Heapsort</b> był szybszy jest wielkość tablicy, Python jak i sam algorytm <b>Quicksort</b> który przy większych tablicach potrzebuje strasznie dużo pamięci oraz bardzo szybko zapełnia stos. Przez co na posortowanych tablicach i odwrotnie posortowanych nie udało się ukończyć działania algorytmu. Jeszcze jednym ciekawym wynikiem jest to, że <b>Merge-sort</b> poradził sobie najlepiej na tablicy odwrotnie posortowanej kiedy logika podpowiada, że najszybciej powinno się to odbyć na już posortowanej tablicy.

<hr>