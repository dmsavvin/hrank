Consider an array $A = [a_1, a_2, a_3, \dots, a_n]$ and its element $a_i$. Consider some partition of the $A$. $l(i)$ is a length of the element of the partition that includes $a_i$.

$C(i)$ is a sum of $l(i)$ for every partition of $A$, $C_1(i)$ is a sum of $l(i)$ for the partitions of $A$ such that $a_{i-1}$ is the end of some element of the partition, $C_2(i)$ is a sum of $l(i)$ for the partitions of $A$ such that $a_i$ is the beginning of some element of the partition.

$C(i) = C(i-1) - C_1(i) + C_2(i)$

Let's find $C_1(i)$ and $C_2(i)$. First consider the following facts:

$S_1 = \sum\limits_{k = 1}^{\infty}\frac{k}{2^k} = \sum\limits_{k = 1}^{\infty}\frac{1}{2^k} + \frac{1}{2}S_1 = 1 + \frac{1}{2}S_1 \implies S_1 = 2$

$S_m = \sum\limits_{k = m}^{\infty}\frac{k}{2^k} = \frac{2}{2^m} + \frac{1}{2}[S_m + \sum\limits_{k = m}^{\infty}\frac{1}{2^k}] = \frac{2}{2^m} + \frac{1}{2}[S_m + \frac{2}{2^m}] \implies S_m = \frac{m + 1}{2^{m - 1}}$

$s_m = \sum\limits_{k = 1}^{m}\frac{k}{2^k} = S_1 - S_{m + 1} = 2 - \frac{m + 2}{2^m}$

The number of the partitions for the $A$ is $2^{n - 1}$ - the number of ways to place delimiters between A's elements (= number of ways to choose subset from the set with the $n - 1$ elements)

If we require the partition to have the element of the length $k$ than the number of such partitions are either $2^{n - k - 2}$ or $2^{n - k - 1}$ (if the element has the common start or the common end with the $A$).

So

$C_1(i) = \sum\limits_{m = 1}^{i - 1}m \cdot 2^{n - m -2} + (i - 1) \cdot 2^{n - i} = 2^{n - 2}\sum\limits_{m = 1}^{i - 1}\frac{m}{2^m} + (i - 1) \cdot 2^{n - i} = 2^{n - 2}(2 - \frac{i}{2^{i - 2}}) + (i - 1) \cdot 2^{n - i}$

$C_1(i) = 2^{n - 1} - 2^{n - i}$ $~$ for $~$ $i = \overline{1, n - 1}$

$C_2(i) = \sum\limits_{m = 1}^{n - i}m \cdot 2^{n - m - 2} + (n - i + 1) \cdot 2^{n - 1 (n - i + 1)} = \sum\limits_{m = 1}^{n - i} m \cdot 2^{n - m - 2} + (n - i + 1) \cdot 2^ {i - 2} = 2^{n - 2} \sum\limits_{m = 1}^{n - i} \frac{m}{2^m} + (n - i + 1) \cdot 2^{i - 2} = $

$ = 2^{n - 2} [2 - \frac{n - i + 2}{2^{n - i}}] + (n - i + 1) \cdot 2^{i - 2} = 2^{n - 1} - (n - i + 2) \cdot 2^{i - 2} + (n - i + 1) \cdot 2^{i - 2} = 2^{n - 1} - 2^{i - 2}$

$C_2(i) = 2^{n - 1} - 2^{i - 2}$ $~$ for $~$ $i = \overline{2, n}$

$C(1) = \sum\limits_{k = 1}^{n - 1} k \cdot 2^{n - k - 1} + n = 2^{n - 1} \sum\limits_{k = 1}^{n - 1} \frac{k}{2^k} + n = 2^{n - 1}[2 - \frac{n - 1 + 2}{2^{n - 1}}] + n = 2^n - 1$

Finally

$C(i) = C(i-1) + 2^{n - i} - 2^{i - 1}$ $~$ for $~$ $i = \overline {2, n}$

In order to find total values of all possible $B$'s we should calculate

$\sum\limits_{i = 1}^{n}(a_i \cdot C(i))$
