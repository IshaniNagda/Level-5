def bToDLL(root):
    if root is None:
        return root
    
    root= BTToDLLUtil(root)
    
    while root.left:
        root= root.left
    
    return root

def BTToDLLUtil(root):
   
    if root is None:
        return root
 
   
    if root.left:
         
        left = BTToDLLUtil(root.left)
 
       
        while left.right:
            left = left.right
 
        left.right = root
         
        root.left = left
 
   
    if root.right:
         
        right = BTToDLLUtil(root.right)
 
        
        while right.left:
            right = right.left
 
       
        right.left = root
         
        
        root.right = right
 
    return root
