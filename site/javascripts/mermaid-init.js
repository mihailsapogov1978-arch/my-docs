document$.subscribe(() => {
  mermaid.initialize({
    startOnLoad: true,
    theme: 'default',
    themeVariables: {
      primaryColor: '#ff6600',
      primaryTextColor: '#fff',
      primaryBorderColor: '#7c0000',
      lineColor: '#F8B229',
      secondaryColor: '#006100',
      tertiaryColor: '#fff'
    }
  });
  
  mermaid.run({
    querySelector: '.mermaid'
  });
})