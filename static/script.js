document.addEventListener('DOMContentLoaded', function() {
  const quoteElement = document.querySelector('#quote');
  const typedElement = document.querySelector('.typed');
  const remainingElement = document.querySelector('.remaining');
  const textInput = document.querySelector('#text-input');

  textInput.addEventListener('input', function() {
    const typedText = textInput.value;
    const quoteText = quoteElement.textContent;

    if (quoteText.startsWith(typedText)) {
      typedElement.textContent = typedText;
      remainingElement.textContent = quoteText.substring(typedText.length);
      typedElement.classList.remove('incorrect');
      remainingElement.classList.remove('incorrect');
    } else {
      typedElement.textContent = quoteText.substring(0, typedText.length);
      remainingElement.textContent = quoteText.substring(typedText.length);
      typedElement.classList.add('incorrect');
      remainingElement.classList.add('incorrect');
    }
  });
});
