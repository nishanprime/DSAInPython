class Node:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def add(self,val):
        newNode=Node(val)
        if self.root == None:
            self.root=newNode
            return 'Done'
        startingNode=self.root
        while startingNode != None:
            if val <= startingNode.value:
                if startingNode.left != None:
                    startingNode=startingNode.left
                else:
                    startingNode.left=newNode
                    return "Done"
            else:
                if startingNode.right != None:
                    startingNode=startingNode.right
                else:
                    startingNode.right=newNode
                    return "Done"
    def DFSPreOrder(self):
        visited=[]
        current=self.root

        def updateVisited(node):
            if node.value != None:
                visited.append(node.value)

            if node.left != None:

                updateVisited(node.left)
            if node.right != None:
                updateVisited(node.right)
        updateVisited(current)
        return visited
    def InOrder(self):
        visited=[]
        current=self.root
        def updateVisited(node):
            if node.left!= None:
                updateVisited(node.left)
            if node.value != None:
                visited.append(node.value)
            if node.right != None:
                updateVisited(node.right)
        updateVisited(current)
        return visited
    def DFSPostOrder(self):
        visited=[]
        current=self.root
        def updateVisited(node):
            if node.left!= None:
                updateVisited(node.left)

            if node.right != None:
                updateVisited(node.right)
            if node.value != None:
                visited.append(node.value)
        updateVisited(current)
        return visited
    def printLeafNode(self):
        leafNodes=[]
        currentNode=self.root
        def leaf(node):
            if (node.left == None and node.right == None and node.value != None):
                leafNodes.append(node.value)
                return leafNodes
            if node.left != None:
                leaf(node.left)
            if node.right != None:

                leaf(node.right)
        leaf(currentNode)
        return leafNodes



firstBST=BST()
firstBST.add(10)
firstBST.add(9)
firstBST.add(8)
firstBST.add(10)
firstBST.add(12)
# firstBST.add(11)
# firstBST.add(13)

print(firstBST.DFSPreOrder())
print(firstBST.InOrder())
print(firstBST.DFSPostOrder())
print(firstBST.printLeafNode())