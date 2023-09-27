import pygame
from constantes import *
from datos import *
from funciones import *

lista_preguntas= listas_filtradas(lista, 'pregunta')
lista_opcion_a= listas_filtradas(lista, 'a')
lista_opcion_b= listas_filtradas(lista, 'b')
lista_opcion_c= listas_filtradas(lista, 'c')
lista_correcta= lista_correcta(lista)

texto_pregunta= " "
pregunta= " "



pygame.init()

screen = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
pygame.display.set_caption('PREGUNTADOS')
fuente_ventana = pygame.font.SysFont(TIPO_FUENTE, TAMAÑO_FUENTE_VENTANA)
fuente_final = pygame.font.SysFont(TIPO_FUENTE, TAMAÑO_FUENTE_FINAL)
fuente_preguntas= pygame.font.SysFont(TIPO_FUENTE,TAMAÑO_FUENTE_PREG)
fuente_boton= pygame.font.SysFont(TIPO_FUENTE,TAMAÑO_FUENTE_BOTON)
score_title = fuente_ventana.render("SCORE", True, COLOR_GRIS)
intentos_title=fuente_ventana.render("INTENTOS", True, COLOR_ROJO)
imagen_titulo = pygame.image.load("titulo.png")
titulo_scale=pygame.transform.scale(imagen_titulo,(282,42))
imagen_preguntados=pygame.image.load("PREGUNTADOS.png")


puntaje= 0
intentos=2
running= True
contador= 0
mostar_respuestas= True
opcion_elegida=""
reiniciar=False
contador_reiniciar=0
game= True

