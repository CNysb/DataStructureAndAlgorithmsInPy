import random


class SkipListNode:
    def __init__(self, val=None, level=0):
        self.val = val  # 节点值
        self.forward = [None] * (level + 1)  # 每层的下一个节点


class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level  # 最大层数
        self.p = p  # 节点晋升概率
        self.head: SkipListNode = SkipListNode(level=self.max_level)  # 头节点
        self.level = 0  # 当前层数

    def random_level(self):
        """
        随机生成节点的层数
        """
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def search(self, target):
        """
        查找目标值是否存在
        """
        curr = self.head
        for i in range(self.level, -1, -1):  # 从最高层开始查找
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.val == target

    def insert(self, val):
        """
        插入新值
        """
        update = [None] * (self.max_level + 1)  # 记录每层的插入位置
        curr = self.head
        for i in range(self.level, -1, -1):  # 从最高层开始查找插入位置
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if curr is None or curr.val != val:  # 如果值不存在，则插入
            new_level = self.random_level()
            if new_level > self.level:  # 更新跳表的层数
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.head
                self.level = new_level
            new_node = SkipListNode(val, new_level)
            for i in range(new_level + 1):  # 更新每层的指针
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def delete(self, val):
        """
        删除指定值
        """
        update = [None] * (self.max_level + 1)  # 记录每层的删除位置
        curr = self.head
        for i in range(self.level, -1, -1):  # 从最高层开始查找删除位置
            while curr.forward[i] and curr.forward[i].val < val:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if curr is not None and curr.val == val:  # 如果值存在，则删除
            for i in range(self.level + 1):  # 更新每层的指针
                if update[i].forward[i] != curr:
                    break
                update[i].forward[i] = curr.forward[i]
            while (
                self.level > 0 and self.head.forward[self.level] is None
            ):  # 更新跳表的层数
                self.level -= 1

    def __str__(self):
        """
        打印跳表
        """
        result = []
        for i in range(self.level, -1, -1):
            level_str = []
            curr = self.head.forward[i]
            while curr:
                level_str.append(str(curr.val))
                curr = curr.forward[i]
            result.append(f"Level {i}: {' -> '.join(level_str)}")
        return "\n".join(result)


if __name__ == "__main__":
    skip_list = SkipList()
    for val in [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]:
        skip_list.insert(val)
    print("插入后的跳表:")
    print(skip_list)
    print("\n查找 19:", skip_list.search(19))
    print("查找 20:", skip_list.search(20))
    skip_list.delete(19)
    print("\n删除 19 后的跳表:")
    print(skip_list)
