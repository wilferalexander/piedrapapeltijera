#Tuppla opciones
import random  # llamamos la funcion random para eliegir aleatoriamente  para la computadora
options =('piedra', 'papel' , 'tijera')
#crear un ciclo para jugar varias veces

#variable para contar las veces que alguien gana
computer_wins = 0
user_wins = 0
rounds = 1

while  True:
    print('**************BIENVENIDO AL JUEGO DE PIEDRA PAPEL O TIJERA****************')
    print('**************************************************************************')
    print('**************************VAMOS A JUGAR***********************************')
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('LA COMPUTADORA HA GANADO UN TOTAL DE ', computer_wins)
    print('EL USUARIO HA GANADO UN TOTAL DE ', user_wins)
  
          
    user_option = input('Hola tienes 3 opciones Escoge Piedra, papel o tijera......=>')
    user_option = user_option.lower()
  
    
    #Validar la opcion del usuario este dentro de las opciones
    if not  user_option in options:  
      print('Esta opcion no es valida')
      continue
      
    computer_option = random.choice(options)
    
    print('User Option.....=>', user_option)
    print('Computer  option.....=>', computer_option)
    rounds +=1
    
  
    if user_option == computer_option:
      print('Empate!')
    elif user_option == 'piedra':
      if computer_option == 'tijera':
        print('Piedra gana a tijera')
        print('User gana')
        user_wins += 1
      else:
        print('papel gana a piedra')
        print('computer gano')
        computer_wins += 1 
    elif user_option == 'papel':   
        if computer_option == 'piedra':
           print('papel gana a piedra')
           print('User gana')
           user_wins += 1
        else:
          print('tijera gana a papel')
          print('computer gano')
          computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
           print('tijera gana a papel')
           print('User gana')
           user_wins += 1
        else:
          print('piedra gana a tijera')
          print('computer gano')
          computer_wins += 1
  
  
    if computer_wins == 2:
      print('El GANADOR ES LA COMPUTADORA')
      break
  
    if user_wins == 2:
       print('El GANADOR ES EL USUARIO')
       break
      
      
  
  
  
   
    