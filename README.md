# GreenWave

Para executar: python main.py
#em alguns casos podera ter de fazer: sudo python main.py

Pacotes necessarios: geopy, seria, RPi.GPIO
RPi.GPIO e uma biblioteca para manipular a GPIO dos Raspberry Pi's.

Para defenir o tipo de elemento altere o valor do argumento senderID no main:
 - senderID =0 #ambulancia
 - senderID !=0 #semaforo
 Use um valor diferente para cada semaforo.

 Para mudar de estado basta carregar inserir 1 (+enter) no terminal para ativiar o modo emergencia e 0 (+enter) para
    desativar.

Projeto para a disciplina de Redes Veiculares, no Instituto Superior Tecnico
2016-2017
