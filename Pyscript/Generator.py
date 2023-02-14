from sizes import sizes as s
import codecs

files_container = { # Здесь прописываются зависимости для каждого файла
  "Несущая пластина":[
      ("Диаметр резьбы редуктора", s["flange_thread_dim_reducer"]),
      ("Глубина резьбы редуктора", s["flange_thread_depth_reducer"]),
      ("Диаметр окружности расположения редуктора", s["flange_thread_D_reducer"]),
      ("Диаметр бурта редуктора", s["flange_collar_dim_reducer"]),
      ("Угл сдвига редуктора", 45),
      
      ("Толщина пластины", s["flange_collar_h_reducer"][0] + 2),
      
      ("Межосевое прижима Вертикаль",  (50, "!!!")),
      ("Межосевое прижима Горизонталь",  (20, "!!!"))
    ],
  
  "Тестовый файл":[
    ("Ебать, русский", s["flange_thread_dim_reducer"])
  ]
  
}

def update_dependencies(): # Функция, создающая новые файлы зависимости
  for file_name in files_container:
    output = codecs.open(f'result/{file_name}.txt','wb',encoding='utf-8-sig')
    try:
      data = ""
      for size in files_container[file_name]:
        data += f'"{size[0]}" = '
        if type(size[1]) == tuple: data += f"{size[1][0]}  '{size[1][1]}\n"
        else:                      data += f"{size[1]}\n"
      output.write(data)
    finally:
      print(file_name+"\n")
      print(data)
      output.close()
    print()
    
if __name__ == "__main__": update_dependencies()