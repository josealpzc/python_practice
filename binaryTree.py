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
    myBT.inorderTraversal() 
if __name__ == '__main__':
    
    main()

