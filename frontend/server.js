const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000; // O Node roda na 3000, o Python na 8000

// Configurações
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

// Rota 1: Tela de Login (A primeira coisa que aparece)
app.get('/', (req, res) => {
    res.render('login', { erro: null });
});

// Rota 2: Processar o Login e buscar dados no Python
app.post('/dashboard', async (req, res) => {
    const chaveMestra = req.body.chave;

    try {
        // O Node vai bater na porta do Python (8000)
        // Note que estamos passando a chave no HEADER, igual no Swagger
        const response = await axios.get('http://localhost:8000/secrets', {
            headers: {
                'x-master-key': chaveMestra
            }
        });

        // Se deu certo, renderiza a página index com os segredos e manda a chave junto
        // (para podermos usar ela depois para ver as senhas)
        res.render('index', { 
            segredos: response.data.secrets, 
            chave: chaveMestra 
        });

    } catch (error) {
        // Se a chave for errada ou o Python estiver desligado
        console.error("Erro ao conectar:", error.message);
        res.render('login', { erro: "Chave inválida ou API Python desligada!" });
    }
});

app.listen(PORT, () => {
    console.log(`Frontend rodando em http://localhost:${PORT}`);
});