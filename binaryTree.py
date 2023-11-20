class BTNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
                
class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.size = 0 
    
    def __init__(self):
        self.root = None
        self.size = 0 

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
        #'current' will be use to go through the BST elements in order to find the value of the node to be removed,
        #in case the value is not found within the BST node, we return -1

        current = self.root # we start looking at root
        
               
        #Verify the BST is not empty
        if self.size > 0:
            #Verify the node to remove is not root
            if(current.val == val):
                self.size=0
                a=self.root
                self.root = None
                return a
            else:
                #Find the node to eliminate 
                while current != None:
                    if(current.val > val):
                        parentNode = current
                        current = current.left
                    elif (current.val < val):
                        parentNode = current
                        current = current.right
                    else:
                        #tmp will point to the node to remove
                        tmp = current
                        current = None

                print(f"parent : {parentNode.val}")
            
            if (tmp!=None):
                print(f"Node to remove is {tmp.val}")
                #Now lets see if node to remove has no children, 1 left/right child, or both (left, and right).
                #Node has 2 children
                if(tmp.left and tmp.right):
                    parent2 = tmp
                    predecesor = parent2.left
                    
                    while(predecesor.right!=None):
                        parent2 = predecesor
                        predecesor = predecesor.right

                    print(f"parent: {parent2.val}")
                    print(f"predecesor : {predecesor.val}")

                    tmp.val = predecesor.val
                    parent2.right = None

                #Node has left child
                elif(tmp.left!=None and tmp.right==None):
                    parentNode.left=tmp.left
                    self.size-=1
                #Node has right child
                elif(tmp.left==None and tmp.right!=None):
                    parentNode.right=tmp.right
                    self.size-=1
                #Node has not children
                else:
                    print(f'Node: {tmp.val} has no children')
                    if (tmp.val < parentNode.val):
                        parentNode.left = None
                    else:
                        parentNode.right = None

                    self.size-=1
            else:
                print(f"Value: {val} does not exist in the BST")
                return 1
            
        else:
            print('You cannot remove from an empty BST')
            return -1


    def printSize(self):
        print (self.size)

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
        self.size+=1

    def inorderTraversal(self):
        if(self.size!=0):
            return self.doInorder(self.root)
        #else:
         #   print('BST is empty')


    def doInorder(self,root):
        res = []
        if root:
            res = self.doInorder(root.left)
            res.append(root.val)
            res = res + self.doInorder(root.right)
        return res
    
def main():
    '''
    root = BTNode(10)
    myBTree = BinaryTree(root)
    
    print(myBTree.root.val)
    '''
    #Do Basic testing for adding and removing root
    myBT = BinaryTree()    #Creating myBT object of type BinaryTree()
    a=myBT.delete(10)      #Trying to Delete an unexisting number
    print(f"a:{a}")        #Print the return value of above call to delete method
    myBT.insert(10)        #Insert 10 as a root 
    b=myBT.delete(10)      #Call delete function again
    print(f"b:{b}")        #print the return value of above call to delete method
    print("Inorder")
    myBT.inorderTraversal()
    print("*****")

    #Now lets create a bigger three
    """
                        10   <--- root
                       /  \
                      5    15
                     / \    \
                    3   7   16
                   /
                  1
    """
    myBT.insert(10) 
    myBT.insert(5)
    myBT.insert(15)         
    myBT.insert(7)
    myBT.insert(3)
    myBT.insert(16)
    myBT.insert(1)
    myBT.insert(4)
    #myBT.delete(3)
    print(myBT.inorderTraversal())
    myBT.delete(5)
    print(myBT.inorderTraversal())

if __name__ == '__main__':
    
    main()

