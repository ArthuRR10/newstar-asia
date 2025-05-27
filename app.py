from flask import Flask, jsonify
from threading import Thread
import random

app = Flask(__name__)

nomes = [ "Hiroshi", "Sakura", "Ravi", "Mei", "Jin", "Aiko", "Arun", "Sang", 
    "Yuna", "Haruto", "Ananya", "Chen", "Min", "Takeshi", "Lakshmi", "Bao", 
    "Ayaka", "Dae", "Kazuki", "Kiran", "Linh", "Jiro", "Tariq", "Yuki", 
    "Sora", "Priya", "Akira", "Natsumi", "Tanaka", "Indira", "Hyun", "Wei", 
    "Manoj", "Asuka", "Naoki", "Isha", "Ryota", "Huan", "Kyung", "Sayuri" ]

sobrenomes = [ "Tanaka", "Kim", "Singh", "Chen", "Yamamoto", "Patel", "Nguyen", "Park", 
    "Khan", "Takahashi", "Zhang", "Sharma", "Kobayashi", "Choudhury", "Lin", 
    "Matsumoto", "Ali", "Reddy", "Fujimoto", "Thapa", "Sato", "Gupta", 
    "Hashimoto", "Hoang", "Imamura", "Das", "Chang", "Oh", "Murakami", 
    "Rahman", "Ito", "Tran", "Narayan", "Han", "Abe", "Jain", "Wang", 
    "Choi", "Rajput", "Ueda" ]

nacionalidades = [
    ("🇯🇵 Japão", 4), ("🇰🇷 Coreia do Sul", 4), ("🇮🇳 Índia", 4), ("🇻🇳 Vietnã", 3),
    ("🇨🇳 China", 3), ("🇮🇩 Indonésia", 2), ("🇲🇾 Malásia", 2), ("🇹🇭 Tailândia", 2),
    ("🇵🇰 Paquistão", 1), ("🇸🇬 Singapura", 1), ("🇮🇷 Irã", 2), ("🇺🇿 Uzbequistão", 1),
    ("🇶🇦 Catar", 1), ("🇸🇦 Arábia Saudita", 1)]

posicoes = ["Goleiro", "Zagueiro", "Lateral Direito", "Lateral Esquerdo", "Volante", "Meia Central", "Meia Ofensivo",
            "Ponta Direita", "Ponta Esquerda", "Centroavante"]

comparacoes = [ "Daichi Kamada", "Hwang In-beom", "Takuma Asano", "Alireza Jahanbakhsh",
    "Wu Lei", "Mehdi Taremi", "Takefusa Kubo", "Salem Al-Dawsari",
    "Son Jun-ho", "Sardar Azmoun", "Kwon Chang-hoon", "Ali Gholizadeh",
    "Shoya Nakajima", "Eldor Shomurodov" ]

capacidade_atual = [
    "Reserva na National League", "Titular na National League", "Reserva na League Two", 
    "Titular na League Two", "Reserva na League One", "Titular na League One"
]

capacidade_potencial = [
    "Reserva na League Two", "Titular na League Two", "Reserva na League One", 
    "Titular na League One", "Reserva na Championship", "Reserva na NLEDF", 
    "Titular na Championship", "Titular na NLEDF"
]

estrelas_pesos = [(2, 10), (3, 25), (4, 40), (5, 25)]

@app.route('/')
def gerar_jogador():
    nome = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    nacionalidade = random.choices(nacionalidades, weights=[n[1] for n in nacionalidades])[0][0]
    posicao = random.choice(posicoes)
    comparacao = random.choice(comparacoes)
    atual = random.choice(capacidade_atual)
    potencial = random.choice(capacidade_potencial)
    estrelas = random.choices([e[0] for e in estrelas_pesos], weights=[e[1] for e in estrelas_pesos])[0]
    estrelas_txt = "<:sstar:1214063700886036532>" * estrelas

    return jsonify({
        "nome": nome,
        "nacionalidade": nacionalidade,
        "posicao": posicao,
        "comparacao": comparacao,
        "cap_atual": atual,
        "cap_potencial": potencial,
        "estrelas": estrelas_txt 
    })

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    run()
