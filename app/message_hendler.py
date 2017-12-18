available_com = ['чай', 'адрес', 'команды']
tees = ['черный', 'зеленый', 'крсаный', 'травяные']


def parse_command(mess):
	command_list = mess.split('.')
	ret_mes = "Набирите 'бот.<команда>'.\nДоступные команды можно посмотреть набрав: 'бот.команды'"
	if command_list[0] == 'бот':
		if len(command_list) == 1:
			return ret_mes
		
		elif command_list[1] == available_com[0]:
			''' tee '''
			return 'Чаи:\n' + '\n'.join(tees)

		elif command_list[1] == available_com[1]:
			"""address"""
			return 'г. Минск, ул. Сурганова 50, ТЦ Рига, 2 этаж, павильон 56'
		
		elif command_list[1] == available_com[2]:				
			sres = ['бот.%s\n' % (word) for word in available_com]
			return  'Доступные команды:\n '+ ''.join(sres)

		elif command_list[1] not in available_com:
			return 'Команда недоступна или неверная команда'	  
		
	else:
	    return ret_mes
		    

