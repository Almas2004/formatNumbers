# import pandas as pd

# def format_phone_number(phone_number):
#     # Удаление всех символов, кроме цифр
#     cleaned_number = ''.join(filter(str.isdigit, phone_number))
    
#     # Если номер длинный, удаляем первую цифру
#     if len(cleaned_number) > 10:
#         cleaned_number = cleaned_number[1:]
    
#     # Форматирование номера: добавляем пробелы
#     formatted_number = ' '.join([cleaned_number[:3], cleaned_number[3:6], cleaned_number[6:]])
#     return formatted_number

# # Считываем номера из файла
# with open('phone.txt', 'r', encoding='utf-8') as file:
#     phone_numbers = file.readlines()

# # Удаляем лишние пробелы и символы новой строки
# phone_numbers = [number.strip() for number in phone_numbers]

# # Преобразуем номера в нужный формат и удаляем дубликаты
# unique_phone_numbers = set()

# for number in phone_numbers:
#     formatted_number = format_phone_number(number)
#     unique_phone_numbers.add(formatted_number)

# # Создаем DataFrame из уникальных номеров
# df = pd.DataFrame(unique_phone_numbers, columns=['Phone Number'])

# # Сохраняем DataFrame в Excel
# df.to_excel('phone_numbers.xlsx', index=False)      


from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

def format_phone_number(phone_number):
    # Удаление всех символов, кроме цифр
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    
    # Если номер длинный, удаляем первую цифру
    if len(cleaned_number) > 10:
        cleaned_number = cleaned_number[1:]
    
    # Форматирование номера: добавляем пробелы
    formatted_number = ' '.join([cleaned_number[:3], cleaned_number[3:6], cleaned_number[6:]])
    return formatted_number

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем введенные пользователем номера телефонов из формы
        phone_numbers = request.form['phone_numbers']
        
        # Разбиваем введенные номера на список
        phone_numbers_list = phone_numbers.split('\n')
        
        # Преобразуем номера в нужный формат и удаляем дубликаты
        unique_phone_numbers = set()
        for number in phone_numbers_list:
            formatted_number = format_phone_number(number)
            unique_phone_numbers.add(formatted_number)
        
        # Создаем DataFrame из уникальных номеров
        df = pd.DataFrame(unique_phone_numbers, columns=['Phone Number'])
        
        # Сохраняем DataFrame в Excel
        df.to_excel('phone_numbers.xlsx', index=False)
        
        return render_template('output.html', phone_numbers=unique_phone_numbers)
    
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
