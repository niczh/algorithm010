# 第三周 学习笔记及心得
***
## L7 泛型递归、树的递归
 - 递归代码模板，分四个模块
    1. recursion terminator 递归终结条件
    2. processlogic in current level 处理当前层逻辑  
    3. drill down 下探到下一层  
    4. reverse the current level status if needed 清理当前层
- 思维要点
    1. 不要进行人肉递归（最大误区）  
    2. 找最近重复子问题  
    3. 数学归纳法思维
***
## L8 分治、回溯
- 本质上是递归
- 寻找重复性
    - 最优重复性：采用DP
    - 最近重复性：根据重复性构造分解采用分治、回溯等方法
### 分治
- 划分成多个子问题subproblem：  
    - 向下进行split（切分）  
    - 向上进行merge（合并）  
- 代码模板类似递归的模板：
    - recursion terminator
    - prepare data
    - conquer subproblems
    - process and generate the final result
    - revert the current level states
- 采用分治的关键在于如何拆分子问题
### 回溯
- 是一种试错的思想
- 通过探寻所有可能解，来找出正确的解法
- 判断可能解是否正确，若不正确，在上一步进行一些变化调整，抛弃该可能解。
