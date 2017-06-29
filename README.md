# GreenWave

Para executar: python main.py
#em alguns casos podera ter de fazer: sudo python main.py

Pacotes necessarios: geopy, serial e RPi.GPIO.

Para defenir o tipo de elemento altere o valor do argumento senderID no main:
 - senderID =0 #ambulancia
 - senderID !=0 #semaforo
 Use um valor diferente para cada semaforo.

 Para mudar de estado basta carregar inserir 1 (+enter) no terminal para ativiar o modo emergencia e 0 (+enter) para
    desativar.
    
 Necessário usar um recetor GPS no dispositivo que simula a ambulancia.

Projeto para a disciplina de Redes Veiculares, no Instituto Superior Tecnico
2016-2017
