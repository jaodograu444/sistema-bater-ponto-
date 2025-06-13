document.getElementById('form-horario').addEventListener('submit', function (event) {
    event.preventDefault();

    // Pegando os dados do formulário
    const funcionario = document.getElementById('funcionario').value;
    const data = document.getElementById('data').value;
    const entrada = document.getElementById('entrada').value;
    const saida = document.getElementById('saida').value;
    const intervalo = document.getElementById('intervalo').value || '0';

    // Debug: Verificar se os dados foram capturados corretamente
    console.log(`Funcionário: ${funcionario}`);
    console.log(`Data: ${data}`);
    console.log(`Entrada: ${entrada}`);
    console.log(`Saída: ${saida}`);
    console.log(`Intervalo: ${intervalo}`);

    // Calculando o total de horas
    const entradaH = parseInt(entrada.split(':')[0]);
    const entradaM = parseInt(entrada.split(':')[1]);
    const saidaH = parseInt(saida.split(':')[0]);
    const saidaM = parseInt(saida.split(':')[1]);

    // Calcular diferença de horas e minutos
    let horasTrabalhadas = (saidaH - entradaH);
    let minutosTrabalhados = (saidaM - entradaM);

    // Ajustar a hora se o minuto for negativo
    if (minutosTrabalhados < 0) {
        horasTrabalhadas -= 1;
        minutosTrabalhados += 60;
    }

    // Converter minutos para horas decimais
    const totalHoras = horasTrabalhadas + (minutosTrabalhados / 60) - parseFloat(intervalo);

    // Criando uma nova linha na tabela
    const tabela = document.getElementById('tabela-horarios').getElementsByTagName('tbody')[0];
    const novaLinha = tabela.insertRow();
    novaLinha.innerHTML = `
        <td>${funcionario}</td>
        <td>${data}</td>
        <td>${entrada}</td>
        <td>${saida}</td>
        <td>${intervalo}h</td>
        <td>${totalHoras.toFixed(2)}h</td>
    `;

    // Limpar o formulário
    document.getElementById('form-horario').reset();
});