function atualizarHora() {
    const agora = new Date();
    const hora = agora.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    document.getElementById('hora').textContent = hora;
  }

  // Atualiza a hora a cada segundo
  setInterval(atualizarHora, 1000);

  // Chama a função imediatamente ao carregar a página
  atualizarHora();