# 第七周学习笔记和心得
***
## L13 字典树和并查集
### 字典树 Trie
- 字典树，即Trie树，又称单词查找树或键树，是一种树形结构。
- 典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以被搜索引擎系统用于文本词频统计。
- 优点：最大限度的减少无谓的字符串比较，查询效率比哈希表高。

- 核心思想:
    1. 用空间换时间
    2. 利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。

- 基本性质:
    1. 结点本身不存完整的单词，是多叉树；
    2. 从根节点到某一节点，路径上经过的字符连接起来，为该结点对应的字符串；
    3. 每个结点的所有子结点路径代表的字符都不相同。

### 并查集 DIsjoint Set
- 适用场景：
    - 组团、配对问题
    - Group or not ？
    - 判断两元素是否在一个集合里
- 基本操作：
    - makeSet(s)：新建一个集合，其中包含s个单元素集合。
    - unionSet(x, y)：把元素x和y所在的集合合并，要求x和用所在的集合不相交，如果相交则不合并。
    - find(x)：找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下即可。
- 代码模板：
    ```
    # Python
    def init(p): 
        # for i = 0 .. n: p[i] = i; 
        p = [i for i in range(n)] 
    
    def union(self, p, i, j): 
        p1 = self.parent(p, i) 
        p2 = self.parent(p, j) 
        p[p1] = p2 
    
    def parent(self, p, i): 
        root = i 
        while p[root] != root: 
            root = p[root] 
        while p[i] != i: # 路径压缩 ?
            x = i; i = p[i]; p[x] = root 
        return root
    ```
    ```
    // C/C++
    class UnionFind {
    public:
        UnionFind(vector<vector<char>>& grid) {
            count = 0;
            int m = grid.size();
            int n = grid[0].size();
            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (grid[i][j] == '1') {
                        parent.push_back(i * n + j);
                        ++count;
                    }
                    else {
                        parent.push_back(-1);
                    }
                    rank.push_back(0);
                }
            }
        }

        //递归
        int find(int i) {
            if (parent[i] != i) {
                parent[i] = find(parent[i]);
            }
            return parent[i];
        }

        void unite(int x, int y) {
            int rootx = find(x);
            int rooty = find(y);
            if (rootx != rooty) {
                if (rank[rootx] < rank[rooty]) {
                    swap(rootx, rooty);
                }
                parent[rooty] = rootx;
                if (rank[rootx] == rank[rooty]) rank[rootx] += 1;
                --count;
            }
        }

        int getCount() const {
            return count;
        }

    private:
        vector<int> parent;
        vector<int> rank;
        int count;
    };
    ```

***
## L14 高级搜索
### 初级搜索
1. 朴素搜索
2. 优化方式：不重复、剪枝
3. 搜索方向：DFS、BFS  
### 剪枝
- 搜索状态树时，发现当前分枝已经处理过、或者不够好时，减去当前分枝，以提高搜索效率。

### 双向BFS Two-ended BFS
- 从起始点和终点同时进行BFS，直至相遇，双向的扩散层数和即为最小步数。
- 细节技巧：互换front和back，先扩散结点数比较小的一端

### 启发式搜索 Heuristic Search (A*)
- 通过优先级不断搜索，先搜索优先级高的
- 估价函数：  
    启发式函数：h(n), 用来评价哪些结点最有希望是一个我们要找的结点。h(n)会返回一个非负实数，也可以认为是从结点n到目标结点路径的估计成本  
    启发式函数是一种告知搜索方向的方法。提供了一种明智的方法来猜测哪个邻居结点会导向目标结点。
- 由于估价函数的存在，使扩散变得有思考性
- 代码模板
    ```
    # Python
    def AstarSearch(graph, start, end):
        pq = collections.priority_queue() # 优先级 —> 估价函数
        pq.append([start]) 
        visited.add(start)

        while pq: 
            node = pq.pop() # can we add more intelligence here ?
            visited.add(node)

            process(node) 
            nodes = generate_related_nodes(node) 
        unvisited = [node for node in nodes if node not in visited]
            pq.push(unvisited)
    ```
***
## L15 AVL树和红黑树
- 二叉搜索树BST在极端情况下会退化成一根棍子，即所有结点在一侧。为了保证搜索效率，要保持树的维度，让左右子树的结点平衡（recursively）。**balance**
- 平衡二叉树，包括：AVL、红黑树、2-3树、B树、Treap、Splay 。。。
### AVL树
- 平衡因子 Balance Factor  
    左子树的高度减去右子树的**高度**(有时相反)  
    balance factor = {-1, 0, 1}
- AVL树的所有结点的平衡因子∈ {-1, 0, 1} 
- 新增、删除结点后，通过四种旋转操作来修正**平衡因子绝对值超过1**的结点，保持树的平衡：
    1. 左旋：  
        右右子树A-B-C（B是A的右儿子、C是B的右儿子、A失衡)，向左旋转，结点A成为结点B的左儿子
    2. 右旋：  
        左左子树A-B-C（B是A的左儿子、C是B的左儿子、A失衡)，向右旋转，结点A成为结点B的右儿子
    3. 左右旋：    
        左右子树A-B-C（B是A的左儿子、C是B的右儿子、A失衡)，先左旋，B成为C的左儿子，C成为A的左儿子（成为了A-C-B的左左子树情况）；再右旋一次，让A成为C的右儿子
    4. 右左旋：    
        右左子树A-B-C（B是A的右儿子、C是B的左儿子、A失衡)，先右旋，B成为C的右儿子，C成为A的右儿子（成为了A-C-B的右右子树情况）；再左旋一次，让A成为C的左儿子
    **左旋或右旋时，旋转结点原本携带的儿子结点中，夹在旋转结点间的儿子结点，要更换父节点。例如右旋时，pivot结点的右儿子，在旋转后成为原root结点的左儿子，原root结点成为pivot结点的右儿子**
- 不足：
    - 结点要存储额外信息：balance factor
    - 调整次数频繁
### 红黑树 Red-Black Tree
- **近似平衡二叉树**
- 是一种**近似平衡**的BST，确保任何一个结点的左右子树的**高度差小于两倍**（大的最多是小的两倍），满足如下条件：
    - 每个节点要么红色，要么是黑色
    - 根结点是黑色
    - 每个叶子结点(NIL结点，空结点)是黑色
    - 不能有相邻的两个红色结点
    - 从任意结点到其每个叶子结点的所有路径都包含相同数目的黑色结点
- 从根到叶子最长的可能路径不多于最短的可能路径的两倍长
### AVL树和红黑树的对比
- AVL trees provide ***faster lookups*** than Red Black Trees because they are more **strictly balanced**.  
    AVL树有更快的搜索速度，因为AVL树更加严格平衡。
- Red Black Trees provide ***faster insertion and removal*** operations than AVL trees as fewer rotations are done due to relatively relaxed balancing.  
    红黑树提供了更快的插入/删除操作，因为相对较少的旋转操作。
- AVL trees store ***balance factors or heights*** with each node, thus requires storage for an integer per node whereas Red Black Tree requires only 1 bit of information per node.  
    AVL树需要更多的存储空间用于保存各个结点的平衡因子或高度，而红黑树只需要1bit记录结点颜色。
- Red Black Trees are used in most of the language libraries
like map, multimap, multiset in C++ whereas AVL trees are used in databases where faster retrievals are required.  
    红黑树常用于大多数的语言库，例如C++中的map、multimap、multiset；而AVL树常用于数据库，因为需要更快的数据检索。
- 读操作多、插入/删除少的时候用AVL。插入/删除操作比较多的话，用红黑树。
***