

# solution (AC)
class Codec:

    def serialize(self, root: TreeNode) -> str:
        # preorder encoding
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        res = ' '.join(map(str, vals))
        return res
        

    def deserialize(self, data: str) -> TreeNode:
        # preorder decoding
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))