sudo apt install ollama

ollama pull [modelo]

ollama list
NAME                   ID              SIZE      MODIFIED    
qwen2.5-coder:7b       dae161e27b0e    4.7 GB    2 weeks ago    
qwen2.5:3b-instruct    357c53fb659c    1.9 GB    2 weeks ago    
qwen2.5:3b             357c53fb659c    1.9 GB    2 weeks ago

ollama run qwen2.5:3b-instruct "En que año se creo HTML?"
HTML (Hypertext Markup Language) fue creada en 1989 por Tim Berners-Lee y 
se publicó oficialmente en 1991.
