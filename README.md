# Внешние бильярды на плоскости Лобачевского

Я написала курсовую работу о внешних бильярдах на третьем курсе матфака НИУ ВШЭ. Работа была довольно творческой, так как мне нужно было самостоятельно исследовать отображение и сформулировать гипотезы (на предыдущих курсах мне давали задачу, а здесь же мне нужно было придумать задачу самостоятельно).
Я сформулировала 4 гипотезы, одну из них доказала. Остальные гипотезы требуют большего знания теории, поэтому я планирую рассмотреть их на четвёртом курсе.

В курсовой работе я использовала 2 составляющие:
- математику: ТФКП;
- python с библиотекой PIL: для визуализации бильярда.

В файле README.md я расскажу о том, что такое внешний бильярд, что нарисовано на изображениях, которые я называю визуализацией бильярда, и в чём заключается главный вопрос моей исследовательской работы. В файле course_work.py код с комментариями, который можно запустить у себя и получить визуализацию бильярда (а также исследовать бильярд, подставляя разные значения параметров).

<p align="center">

  <img width="400" height="400" src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/pic3.png">

</p>



## Математическое введение

### Диск Пуанкаре.



У геометрии Лобачевского есть несколько моделей. Одна из самых известных и широко использующихся - диск Пуанкаре. В этой модели
- Точки — точки единичного диска D = {z ∈ C : |z| < 1}.
- Прямые — диаметры D и дуги окружностей, перпендикулярных
граничной окружности {|z| = 1}; эта последняя называется абсолютом.
- Угол между прямыми определяется как обычный евклидов угол
между двумя окружностями.

На рисунке ниже жёлтый круг - диск Пуанкаре. В нём изображён треугольник с вершинами z_1, z_2, z_3. Точка X отражается относительно z_1.


<p align="center">

  <img width="400" height="400" src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/pic1.png">

</p>

Есть два внешних бильярда, которые стоит различать: правый и левый. Правый внешний бильярд относительно треугольника $z_1z_2z_3$ -- это отображение, которое отражает точки, лежащие вне треугольника, относительно правой вершины. Например, для точки $X$ правой вершиной является $z_1$, поэтому под действием правого внешнего бильярда $X$ переходит в $g(X)$. При этом у точек, лежащих на синих лучах, две правые вершины, поэтому мы считаем, что отображение правого внешнего бильярда на этих точках не определено.

Левый внешний бильярд относительно треугольника определяется аналогично, и под действием этого отображения точка $g(X)$ переходит в точку $X$. На зелёных лучах отражение левого внешнего бильярда не определено.

Более формальное определение бильярда:

### Правый внешний бильярд.
Пусть $K$ -- аффинная плоскость над $\mathbb{R}$ с заданной ориентацией $(K = \mathbb{R}^2, \mathbb{C}, \ldots)$, а $S \subset K$ -- внутренность выпуклого многоугольника и его граница.

Для точки $X \in K \setminus S$ назовём вершину $A$ правой, если из точки $X$ проведены прямые через вершины выпуклого многоугольника и ориентированный угол между прямыми $AX$ и $BX$, где $B$ -- любая другая вершина многоугольника, неотрицателен.

Существуют точки $X$, у которых 2 правые вершины $A_1$ и $A_2$, то есть прямые $A_1X$ и $A_2X$ совпадают, а угол между прямой $A_1X$ и $BX$, где $B$ -- вершина многоугольника, отличная от $A_1$ и $A_2$, положителен. Пусть $T$ -- множество точек, у которых 2 правые вершины.

Правый внешний бильярд — отображение 
   $g: K \setminus (S \sqcup T) \rightarrow K \setminus S$, 
которое отражает точки относительно правой вершины многоугольника. 

Аналогично определяется левый внешний бильярд, с тем отличием, что точки отражаются относительно левой вершины многоугольника, а это такая вершина $A$, для которой ориентированный угол между прямыми $AX$ и $BX$ неположителен, $B$ -- любая другая вершина многоугольника.

