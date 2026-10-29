from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self):
        self.root=None
        
    def inorder(self,node,result):
        if node:
          self.inorder(node.left,result)
          result.append(node)
          self.inorder(node.right,result)
          
    def preorder(self,node,result):
        if node:
            result.append(node)
            self.preorder(node.left,result)
            self.preorder(node.right,result)
            
    def postorder(self,node,result):
        if node:
            self.postorder(node.left,result)
            self.postorder(node.right,result)
            result.append(node)
            
    def build_tree_stepwise(self,values,root,visualizer,output_label):
        if not values:
            return
        
        self.root=Node(values[0])
        q=deque([self.root])
        
        visualizer.clear()
        visualizer.draw_tree(self.root,450,70,180)
        output_label.config(text=f"Inserted:{values[0]}")
        
        i=1
        
        def step():
            nonlocal i
            
            if i>=len(values):
                output_label.config(text="tree Created Successfully!")
                return
            
            current=q[0]
            
            if current.left is None:
                current.left=Node(values[i])
                q.append(current.left)
                inserted_value=values[i]
                i+=1
                
            elif current.right is None:
                current.right=Node(values[i])
                q.append(current.right)
                inserted_value=values[i]
                i+=1
                q.popleft()
                
            visualizer.clear()
            visualizer.draw_tree(self.root,450,70,180)
            
            output_label.config(text=f"Inserted:{inserted_value}")
            
            root.after(800,step)
            
        root.after(800,step)