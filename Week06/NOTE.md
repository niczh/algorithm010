# 第六周学习笔记和心得
***
## L12 动态规划
### 分治、回溯、递归、动态规划的异同
- 本质上没有很大差异
- 动态规划 和 递归或者分治 的差别 关键看有没有最优的子结构
- **共性：重复子问题**
- 感悟
    - 人肉递归很低效、很累
    - 找到最近最简方法，将其拆解成可重复解决的问题
    - 要有数学归纳法思维（抵制人肉递归的诱惑）
    - **本质：寻找重复性-->计算机指令集**
### 动态规划 Dynamic Programming
- Simplifying complicated problem by breaking it down into simple subproblems(in a recursive manner)  
    将复杂问题分解为简单的子问题（用一种递归的方式）
- Divide & Conquer + Optimal substructure  
    分治 + 最优子结构
- 一般要求计算**最优解、最大值、最少的方式**
- 相较于 递归或分治，差异在于有*最优子结构**，中途可以**淘汰**次优解
- 方法：
    - 分析问题，找到重复子问题
    - 通过数学归纳法思维定义DP方程
    - 例如：
        1. 最优子结构 opt[n] = best_of(opt[n-1], opt[n-2])
        2. 存储中间状态：opt[i]
        3. 递推公式（美其名曰：状态转移方程 或 DP方程）  
            Fib：opt[i] = opt[i-1] + opt[i-2]  
            二维路径：opt[i,j] = opt[i+1,j] + opt[i,j+1](且判断a[i,j]是否空地)
### 要点
- 熟记代码模板
- 熟练使用DP方法的三部曲：
    1. subproblem 
    2. DP数组(状态空间) 
    3. DP方程
