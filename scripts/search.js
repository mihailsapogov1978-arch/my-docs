// docs/search.js
document.addEventListener('DOMContentLoaded', function() {
  if (typeof lunr !== 'undefined') {
    // Переопределяем tokenizer для русского языка
    lunr.tokenizer = function (str) {
      if (!str || typeof str !== 'string') return []
      // Приводим к нижнему регистру перед токенизацией
      str = str.toLowerCase()
      // Разбиваем по пробелам, дефисам, точкам и др.
      return str.split(/[\s\-–—_\.,;:!?]+/).filter(token => token.length > 2)
    }
  }
});