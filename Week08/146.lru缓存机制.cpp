/*
 * @lc app=leetcode.cn id=146 lang=cpp
 *
 * [146] LRU缓存机制
 */

// @lc code=start
class LRUNode {
public:
    int key, val;
    LRUNode* next;
    LRUNode* prev;
    LRUNode(): key(0), val(0), next(NULL), prev(NULL) {}
    LRUNode(int k, int v): key(k), val(v), next(NULL), prev(NULL) {}
};

class LRUCache {
private:
    unordered_map<int, LRUNode*> cache;
    LRUNode* head;
    LRUNode* tail;
    int size;
    int cap;

    void addToHead(LRUNode* node) {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }

    void removeNode(LRUNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    LRUNode* removeTail() {
        LRUNode* tailNode = tail->prev;
        removeNode(tailNode);
        return tailNode;
    }

public:
    LRUCache(int capacity) : cap(capacity), size(0) {
        head = new LRUNode();
        tail = new LRUNode();
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (!cache.count(key)) {
            return -1;
        }
        LRUNode* node = cache[key];
        // 被访问过，移到头部位置
        removeNode(node);
        addToHead(node);
        return node->val;
    }
    
    void put(int key, int value) {
        // key存在
        if (cache.count(key)) {
            // key存在
            LRUNode* node = cache[key];
            node->val = value;
            removeNode(node);
            addToHead(node);
        } else {
            // key不存在
            LRUNode* node = new LRUNode(key, value);
            if (size == cap) {
                // 容量已满
                LRUNode* deleteNode = removeTail();
                cache.erase(deleteNode->key);
                delete deleteNode;
                --size; 
            }

            cache[key] = node;
            addToHead(node);
            ++size;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end