while running:
    lista_eventos=pygame.event.get()
    screen.fill(COLOR_AZUL)
    if game:
        
        score=fuente_ventana.render(str(puntaje), True, COLOR_BLANCO)
        intentos_conteo=fuente_ventana.render(str(intentos), True, COLOR_BLANCO)
        pregunta= lista_preguntas[contador]
        texto_pregunta= fuente_preguntas.render(pregunta, True, COLOR_BLANCO)
        opcion_a=fuente_preguntas.render(lista_opcion_a[contador], True, COLOR_BLANCO)
        opcion_b=fuente_preguntas.render(lista_opcion_b[contador], True, COLOR_BLANCO)
        opcion_c=fuente_preguntas.render(lista_opcion_c[contador], True, COLOR_BLANCO)
        respuesta=fuente_preguntas.render(lista_correcta[contador],True, COLOR_BLANCO)
        correcta=fuente_preguntas.render('RESPUESTA CORRECTA', True, COLOR_VERDE)
        incorrecta=fuente_preguntas.render('RESPUESTA INCORRECTA', True, COLOR_ROJO)

        for evento in lista_eventos:
            
            if evento.type== pygame.QUIT:
                running= False
        
            if evento.type== pygame.MOUSEBUTTONDOWN:
                pos_click= list(evento.pos)
                
                if (pos_click[0]>POS_LEFT_BOTON and pos_click[0]<POS_LEFT_BOTON  +ANCHO_BOTON)and(pos_click[1]>POS_TOP_BOTON and pos_click[1]<POS_TOP_BOTON + ALTO_BOTON):
                    intentos=2
                    mostar_respuestas= True
                    
                    if contador<=len(lista_preguntas)and contador_reiniciar==0:
                        contador+=1
                       
                    if contador<=len(lista_preguntas) and contador_reiniciar>0:
                        contador_reiniciar= contador_reiniciar +1
                        contador=contador_reiniciar
            #-------------------------------------------------
            
            if evento.type== pygame.MOUSEBUTTONDOWN:
                pos_click= list(evento.pos)
                
                if intentos>0:  
                    if (pos_click[0]>POS_LEFT_PREGUNTA and (pos_click[0]<POS_LEFT_PREGUNTA+opcion_a.get_width()))and(pos_click[1]>POS_TOP_RTA_A and (pos_click[1]<POS_TOP_RTA_A + opcion_a.get_height())):
                        opcion_elegida= lista_opcion_a[contador]
                        if opcion_elegida== lista_correcta[contador]:
                            mostar_respuestas= False
                            puntaje= puntaje + 10
                            intentos=2
                        elif(opcion_elegida!=lista_correcta[contador]):
                            intentos= intentos-1
                        
                    elif (pos_click[0]>POS_LEFT_PREGUNTA and (pos_click[0]<POS_LEFT_PREGUNTA+ opcion_b.get_width()))and(pos_click[1]>POS_TOP_RTA_B and (pos_click[1]<POS_TOP_RTA_B + opcion_b.get_height())):
                        opcion_elegida= lista_opcion_b[contador]                        
                        if opcion_elegida== lista_correcta[contador]:
                            mostar_respuestas= False
                            puntaje= puntaje + 10
                            intentos=2
                        elif(opcion_elegida!=lista_correcta[contador]):
                            intentos=intentos-1
                        
                    elif (pos_click[0]>POS_LEFT_PREGUNTA and (pos_click[0]<POS_LEFT_PREGUNTA + opcion_c.get_width()))and(pos_click[1]>POS_TOP_RTA_C and (pos_click[1]<POS_TOP_RTA_C + opcion_c.get_height())):
                        opcion_elegida= lista_opcion_c[contador]
                        if opcion_elegida== lista_correcta[contador]:
                            mostar_respuestas= False
                            puntaje= puntaje + 10
                            intentos=2
                        elif(opcion_elegida!=lista_correcta[contador]):
                            intentos= intentos-1
                     
                if intentos==0:     #aca el if es a propósito porque si se transforma en un numero mayo a 1 dentro del if anterior, necesito que lo analice al salir. Si uso else, lo pasa de largo y analiza recien en el siguiente bucle, lo que me origina un error
                    mostar_respuestas= False

            
                            

            if evento.type== pygame.MOUSEBUTTONDOWN:
                pos_click= list(evento.pos) 
                
                if (pos_click[0]>POS_LEFT_BOTON_REINICIAR and pos_click[0]<POS_LEFT_BOTON_REINICIAR + ANCHO_BOTON)and(pos_click[1]>POS_TOP_BOTON and pos_click[1]<POS_TOP_BOTON + ALTO_BOTON):
                    puntaje=0
                    reiniciar= True
                    contador=contador_reiniciar
                    intentos=2
                    mostar_respuestas= True
                    if reiniciar==True:
                        contador_reiniciar= contador_reiniciar +1

        if contador>= len(lista_preguntas):#NO ES ELIF APROPOSITO, PORQUE SINO DA ERROR YA QUE NO REGISTRA ESTE CLICK EN EL ELSE Y SE ME VA
            game=False

        
        screen.blit(titulo_scale,(POS_LEFT_TITULO,POS_TOP_TITULO))
        screen.blit(score_title, (POS_LEFT_SCORE,POS_TOP_SCORE_TITULO))
        screen.blit(score,(POS_LEFT_SCORE,POS_TOP_SCORE))
        screen.blit(intentos_conteo,(POS_LEFT_SCORE, POS_TOP_INTENTOS))
        screen.blit(intentos_title,(POS_LEFT_SCORE, POS_TOP_TITLE_INTENTOS))
        screen.blit(imagen_preguntados,(POS_LEFT_PREGUNTADOS,POS_TOP_PREGUNTADOS))        
        screen.blit(texto_pregunta, (POS_LEFT_PREGUNTA,POS_TOP_PREGUNTA))
        if mostar_respuestas== True:
            screen.blit(opcion_a, (POS_LEFT_PREGUNTA,POS_TOP_RTA_A)) 
            screen.blit(opcion_b, (POS_LEFT_PREGUNTA,POS_TOP_RTA_B)) 
            screen.blit(opcion_c, (POS_LEFT_PREGUNTA,POS_TOP_RTA_C))
        else: 
            if intentos>0:
                screen.blit(correcta, (POS_LEFT_PREGUNTA,POS_TOP_RTA_B))
            else:
                screen.blit(incorrecta, (POS_LEFT_PREGUNTA,POS_TOP_RTA_B))

        boton_pregunta= pygame.draw.rect(screen, COLOR_AMARILLO, (POS_LEFT_BOTON, POS_TOP_BOTON, ANCHO_BOTON, ALTO_BOTON)) #BOTON PREGUNTA
        boton_siguiente=fuente_boton.render('SIGUIENTE PREGUNTA', True, COLOR_NEGRO)
        texto_siguiente= screen.blit(boton_siguiente, (POS_LEFT_BOTON, POS_TOP_BOTON))
        boton_reiniciar= pygame.draw.rect(screen, COLOR_AMARILLO, (POS_LEFT_BOTON_REINICIAR, POS_TOP_BOTON, ANCHO_BOTON, ALTO_BOTON))
        boton_texto_reiniciar= fuente_boton.render('REINICIAR', True, COLOR_NEGRO)
        texto_reiniciar= screen.blit(boton_texto_reiniciar, (POS_LEFT_BOTON_REINICIAR, POS_TOP_BOTON))
    else:
        for evento in lista_eventos:
            
            if evento.type== pygame.QUIT:
                running= False

            if (evento.type== pygame.MOUSEBUTTONDOWN):
                pos_click= list(evento.pos)
                if ((pos_click[0]>POS_LEFT_SALIDA and pos_click[0]<POS_LEFT_SALIDA + ANCHO_BOTON_SALIDA)and(pos_click[1]>POS_TOP_SALIDA and pos_click[1]<POS_TOP_SALIDA + ALTO_BOTON_SALIDA)):
                    running= False
                elif ((pos_click[0]>POS_LEFT_GAME_REINICIAR and pos_click[0]<POS_LEFT_GAME_REINICIAR + ANCHO_BOTON_SALIDA)and(pos_click[1]>POS_TOP_SALIDA and pos_click[1]<POS_TOP_SALIDA + ALTO_BOTON_SALIDA)):
                    intentos=2
                    contador=0
                    mostar_respuestas=True
                    game=True

        texto_game_over=fuente_final.render('GAME OVER',True, COLOR_AMARILLO)
        screen.blit(texto_game_over,(POS_LEFT_TEXTO_GAME_OVER,POS_TOP_TEXTO_GAME_OVER))        
        puntaje_final= f'Puntaje final: {puntaje}'
        texto_game_over_score=fuente_final.render(puntaje_final,True, COLOR_VERDE)
        screen.blit(imagen_preguntados,(POS_IMG_LEFT_FINAL_PREGUNTADOS,POS_IMG_FINAL_TOP_PREGUNTADOS))
        screen.blit(texto_game_over_score,(POS_LEFT_PUNTAJE_FINAL,POS_TOP_PUNTAJE_FINAL))
        boton_pregunta= pygame.draw.rect(screen, COLOR_AMARILLO, (POS_LEFT_SALIDA,POS_TOP_SALIDA,ANCHO_BOTON_SALIDA,ALTO_BOTON_SALIDA))
        texto_boton_salida=fuente_preguntas.render('SALIR',True, COLOR_NEGRO)
        screen.blit(texto_boton_salida,(POS_LEFT_SALIDA,POS_TOP_SALIDA))
        boton_reiniciar_juego= pygame.draw.rect(screen, COLOR_AMARILLO, (POS_LEFT_GAME_REINICIAR,POS_TOP_SALIDA,ANCHO_BOTON_SALIDA,ALTO_BOTON_SALIDA))
        texto_boton_salida=fuente_preguntas.render('REINCIAR',True, COLOR_NEGRO)
        screen.blit(texto_boton_salida,(POS_LEFT_GAME_REINICIAR,POS_TOP_SALIDA))

    
    pygame.display.flip()
pygame.quit()
