## 斐波那契数列（Fibonacci number）

![Fibonacci](../../img/Fibonacci.jpg)

### 问题描述
斐波那契数列是这样的一个数列：从数列的第三项起，其项所对应的数值等于其相邻前两项之和。

斐波那契数列有两种表示方式，一种是从 1 开始，如：
> 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144，...


另一种是从 0 开始，如：
> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144，... 

特别需要注意的是，上面这种方式中，**0 不是第 1 项，而是第 0 项**。

在数学上，第 n 个斐波那契数用如下公式表示：

$$F_{n}\  =\ F_{n - 1}\ +\ F_{n - 2}$$

针对两种不同的表示方式，满足：
$$F_{1} = 1,\ F_{2} = 1$$
或者
$$F_{0} = 0,\ F_{1} = 1$$


### 编程实现
求出第 n 个斐波那契数。 分别使用**迭代（Iterative）**和**递归（ Recursive）**的方式实现。

### 参考
* [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number)
* [斐波那契数列](https://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97)