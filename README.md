# BUTANTAN GAME 🇧🇷

Um jogo clássico da cobrinha (Snake Game) totalmente customizado e otimizado, 
desenvolvido em Python utilizando a biblioteca **Pygame**. Esta versão traz uma 
roupagem visual inspirada na bandeira do Brasil e diversas melhorias de jogabilidade 
que transformam o clássico arcade em uma experiência moderna, fluida e desafiadora.

## 📝 Resumo do Projeto

O objetivo principal do jogo permanece fiel às raízes: controlar a cobra, coletar 
alimentos (bolinhas azuis) para acumular pontos e crescer o máximo possível sem 
colidir com os limites da tela ou com o próprio corpo. No entanto, o diferencial 
deste projeto está na implementação de uma lógica robusta de estados, otimização 
de controles e um design temático dinâmico que melhora significativamente a 
experiência do usuário (UX).

---

## 🚀 Melhorias e Funcionalidades Implementadas

O jogo evoluiu de um protótipo básico para uma versão com recursos avançados de 
design e código:

### 1. Visual Temático Nacional (Estilo Brasil)
* **Paleta de Cores Harmônica:** O fundo utiliza um tom de verde floresta fosco 
(`34, 139, 34`) cuidadosamente escolhido para não cansar a vista do jogador.
* **Corpo Dinâmico:** Sempre que a cobra consome uma fruta, seu corpo cresce 
alternando os gomos perfeitamente entre **Verde Vibrante** (`0, 255, 0`) e 
**Amarelo** (`255, 255, 0`). A lógica de renderização foi projetada de trás 
para frente para garantir que as cores permaneçam fixas enquanto a cobra se 
move, evitando o efeito de "piscada".
* **Fruta Estilizada:** A fruta assume a cor **Azul** (`0, 0, 255`), completando 
a identidade visual da bandeira nacional.

### 2. Cabeça Guia Destacada
* Para evitar que o jogador se confunda em curvas fechadas quando a cobra estiver 
muito grande, a **cabeça guia** é renderizada de forma independente na cor 
**Branca** (`255, 255, 255`), fornecendo um ponto focal claro de direção.

### 3. Design Moderno (Formas Arredondadas)
* Removendo o aspecto serrilhado de blocos quadrados comuns, tanto a fruta quanto 
os gomos da cobra utilizam a propriedade `border_radius` calculada matematicamente 
com base na metade do tamanho do grid, transformando-os em círculos suavizados.

### 4. Bloqueio de Colisão
* Foi implementada uma trava de segurança na função de leitura dos comandos. Se 
a cobra estiver se movendo para a direita, o comando para a esquerda é sumariamente 
ignorado (e vice-versa para todas as direções). Isso elimina mortes acidentais 
causadas por cliques duplos involuntários no teclado.

### 5. Aceleração Linear Progressiva
* A dificuldade agora é dinâmica. O jogo inicia em um ritmo confortável de 15 FPS. 
A cada fruta azul coletada, a velocidade do relógio interno aumenta em `0.5`, 
exigindo reflexos cada vez rápidos conforme a pontuação sobe.

### 6. Sistema de Reiniciar 
* Ao colidir com as paredes ou com o próprio corpo, o jogo exibe um letreiro 
estilizado de **GAME OVER** em vermelho.
* O loop principal não quebra: ele entra em um estado de espera ativa, 
permitindo que o usuário pressione a tecla **C** para reiniciar instantaneamente 
a partida com os pontos e velocidade resetados, ou **S** para fechar a 
aplicação de forma limpa.

---

## 🎮 Controles

* ⬆️ **Seta para Cima:** Move a cobra para cima (bloqueado se estiver descendo).
* ⬇️ **Seta para Baixo:** Move a cobra para baixo (bloqueado se estiver subindo).
* ➡️ **Seta para a Direita:** Move para a direita (bloqueado se for à esquerda).
* ⬅️ **Seta para a Esquerda:** Move para a esquerda (bloqueado se for à direita).

### Na tela de Game Over (A COBRA FUMOU):
* 🇨 **Tecla C:** Reinicia o jogo imediatamente.
* 🇸 **Tecla S:** Fecha o jogo e o terminal de forma segura.

---

## 📋 Pré-requisitos e Instalação

### Recomendação de Ambiente
Para evitar erros de compilação de código-fonte de pacotes antigos no Windows, 
é altamente recomendado utilizar versões estáveis e consolidadas do Python, 
como o **Python 3.12** ou **3.13**. 

1. Baixe e instale o Python através do site oficial, certificando-se de marcar 
a opção **"Add Python to PATH"**.
2. Abra o terminal do seu projeto no editor (como o PyCharm) e instale a 
biblioteca de jogos:

```bash
pip install pygame