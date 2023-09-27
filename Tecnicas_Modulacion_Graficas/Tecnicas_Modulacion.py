import matplotlib.pyplot as plt
from tkinter import messagebox

def binary_to_pulses(binary_string):
    # Convertimos la cadena binaria en una lista de enteros
    binary_list = [int(bit) for bit in binary_string]
    
    # listas para cada técnica de modulación
    do_list = []
    rz_list = []
    nrz_list = []
    ami_list = []
    pseudo_list = []
    manchester_list = []

    # Iterar sobre la lista binaria
    for bit in binary_list:
        # Dato digital
        if bit == 0:
            do_list.append(0)

        else:
            do_list.append(1)
        # RZ
        if bit == 0:
            rz_list.extend([-1, -1, 0, 0])
        else:
            rz_list.extend([1, 1, 0, 0])
        # NRZ
        if bit == 0:
            nrz_list.append(-1)
        else:
            nrz_list.append(1)
        # AMI
        if bit == 0:
            ami_list.append (0)
        else:
            ami_list.append(1 if len([b for b in ami_list if b != 0]) % 2 == 0 else -1)
        # Pseudoternario
        if bit == 0: 
            pseudo_list.append(1 if len([b for b in pseudo_list if b != 0]) % 2 == 0 else -1)
        else:
            pseudo_list.append(0)        
        
        # Manchester
        if bit == 0:
            manchester_list += [1,-1]
        else:
            manchester_list += [-1,1]
    
    # Crear las gráficas
    fig, axs = plt.subplots(6, 1, figsize=(12, 16))
    fig.suptitle('Códigos de línea', fontsize=20)

    axs[0].step(range(len(do_list)), do_list, where='post')
    axs[0].set_title('Dato Digital')
    axs[0].set_ylim(-1.5, 1.5)

    axs[1].step(range(len(rz_list)), rz_list, where='post')
    axs[1].set_title('RZ')
    axs[1].set_ylim(-1.5, 1.5)
    
    axs[2].step(range(len(nrz_list)), nrz_list, where='post')
    axs[2].set_title('NRZ')
    axs[2].set_ylim(-1.5, 1.5)
    
    axs[3].step(range(len(ami_list)), ami_list, where='post')
    axs[3].set_title('AMI')
    axs[3].set_ylim(-1.5, 1.5)
    
    axs[4].step(range(len(pseudo_list)), pseudo_list, where='post')
    axs[4].set_title('Pseudoternario')
    axs[4].set_ylim(-1.5, 1.5)
    
    axs[5].step(range(len(manchester_list)), manchester_list, where='post')
    axs[5].set_title('Manchester')
    axs[5].set_ylim(-1.5, 1.5)
    

    plt.subplots_adjust(hspace=1.0)
    # Mostrar las gráficas
    plt.show()

while True:

    # Pedir al usuario que introduzca un número binario
    binary_input = input("Introduce un número binario: ")
    if not all(c in "01" for c in binary_input): #Verifica si el usuario introducio numeros binarios
        messagebox.showerror("Error", "El valor introducido no es un número binario válido") #Si es así, entra al if y ejecuta una notificación de error
    else:
        # Si no lo es, Llama a la función para generar las gráficas
        binary_to_pulses(binary_input) 

    #Preguntar si desea continuar
    continuar = input("¿Deseas seguir graficando (s|n) ").upper()
    #Presiona n, termina el programa
    if continuar == 'N':
        messagebox.showinfo("","Gracias por usar el programa :)")
        break
