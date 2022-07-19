# Vector Algebras
## Notations for Vectors
A vector is an object with an **amplitude** and a **direction**.
向量常見的符號有上面有箭頭的變數 $\vec{A}$ 或者是粗體的變數 $\mathbf{A}$。 

- 分量表示法:
      $\mathbf{A} = A_x \hat{i} + A_y \hat{j} + A_z \hat{k}$
-   $\hat{i}$ 代表 $x$ 方向的單位向量
    $\hat{j}$ 代表 $y$ 方向的單位向量
    $\hat{k}$ 代表 $z$ 方向的單位向量
    有些書使用 $\hat{x}$, $\hat{y}$, $\hat{z}$ 或
    $\hat{e}_x$, $\hat{e}_y$, $\hat{e}_z$ 代表單位向量
-  The amplitude of $\mathbf{A}$ is 

$$|\mathbf{A}| = A = \sqrt{A_x^2+A_y^2+A_z^2} $$ 


## Tensors 

我們也可以用張量的寫法來表示向量。張量可視為更廣義的向量，用來表示更高維的 arrays。沒有 index 的數，我們稱為純量 scalar。有一個index的數稱為向量，例如 $A_\mu$, where $\mu =x,~y,~z$，對應到線性代數就是一個一維的 array，向量也可視為一階張量。有兩個 indices 的量稱為二階張量，寫成 $B_{\mu\nu}$, where $\mu =x,~y,~z$, $\nu =x,~y,~z$, 對應到矩陣。以 index 來表示的好處是，可以表達更高維的量，如 $C_{ijk}$ (張量裡的下標都可以是 $x$, $y$, $z$)。此外，**用 index 表示許多可能性，也可以簡化向量運算**。

常用來當張量 index 的字母有 $\mu$, $\nu$, $i$, $j$, $k$, $l$, $m$, $n$, $\alpha$, $\beta$。 當然也可以用其他字母。 

|      | number of indice | example | name|
| -----| ---- | ---- | ----|
|  零階張量     | 0 | $a$ | scalar 純量|
|  一階張量 | 1 | $A_\mu$ | vector 向量|
|  二階張量 | 2 | $B_{\mu\nu}$ | 張量|
|  三階張量 | 3 | $C_{ijk}$ | 張量|

>所以，當我們寫 $A_\mu$時，這個數就代表一個向量，因為$\mu=x,~y,~z$ 有三種可能性

### Einstein conventions
以張量符號處理線性代數的操作時，例如矩陣相乘，常常會遇到很多求和的情況，需要處理很多summations

$$\sum_{j}A_{ij}B_{jk} $$
$$\sum_{j}\sum_{k}A_{ij}B_{jk}C_{km}$$

就需要寫很多次 $\sum$。為了簡化，我們就使用 Einstein convention

```{prf:definition} Einstein convention
遇到張量相乘時，如果 index 重複出現，則自動視為有 summation，也就是

$$A_{ij}B_{jk}=\sum_{j}A_{ij}B_{jk}$$
$$A_{ij}B_{jk}C_{km}=\sum_{j}\sum_{k}A_{ij}B_{jk}C_{km}$$

```

:::{admonition} Click here!
:class: tip, dropdown
Here's what's inside!
:::

```{exercise}
:class: dropdown
:label: my-exercise
- $\mathbf{A} =(1,2,3)$
$\mathbf{B} =(6,2,5)$

$$A_\mu B_{\mu} =?$$
- $$ C_{ij} = \begin{pmatrix}
4&1&2\\
3&5&6\\
8&2&5
\end{pmatrix}$$

$$C_{ij}A_j=?$$
```