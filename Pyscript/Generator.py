from sizes import sizes as s
import codecs

files_container = { # Здесь прописываются зависимости для каждого файла
  "Несущая пластина":[
      ("flange_thread_dim_reducer", s["flange_thread_dim_reducer"]),
      ("flange_thread_depth_reducer", s["flange_thread_depth_reducer"]),
      ("flange_collar_dim_reducer", s["flange_collar_dim_reducer"]),
    ]
  
}

def update_dependencies(): # Функция, создающая новые файлы зависимости
  for file_name in files_container:
    output = codecs.open(f'result/{file_name}.txt','wb',encoding='utf-8-sig')
    try:
      data = ""
      for size in files_container[file_name]:
        data += f'"{size[0]}" = {size[1][0]}'+f"  '{size[1][1]}\n"
      output.write(data)
    finally:
      print(file_name+"\n")
      print(data)
      output.close()
    print()
    
if __name__ == "__main__": update_dependencies()