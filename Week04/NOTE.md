# 第四周学习笔记和心得
***
## L9 深度优先搜索和广度优先搜索
- 搜索  
    对于搜索，当这种存储数据的数据结构本身没有任何特点时，最普通的搜索就是将每个节点**遍历且仅遍历一遍**，找到搜索的内容，时间复杂度为O(N)。  
    - 每个节点要访问一次
    - 每个节点仅仅访问一次
    - 对于节点的访问顺序不限，例如：
        - 深度优先：depth first search（DFS）
        - 广度优先：breadth first search（BFS）
        - 其他：优先级优先，定义一种估价函数，决定优先级。根据业务场景决定。  
- 深度优先搜索 DFS   
``` 
# 代码模板
# 二叉树
def dfs(node):  
    if node in visited:
    # already visited
        return
    
    visited.add(node)

    # process current node
    # ... # logic here
    dfs(node.left)
    dfs(node.right)

# 多叉树
visited = set()
def dfs(node, visited):
    visited.add(node)
    # process current node
    # ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)

# 非递归写法
# 通过维护一个栈来实现
def DFS(self, tree):
    if tree.root is None:
        return []
    
    visited, stack = [], [tree.root]

    while stack:
        node = stack.pop()
        visited.add(node)

        process(node)
        node = generate_related_nodes(node)
        stack_push(nodes)
    
    # other processing work
```

- 广度优先遍历  BFS
    - 使用**队列**实现  
```
# 代码模板
def BFS(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
    
    # other processing work
```
***

## L10 贪心算法
- 在每一步选择中都进行最有利的选择（最好或最优的选择），从而希望结果是全局最好或最优。
- 贪心算法和动规的区别在于：动规会保存以前的结果，进行比较后选择，有回退功能。而贪心算法只在处理子问题时进行选择，不能回退。
- **贪心算法不一定能够找到全局最优的结果**（鼠目寸光，只顾眼前不顾全局），因此需要根据实际情况进行选择，或运用于某一个处理子问题的方法中。
> **贪心： 当下做局部最优判断  
回溯：能够回退  
动规：最优判断+回退**
- 贪心算法一般用来解决一些最优解问题
- 当一个问题可以通过贪心算法来解决，一般的来说，即是解决这个问题的最好办法。
- 高效、最接近最优解。可以用来辅助解决对结果精确度要求不高的问题。
- 适用场景：  
    可以分解成子问题，子问题的最优解可以递推到最终问题的最优解

**问题选择使用贪心算法的难度在于：要证明贪心算法可以找出全局最优解。  
或者，在经过转化后使用贪心算法，需要巧妙的寻求使用贪心算法的角度。**
***
## L11 二分查找
- 关键的三个前提：
    1. 单调性（目标数据结构需要单调递增或递减）
    2. 存在上下界（bounded）
    3. 能通过索引访问（index accessible）
- 代码模板
```
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
        # find the target
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```
- 可以使用二分查找的理论依据，要明确”关键的三个前提“
- 在使用二分查找实现时，关键要厘清对于target位于左边还是右边，以及判断方式

