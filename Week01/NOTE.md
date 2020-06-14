学习笔记及心得
L1：系统学习数据结构和算法
    - 学习->精通领域的三步走方式（from 《异类》）：
        1.Chunk it up 切碎知识点，如庖丁解牛，理解知识点脉络相关
        2.Deliberate Practicing 刻意练习
        3.Feedback 反馈
    - 知识脉络：
        -- 数据结构（三大块）：
            一维数据结构：
                基础：array, linked list
                高级：stack, queue, deque, set, map or hashmap, etc
            二维数据结构:
                基础：tree, graph
                高级：binary search tree(r-b tree, AVL), heap, disjoint set, Trie, etc
            特殊数据结构:
                位运算 Bitwise, BloomFilter
                LRU Cache
        -- 算法（八大点，3+5）：
            【初级】
            branch:
                if-else, switch
            iterration:
                for, while loop
            recursion

            【高级】
            search:
                DFS, BFS, A*, etc
            DP
            Binary Search
            Greedy
            Math, Geometry

    - 刻意练习
        使用覃老师介绍的五毒神掌方法，注重过遍数
        针对弱点练习
        克服不舒服枯燥不爽的情绪，离开舒适区

    - 切题方法（四件套）：
        -- Clarification
            弄清题意！
        -- Possible Solutions
            尽可能多的方法
            compare 比较时间/空间复杂度
            optimal 加强
        -- Coding 多写
        -- Test cases 验证

L2：环境和复杂度
    - 多用Google搜索查询
    - iTerm2 + zsh(oh my zsh)
    - 用leetcode插件
    - 看题目时常看看leetcode国际站解法
    - code style 看看Google Code Style Guide
    - 善用、多用快捷键小操作
    - 上手新IDE时，搜一搜top tips，可以快速学习上手。
    - 自定向下的编程方式：
        先构思总体框架/标题，再补全实现/细节
        先主干，再枝叶
    - 复杂度：
        -- 时间复杂度：Big O Notation
            常见7种，不考虑系数
            O(1), O(logn), O(n), O(n^2), O(n^3), O(2^n), O(n!)
            复杂度从小到大：O(1) < O(logn) < O(n) < O(n^2) < O(2^n) < O(n!)
            递归的时间复杂度：O(k^n)
        -- 主定理 Master Theorem 
            计算分治或递归的时间复杂度
            1、二分查找（一位数组）         O(logn)
            2、二叉树遍历                   O(n)
            3、有序矩阵（二维数组）查找     O(n)
            4、归并排序                     O(n*logn)
        -- 空间复杂度
            使用的空间在于：1、开辟的数组长度；2、递归的深度

L3：数组 链表 跳表
    - 数组array
        存储位置固定
        访问元素快 O(1)
        增加/删除元素较慢 O(n)
    - 链表 Linked List
        数据域，指针域
        访问较慢O(n)，增加/删除...方法快O(1)
    - 跳表 skip list
        用于元素有序的情况
        插入/删除/搜索，都是O(logn)
        优势：原理简单，容易实现，方便扩展，效率高
        针对“平衡二叉树”，“二分查找”
        增加/删除元素时要重建索引，复杂度需要O(logn)
        增加索引需要的空间复杂度增加为：n/2 + n/4 + n/8 + ... --> O(n)
        (Redis、LRU Cache采用)
    - **优化思路：
        升维
        用空间换时间

L4: 栈 队列 优先队列 双端队列
    - 栈（Stack）
        先入后出 Last In - First Out
        push/pop方法
        增/删-->O(1)
        查询-->O(n)  （元素无序）
        [问题中存在最近相关性，形如洋葱，有从内向外或从外向内对称结构时，考虑用栈解决]
    - 队列（Queue）
        先进先出 First In - First Out
        增/删-->O(1)
        查询-->O(n)  （元素无序）
    - 双端队列（Deque）Double-End Queue
        相当于stack和queue的结合
        增/删-->O(1)
        查询-->O(n)  （元素无序）

本周未完成问题总结：
1、周日的每周一题（1300.转变数组后最接近目标值的数组和）只想到了优化的暴力解法，题解中更好的解法还没有吃透理解思路，需要再次实践加强理解。
2、L04-2视频内容只看了第一遍，尚未复习加深理解。
3、本周时间较少，部分题目的相关联问题未刷题加深理解，下周过遍数时需增加刷题量，加深记忆。
