import math

class Visualizer:
    def __init__(self,canvas):
        self.canvas=canvas
        self.node_map={}
        
    def clear(self):
        self.canvas.delete("all")
        self.node_map.clear()
        
    def draw_tree(self,node,x,y,gap):
        if node is None:
            return
        
        r=20
        
        #drawNode
        oval=self.canvas.create_oval(
           x-r, y-r, x+r, y+r,
            fill="skyblue",
            outline="black",
            width=2
        )
        
        self.canvas.create_text(
            x,y,
            text=str(node.data),
            font=("Arial",10,"bold")
        )
        
        self.node_map[node]=oval
        
        if node.left:
            child_x = x - gap
            child_y = y + 80
            self.draw_edge(x,y,child_x,child_y,r)
            self.draw_tree(node.left,child_x,child_y,gap//2)
                     
        if node.right:
            child_x = x + gap
            child_y = y + 80
            self.draw_edge(x,y,child_x,child_y,r)
            self.draw_tree(node.right,child_x,child_y,gap//2)
            
    def draw_edge(self,x1,y1,x2,y2,r):
        angle=math.atan2(y2 - y1,x2 - x1)
               
        start_x = x1 + r * math.cos(angle)
        start_y = y1 + r * math.sin(angle)
        
        end_x = x2 -r * math.cos(angle)
        end_y = y2 - r * math.sin(angle)
        
        self.canvas.create_line(
            start_x,start_y,
            end_x,end_y,
            width=2,
            fill="#444"
        )
        
    def reset_colors(self):
        for node in self.node_map:
            self.canvas.itemconfig(self.node_map[node],fill="skyblue")
            
    def animate(self,root,nodes,output_label,color,index=0):
        if index >= len(nodes):
            return
        
        node = nodes[index]
        
        if node in self.node_map:
            self.canvas.itemconfig(self.node_map[node],fill=color)
            
        output_label.config(text=output_label["text"]+" "+str(node.data))
            
        root.after(700,lambda:self.animate(root,nodes,output_label,color,index+1))