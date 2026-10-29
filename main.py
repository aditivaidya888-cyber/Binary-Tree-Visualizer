import tkinter as tk
from tkinter import messagebox
from tree import BinaryTree
from visualizer import Visualizer
from utils import parse_input

tree=BinaryTree()

def build_tree():
    values = parse_input(entry.get())
    
    if not values:
        messagebox.showerror("Error","Please enter valid input!")
        return
    
    visualizer.clear()
    output_label.config(text="Building Tree..")
    tree.build_tree_stepwise(values,root,visualizer,output_label)
    
def run_traversal(t_type):
    result=[]
    
    if t_type == "inorder":
        tree.inorder(tree.root,result)
        color="yellow"
        
    elif t_type =="preorder":
        tree.preorder(tree.root,result)
        color="lightgreen"
        
    elif t_type == "postorder":
        tree.postorder(tree.root,result)
        color="salmon"
        
    output_label.config(text="Traversal:")
    visualizer.reset_colors()
    visualizer.animate(root,result,output_label,color)
    
    
root=tk.Tk()
root.title("Binary Tree Visualizer")
root.geometry("900x650")
root.configure(bg="#eefeff")

title=tk.Label(root,text="Binary Tree Visualizer",
               font=("Arial",20,"bold"),bg="#eefeff")
title.pack(pady=10)

frame=tk.Frame(root,bg="#eef6ff")
frame.pack()

entry=tk.Entry(frame,width=35,font=("Arial",12))
entry.pack(side=tk.LEFT,padx=10)

tk.Button(frame,text="Build Tree",
       bg="#007acc",fg="white",
       command=build_tree).pack(side=tk.LEFT)

btn_frame=tk.Frame(root,bg="#eef6ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame,text="Inorder",bg="yellow",
          command=lambda:run_traversal("inorder")).pack(side=tk.LEFT,padx=5)

tk.Button(btn_frame,text="Preorder",bg="lightgreen",
          command=lambda:run_traversal("preorder")).pack(side=tk.LEFT,padx=5)

tk.Button(btn_frame,text="Postorder",bg="salmon",
          command=lambda:run_traversal("postorder")).pack(side=tk.LEFT,padx=5)


canvas=tk.Canvas(root,width=800,height=400,
                 bg="white",highlightthickness=2)
canvas.pack(pady=10)

visualizer = Visualizer(canvas)

output_label=tk.Label(root,text=" ",font=("Arial",14),
                      bg="#eefeff")
output_label.pack(pady=10)

root.mainloop()

               
    
    
    
