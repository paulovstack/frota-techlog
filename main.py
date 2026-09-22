import os
from time import sleep

class Veiculos:
    def __init__(self, codigo: str, modelo: str, custobase: float):
        self.codigo = codigo
        self.modelo = modelo
        self.custobase = custobase

    def calcular_custo(self):
        return self.custobase

class Caminhao(Veiculos):
    def __init__(self, codigo: str, modelo:str, custobase: float, consumo_combustivel: float, distancia: float, preco_litro: float):
        super().__init__(codigo, modelo, custobase)
        self.consumo_combustivel = consumo_combustivel
        self.distancia = distancia
        self.preco_litro = preco_litro
        

    def calcular_custo(self) -> float:
        gasto_combustivel = (self.distancia / self.consumo_combustivel) * self.preco_litro
        custo_total = self.custobase + gasto_combustivel  

        if self.distancia > 500:
            custo_total += 100
        return custo_total

      
class Empilhadeira(Veiculos):
    def __init__(self, codigo: str, modelo: str, custobase: float, bateria: float, nivel_bateria: float):
        super().__init__(codigo, modelo, custobase)
        self.bateria = bateria
        self._nivel_bateria = nivel_bateria

    def calcular_custo(self) -> float:
        custo_total = (self.custobase*1.15) + (5.00 * self.bateria)
        return custo_total

    def verificar_status(self) -> str:
        if  self._nivel_bateria < 15:
            return "\33[1;41;30mCRÍTICO:\33[0m Parada Imediata!"

        elif self._nivel_bateria <= 40:
            return "\33[1;43;30mALERTA:\33[0m Bateria Baixa"

        else:
            return "\33[1;42;39mNORMAL:\033[0m Operação Liberada!"



 

frota = []

