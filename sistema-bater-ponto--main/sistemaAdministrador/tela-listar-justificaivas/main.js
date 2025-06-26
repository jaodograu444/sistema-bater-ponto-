document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".btn.aceitar, .btn.recusar");

    buttons.forEach((btn) => {
      btn.addEventListener("click", function () {
        const row = this.closest("tr");
        row.classList.add("fade-out");

        // Se quiser remover do DOM depois da animação:
        setTimeout(() => {
          row.remove();
        }, 500); // tempo igual ao da animação
      });
    });
  });