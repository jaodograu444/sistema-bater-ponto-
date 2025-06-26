function atualizarRelogio() {
    const agora = new Date();
    const horas = String(agora.getHours()).padStart(2, '0');
    const minutos = String(agora.getMinutes()).padStart(2, '0');
    const segundos = String(agora.getSeconds()).padStart(2, '0');
    const horarioFormatado = `${horas}:${minutos}:${segundos}`;
    document.getElementById('relogio').textContent = horarioFormatado;
}

setInterval(atualizarRelogio, 1000);
atualizarRelogio();

function registrarPonto(tipo) {
      const agora = new Date();
      const hora = agora.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit', second: '2-digit' });

      const relatorio = document.getElementById("relatorio");
      const div = document.createElement("div");
      div.classList.add("registro");
      div.textContent = `${tipo} batido às ${hora}`;
      relatorio.appendChild(div);
    }