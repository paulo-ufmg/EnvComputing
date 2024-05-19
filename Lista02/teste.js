function executarCodigo() {
    var codigo = document.getElementById('code').value;
    var consoleLog = console.log; // Salva a referência original para console.log
    
    // Redefine console.log para capturar a saída
    var capturarSaida = [];
    console.log = function() {
      var mensagem = Array.prototype.slice.call(arguments).join(' ');
      capturarSaida.push(mensagem);
    };
    
    try {
      // Executa o código JavaScript usando eval()
      var resultado = eval(codigo);
      
      // Verifica se há saída capturada
      var saidaCapturada = capturarSaida.join('<br>');
      
      // Se houver saída capturada, exibe-a
      if (saidaCapturada) {
        document.getElementById('resultado').innerHTML = saidaCapturada;
      } else if (resultado === undefined) {
        document.getElementById('resultado').innerHTML = "<pre>Nenhum resultado retornado</pre>";
      } else {
        // Mostra o resultado na div resultado
        document.getElementById('resultado').innerHTML = "<pre>" + resultado + "</pre>";
      }
    } catch (error) {
      // Se houver um erro, mostra na div resultado
      document.getElementById('resultado').innerHTML = "<pre class='error'>" + error + "</pre>";
    }
    
    // Restaura console.log para sua referência original
    console.log = consoleLog;
  }