<p align="center">

  <img width="400" height="400" src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/pic1.png">

</p>


Рис. 1: В диске Пуанкаре образ точки $X$ под действием правого внешнего бильярда равен $g(X)$; правая вершина треугольника $z_1z_2z_3$ для $X$ -- точка $z_1$. На синих лучах, которые в объединении образуют множество $T$, отображение правого внешнего бильярда не определено.


Меня интересует правый внешний бильярд в диске Пуанкаре (здесь и далее обозначу его за D) и выпуклый многоугольник $S$ — правильный треугольник с центром в нуле. Область определения отображения внешнего бильярда относительно треугольника $z_1z_2z_3$ состоит из трёх областей, в каждой из которых точки отражаются относительно одной из вершин треугольника — $z_1, z_2$ или $z_3$.

Давайте применим отображение $N$ раз, где $N$ - какое-то большое число. Куда отображаются точки? Существуют ли точки и области, которые с некоторой периодичностью отображаются в себя? Я исследовала эти вопросы, написав алгоритм на Python. На рисунке ниже изображён диск Пуанкаре жёлтым цветом, треугольник $z_1z_2z_3$ выделен красным цветом, а чёрным цветом отмечены точки, которые под действием правого внешнего бильярда на $N = 1, 2, \dots , 1000$ итерации отображаются в точки, на которых отображение не определено:

  <p class="thumb">
   <img src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/image_100, r = 75.png" alt="Фотография 1" width="300" height="300" hspace="10" vspace="100">
   <img style="margin:0 300px 0 0;" src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/image_500, r = 75.png" alt="Фотография 2" width="300" height="300" hspace="10" vspace="100">
  </p>


Сверху изображения отличаются количеством итераций. На картинке слева 100 итераций, на картинке справа -- 500. Как видно, изображение с 500 итерациями более детализировано.

  <p class="thumb">
   <img src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/image_1000, r = 100.png" alt="Фотография 1" width="300" height="300" hspace="10" vspace="300">
   <img src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/image_1000, r = 30.png" alt="Фотография 2" width="300" height="300" hspace="10" vspace="300">
  </p>


  <p class="thumb">
   <img src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/image_1000, r = 20.png" alt="Фотография 1" width="300" height="300" hspace="10" vspace="200">
  
   <img src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/image_1000, r = 10.png" alt="Фотография 2" width="300" height="300" hspace="10" vspace="200">
  </p>

</p>


На картинках выше изменяется размер треугольника. Меняя размеры треугольников и количество итераций, я доказала теорему:
- Для отображения правого внешнего бильярда относительно правильного треугольника с центром в нуле и вершинами $z_1 = \varepsilon, z_2 = \varepsilon e^{\frac{2\pi i}{3}}, z_3 = \varepsilon e^{\frac{-2\pi i}{3}}$, таких что $\varepsilon < 2 - \sqrt{3}$, существует цикл длины 3. Точки, образующие цикл, имеют вид
   $z_a = e^{-\frac{\pi i}{3}} a$,
   
   $z_b = e^{\frac{\pi i}{3}} a$,
   
   $z_c = - a$, где $a = \frac{1 + \varepsilon^2 - \sqrt{\varepsilon^4 - 14\varepsilon^2 + 1}}{4\varepsilon}$
   
   если $\varepsilon \geqslant 2 - \sqrt{3}$, то периодических точек с периодом 3 в $\mathbb{D}$ нет.

и сформулировала следующие гипотезы:
- Существуют открытые диски, которые с периодичностью 9 переходят в себя с точностью до поворота, причём центры дисков отображаются в центры и это единственные периодические точки с наименьшим периодом, равным 9;
- Существует бесконечно много периодических областей;
- Объединение периодических областей всюду плотно в диске Пуанкаре.


