from calculadora import calculadora
from usuario import usuario

calculadora = calculadora()

while True:
    usuario = usuario() 
    usuario.solicitar_datos() 

    resultado = calculadora.calcular(usuario) 
    print(resultado) 
    continuar = input("\n¿Desea realizar otro cálculo? (s/n): ").strip().lower()
    if continuar != "s":
        print("Gracias por usar la calculadora. ¡Hasta pronto!")
        break 