# Внешние бильярды на плоскости Лобачевского

Я написала курсовую работу о внешних бильярдах на третьем курсе матфака НИУ ВШЭ. Работа была довольно творческой, так как мне нужно было самостоятельно исследовать отображение и сформулировать гипотезы (на предыдущих курсах мне давали задачу, а здесь же мне нужно было придумать эту задачу самой).
Я сформулировала 4 гипотезы: одну доказала, почти все остальные гипотезы требуют большего знания теории, поэтому я планирую рассмотреть их на четвёртом курсе.

В курсовой работе я использовала 2 составляющие:
- математику: ТФКП;
- python с библиотекой PIL: для визуализации бильярда.

В файле README.md я расскажу о том, что такое внешний бильярд и в чём заключается главный вопрос моей исследовательской работы. В файле course_work.py код с комментариями, который можно запустить у себя и получить визуализацию бильярда при разных значениях параметров.

<p align="center">

  <img width="400" height="400" src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/pic3.png">

</p>



## Математическое введение

### Диск Пуанкаре.
У геометрии Лобачевского есть несколько моделей. Одна из самых известных и широко использующихся - диск Пуанкаре. В этой модели
- Точки - точки единичного диска |z| < 1;
- Прямые - дуги окружностей, перпендикулярные абсолюту, то есть перпендикулярные окружности |z| = 1 и прямые, проходящие через 0;
- Расстояние...

На рисунке ниже жёлтый круг - диск Пуанкаре. В нём изображён треугольник, проходящий через точки z_1, z_2, z_3. Точка X отражается относительно z_1.

<p align="center">

  <img width="400" height="400" src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/pic1.png">

</p>

Есть два внешних бильярда, которые стоит различать: правый и левый. Если опустить несколько деталей и сказать простым языком, то правый внешний бильярд относительно треугольника $z_1z_2z_3$ -- это отображение, которое отражает точки, лежащие вне треугольника, относительно правой вершины. Например, для точки $X$ правой вершиной является $z_1$, поэтому под действием правого внешнего бильярда $X$ переходит в $g(X)$.

Левый внешний бильярд относительно треугольника определяется аналогично, и под действием этого отображения точка $g(X)$ переходит в точку $X$. Более формальное определение:

### Правый внешний бильярд.
Пусть $K$ -- аффинная плоскость над $\mathbb{R}$ с заданной ориентацией $(K = \mathbb{R}^2, \mathbb{C}, \ldots)$, а $S \subset K$ -- внутренность выпуклого многоугольника и его граница.

Для точки $X \in K \setminus S$ назовём вершину $A$ \emph{правой}, если из точки $X$ проведены прямые через вершины выпуклого многоугольника и ориентированный угол между прямыми $AX$ и $BX$, где $B$ -- любая другая вершина многоугольника, неотрицателен.

Существуют точки $X$, у которых 2 правые вершины $A_1$ и $A_2$, то есть прямые $A_1X$ и $A_2X$ совпадают, а угол между прямой $A_1X$ и $BX$, где $B$ -- вершина многоугольника, отличная от $A_1$ и $A_2$, положителен. Пусть $T$ -- множество точек, у которых 2 правые вершины.

Правый внешний бильярд — отображение 
   g: K \setminus (S \sqcup T) \rightarrow K \setminus S, 
которое отражает точки относительно правой вершины многоугольника. 

Аналогично определяется левый внешний бильярд, с тем отличием, что точки отражаются относительно левой вершины многоугольника, а это такая вершина $A$, для которой ориентированный угол между прямыми $AX$ и $BX$ неположителен, $B$ -- любая другая вершина многоугольника.

<p align="center">

  <img width="400" height="400" src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/pic1.png">

</p>


Рис. 1: В диске Пуанкаре образ точки $X$ под действием правого внешнего бильярда равен $g(X)$; правая вершина треугольника $z_1z_2z_3$ для $X$ -- точка $z_1$. На синих лучах, которые в объединении образуют множество $T$, отображение правого внешнего бильярда не определено.


Меня интересует правый внешний бильярд в диске Пуанкаре (здесь и далее обозначу его за $\mathbb{D}$) и выпуклый многоугольник $S$ — правильный треугольник с центром в нуле. Область определения отображения внешнего бильярда относительно треугольника $z_1z_2z_3$ состоит из трёх областей, в каждой из которых точки отражаются относительно одной из вершин треугольника — $z_1, z_2$ или $z_3$.

Давайте применим отображение $N$ раз, где $N$ -- какое-то большое число. Куда отображаются точки? Существуют ли точки и области, которые с некоторой периодичностью отображаются в себя? Для ответа на этот вопрос

Я исследовала эти вопросы, написав алгоритм на Python. На рисунке ниже изображён диск Пуанкаре жёлтым цветом, треугольник $z_1z_2z_3$ выделен красным цветом, а чёрным цветом отмечены точки, которые под действием правого внешнего бильярда на $N = 1, 2, \dots , 1000 $ итерации отображаются в точки, на которых отображение не определено:

<p align="center">

  <img width="400" height="400" src="https://github.com/IraNovichkova/Outer-Billiards-in-the-Hyperbolic-Plane/blob/main/pic2.png">

</p>



