# 📘 Assignment: Games in Python

## 🎯 Objetivo

Pratique strings, loops, condicionais, entrada de dados e seleção aleatória em Python. Você vai criar uma versão interativa do jogo da Forca com regras claras para palpites e tentativas.

## 📝 Tarefas

### 🛠️ Implementar o Jogo da Forca

#### Descrição
Implemente um jogo em que o programa escolhe uma palavra aleatória de uma lista predefinida e o jogador tenta adivinhá-la, informando uma letra por vez. Após cada palpite, atualize o progresso e informe quantas tentativas incorretas ainda restam.

#### Requisitos
O programa concluído deve:

- Escolher aleatoriamente uma palavra de uma lista predefinida.
- Começar com 6 tentativas incorretas disponíveis.
- Solicitar um palpite por vez e aceitar letras maiúsculas ou minúsculas sem diferenciar entre elas.
- Exibir a palavra com letras ainda não adivinhadas ocultas, usando o formato `_ _ _`.
- Revelar todas as posições de uma letra quando o palpite estiver correto.
- Reduzir as tentativas restantes apenas quando o palpite for uma letra válida que não esteja na palavra; palpites repetidos não devem reduzir tentativas.
- Informar as tentativas restantes após cada palpite incorreto.
- Encerrar quando todas as letras da palavra forem adivinhadas ou as 6 tentativas incorretas forem usadas.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra escolhida.

Exemplo de progresso para a palavra `gato`, após acertar `a`:

```text
_ a _ _
```
