[README_frota.md](https://github.com/user-attachments/files/32532472/README_frota.md)
# TechLog Solutions — Sistema de Gestão de Frota

Sistema em Python para gestão de frota de veículos (caminhões e empilhadeiras), simulando o cadastro de cada veículo e o cálculo do custo operacional de acordo com as características específicas de cada tipo.

## Funcionalidades

- Cadastro de caminhões (com consumo de combustível, distância percorrida e preço do litro)
- Cadastro de empilhadeiras (com capacidade de carga e nível de bateria)
- Validação de código duplicado no cadastro
- Cálculo automático do custo operacional de cada veículo, com regra específica por tipo
- Verificação de status da bateria das empilhadeiras (Normal / Alerta / Crítico)
- Relatórios filtrados: só caminhões, só empilhadeiras, frota completa ou busca por código
- Menu interativo via terminal, com feedback visual (cores e emojis)

## Conceitos praticados

Esse projeto foi minha forma de aprofundar Programação Orientada a Objetos (POO) em Python:

- **Herança**: `Caminhao` e `Empilhadeira` herdam de `Veiculos`, reaproveitando os atributos e comportamentos comuns (código, modelo, custo base) e implementando apenas o que é específico de cada tipo.
- **Sobrescrita de métodos (override)**: cada subclasse implementa sua própria versão de `calcular_custo()`, seguindo sua própria regra de negócio — o caminhão considera distância e consumo de combustível, a empilhadeira considera capacidade de carga.
- **Consistência de assinatura entre subclasses**: inicialmente o método `calcular_custo()` do caminhão exigia parâmetros extras (`distancia`, `preco_litro`) que as outras classes não pediam. Refatorei para que esses valores fossem guardados como atributos do objeto (`self.distancia`, `self.preco_litro`), deixando a assinatura do método igual em todas as classes — o que segue o princípio de que uma subclasse deve poder ser tratada da mesma forma que sua classe-mãe.
- **Uso de `isinstance()`** para diferenciar o comportamento de cada tipo de veículo dentro de uma mesma lista (`frota`), evitando a necessidade de listas separadas por tipo.
- **Encapsulamento**: o nível de bateria da empilhadeira é um atributo protegido (`_nivel_bateria`), acessado por um método (`verificar_status()`) em vez de manipulado diretamente.

## Como executar

```bash
python main.py
```

O programa abre um menu onde é possível cadastrar caminhões, cadastrar empilhadeiras, e visualizar relatórios de custo da frota.

## Tecnologias

- Python 3
- Bibliotecas padrão: `time`, `os`

## Próximos passos

- Persistência de dados (salvar a frota em arquivo, para não perder os cadastros ao fechar o programa)
- Validação mais robusta de entradas numéricas (hoje o programa pode quebrar se o usuário digitar texto onde espera número)
- Histórico de cálculos de custo por veículo, em vez de recalcular a cada consulta
