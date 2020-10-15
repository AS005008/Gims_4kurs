from PIL import Image



IMAGE = Image.open('1.bmp')#Изображение на которое будет наложена его копия
PIXEL = IMAGE.load()#Создаю список значений пикселей изображения

IMAGE_SIZE = IMAGE.size#Размер изображения



def resize_image(new_size): #Меняю размер изображения на заданный
	resized_image = IMAGE.resize(resolution)#Устанавливаю новое разрешение для изображения
	resized_image.show()#Вывожу изображение на экран


	return resized_image



def input_coordinates():#Устанавливаю новое разрешение для изображения и координаты для наложения
	coordinates = []#Координата точки с которой начнется наложение
	resolution = []#Новое разрешение изображения

	print('Пример (ширина:320, высота:420)')
	resolution.append(int(input('Введите ширину: ')))
	resolution.append(int(input('Введите высоту: ')))

	resolution = tuple(resolution)#Меняю тип на кортеж
	print()

	print('Пример (x:500, y:500)')
	coordinates.append(int(input('Введите координату x: ')))
	coordinates.append(int(input('Введите координату y: ')))


	return coordinates, resolution




def enter_image(new_image, coordinates):
	size_new_image = new_image.size#Узнаю размер накладываемого изображения
	new_PIXEL = new_image.load()#Создаю список со значениями пикселей накладываемого изображения



	##########################################
	#										 #
	# Накладываю новое изображение на старое #
	#										 #
	##########################################
	for i in range(size_new_image[0]):
		for j in range(size_new_image[1]):
			PIXEL[i + coordinates[0], j + coordinates[1]] = new_PIXEL[i, j]#Замена пикселей


	IMAGE.show()#Вывод на экран
	IMAGE.save('New.bmp')




if __name__ == "__main__":
	coordinates, resolution = input_coordinates()
	new_image = resize_image(resolution)
	enter_image(new_image, coordinates)