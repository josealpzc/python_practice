class BTNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
                
class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def __init__(self):
        self.root = None

    #This function will look for a given value and return True is the node is already included in the BST,
    #and it will return false in case the node is not included in the BST 
    def nodeExist(self,val):
        current = self.root
        while (current != None):

            if(val == current.val):
                return current
            elif (val < current.val):
                current = current.left
            else:
                current = current.right
        return current 

    def delete(self, val):
        #There exist 3 different cases when a deletion is performed in a binary search tree. 
        # 1 - Node has no children
        # 2 - Node has at least one child 
        # 3 - Node has 2 children 
        
        #Case 1 - No children
        node = self.nodeExist(val)
        if(node.left==None and node.right == None):
            print('No children')


    def insert(self, val):
        if self.root:
            current = self.root
            #Compares if given value is greather than the value in current node   
            while current != None:
                
                if (val < current.val):
                    if(current.left):
                        current=current.left
                    else:
                        current.left = BTNode(val)
                        current=None
                else:
                    if(current.right):
                        current=current.right
                    else:
                        current.right = BTNode(val)
                        current=None
        else:
            self.root = BTNode(val)
    
    def inorderTraversal(self):
        self.doInorder(self.root)

    def doInorder(self,root):
        if root:
            self.doInorder(root.left)
            print(root.val)
            self.doInorder(root.right)

    
def main():
    '''
    root = BTNode(10)
    myBTree = BinaryTree(root)
    
    print(myBTree.root.val)
    '''
    myBT = BinaryTree()
    myBT.insert(10)
    myBT.insert(5)
    myBT.insert(15)
    myBT.insert(7)
    myBT.insert(3)
    myBT.inorderTraversal()
    myBT.delete(3)


if __name__ == '__main__':
    
    main()