while True:
        print("="*30)
        print("   SISTEMA TECHLOG SOLUTIONS   ")
        print("="*30)
        print("\33[33m[1]\33[0m Cadastrar Caminhão")
        print("\33[33m[2]\33[0m Cadastrar Empilhadeira")
        print("\33[33m[3]\33[0m Mostrar Frota e Custos")
        print("\33[33m[0]\33[0m Sair do Sistema")
        print("="*30)
        
        opcao = input("Escolha uma opção: ").strip()
        os.system("cls")

        if opcao == "1":
            print("="*15)
            print(" NOVO CAMINHÃO ")
            print("="*15)
            while True:
               codigo = input("Código do veículo: ").strip()

               existe = False
               for caminhao in frota:
                  if caminhao.codigo == codigo:
                      existe = True
                      break
                   
               if not existe:
                break
               
               else:
                 print("\33[31mEsse código já foi cadastrado, tente outro!\033[0m")
                 sleep(2)
                 os.system("cls")
                 print("="*15)
                 print(" NOVO CAMINHÃO ")
                 print("="*15)
           
            modelo = input("Modelo do veículo: ").strip().upper()
            custobase = float(input("Custo base (R$): "))
            consumo_combustivel = float(input("Qual consumo (km/l): "))
            distancia = 0
            preco_litro = 0

            novo_caminhao = Caminhao(codigo, modelo, custobase, consumo_combustivel, distancia, preco_litro)
            frota.append(novo_caminhao)
            
            os.system("cls")

            print(f"✅ \33[32mCaminhão {modelo} foi cadastrado com sucesso!\33[0m ")
            sleep(3)
            os.system("cls")

        elif opcao == "2":
            print("="*18)
            print(" NOVA EMPILHADEIRA ")
            print("="*18)
            while True:
                codigo = input("Código da empilhadeira: ").strip()
             
                existe = False
                for empilhadeira in frota:
                   if empilhadeira.codigo == codigo:
                    existe = True
                    break 

                if not existe:
                   break
                            
                else:
                    print("\33[31mEsse código já foi cadastrado, tente outro!\033[0m")
                    sleep(2)
                    os.system("cls")
                    print("="*18)
                    print(" NOVA EMPILHADEIRA ")
                    print("="*18)
                        
            modelo = input("Modelo da empilhadeira: ").strip().upper()
            custobase = float(input("Custo base (R$): "))
            bateria = float(input("Capacida de carga (toneladas): "))
            nivel_bateria = float(input("Nível atual da bateria (%): "))
            

            nova_empilhadeira = Empilhadeira(codigo, modelo, custobase, bateria, nivel_bateria)
            frota.append(nova_empilhadeira)
            
            os.system("cls")

            print(f"✅ \033[32mEmpilhadeira {modelo} foi cadastrada com sucesso!\033[0m ")
            sleep(3)
            os.system("cls")

        elif opcao == "3":
            if not frota:
                print("⚠️  Nenhum veículo/empilhadeira foi cadastrado ainda.")
                sleep(3)
                os.system("cls")
                continue

            print("="*8)
            print(" FROTA ")
            print("="*8)
            print("\033[33m[1]\033[0m - Caminhão\n\033[33m[2]\033[0m - Empilhadeira\n\033[33m[3]\033[0m - Todos \n\033[33m[4]\033[0m - Buscar por código\n\033[33m[0]\033[0m - VOLTAR" )

            opcao2 = str(input("Escolha uma opção: ")).strip()
            os.system("cls")

            if opcao2 == "1":
              print("="*22)
              print("RELATÓRIO DE CAMINHÕES")
              print("="*22)
              for veiculo in frota:
                  if isinstance(veiculo, Caminhao):
                        print(f"🚚 Veículo: {veiculo.modelo} [Código: {veiculo.codigo}]")
                        print("🧮 Para calcular o custo do caminhão, informe os dados da rota abaixo ⬇️")
                        print(" ")
                        distancia = float(input(f"🚀 Distância pecorrida por {veiculo.modelo} (km): "))
                        preco = float(input("⛽ Preço do litro de combustível (R$): "))
                        veiculo.distancia = distancia
                        veiculo.preco_litro = preco

                        custo = veiculo.calcular_custo()
                        print(f"💰 Custo operacional: \033[33mR${custo:.2f}\033[0m")
                        print("-"*30)
                        

                  else:
                    continue
                  
              while True:
                 op3 = str(input("Pra sair é só digitar [0]: "))
                 if op3 == "0":
                    os.system("cls")
                    break

            elif opcao2 == "2":
                 print("="*26)
                 print("RELATÓRIO DE EMPILHADEIRAS")
                 print("="*26)
                 for veiculo in frota:
                    if isinstance(veiculo, Empilhadeira):
                        print(f"🚜 Empilhadeira: {veiculo.modelo} [Código: {veiculo.codigo}]")
                        custo = veiculo.calcular_custo()
                        print(f"🔋 Status: {veiculo.verificar_status()}")
                        print(f"💰 Custo operacional: \033[33mR${custo:.2f}\033[0m")
                        print("-"*30)
                       

                    else:
                        continue

                 while True:
                    op3 = str(input("Pra sair é só digitar [0]: "))
                    if op3 == "0":
                        os.system("cls")
                        break

            elif opcao2 == "3":
              print("="*17)
              print("RELATÓRIO TOTAL")
              print("="*17)
              for veiculo in frota:
                    print(f"🚚🚜 Veículo: {veiculo.modelo} [Código: {veiculo.codigo}]")

                    if isinstance(veiculo, Caminhao):                       
                        print("🧮 Para calcular o custo do caminhão, informe os dados da rota abaixo ⬇️")
                        print(" ")
                        distancia = float(input(f"🚀 Distância pecorrida por {veiculo.modelo} (km): "))
                        preco = float(input("⛽ Preço do litro de combustível (R$): "))
                        veiculo.distancia = distancia
                        veiculo.preco_litro = preco
                    
                        custo = veiculo.calcular_custo()
                        print(f"💰 Custo operacional: \033[33mR${custo:.2f}\033[0m")
                        print("-"*30)
                        

                    elif isinstance(veiculo, Empilhadeira):
                        custo = veiculo.calcular_custo()
                        print(f"🔋 Status: {veiculo.verificar_status()}")
                        print(f"💰 Custo operacional: \033[33mR${custo:.2f}\033[0m")
                        print("-"*30)

              while True:
                op3 = str(input("Pra sair é só digitar [0]: "))
                if op3 == "0":
                    os.system("cls")
                    break

            elif opcao2 == "4":
                print("="*17)
                print("BUSCAR POR CÓDIGO")
                print("="*17)
                cod = str(input("Digite o código que deseja buscar: ")).strip()
                encontrado = False


                     
                for veiculo in frota:
                    if veiculo.codigo == cod:
                        encontrado = True

                        print(f"🚚🚜 Veículo: {veiculo.modelo} [Código: {veiculo.codigo}]")

                        if isinstance(veiculo, Caminhao):
                            print("🧮 Para calcular o custo do caminhão, informe os dados da rota abaixo ⬇️")
                            print(" ")
                            distancia = float(input(f"🚀 Distância pecorrida por {veiculo.modelo} (km): "))
                            preco = float(input("⛽ Preço do litro de combustível (R$): "))
                            veiculo.distancia = distancia
                            veiculo.preco_litro = preco
                        
                            custo = veiculo.calcular_custo()
                            print(f"💰 Custo operacional: \033[33mR${custo:.2f}\033[0m")
                            print("-"*30)
                            

                        elif isinstance(veiculo, Empilhadeira):
                            custo = veiculo.calcular_custo()
                            print(f"🔋 Status: {veiculo.verificar_status()}")
                            print(f"💰 Custo operacional: \033[33mR${custo:.2f}\033[0m")
                            print("-"*30)

                        while True:
                          op4 = str(input("Pra sair é só digitar [0]: ")).strip()
                          if op4 == "0":
                              break
                
                if not encontrado:
                        print(f"⚠️\033[31mVeículo com o código '{cod}' não foi encontrado.\033[0m")
                        sleep(2)
                        os.system("cls")

            elif opcao2 == "0":
                continue

            else:
                 print("\n❌ Opção inválida! Tente novamente.")
                 sleep(2)
                 os.system("cls")


        elif opcao =="0":
            print("Encerrando o sistema da TechLog Solutions. Até mais!😀")
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.")
            sleep(2)
            os.system("cls")

        


 