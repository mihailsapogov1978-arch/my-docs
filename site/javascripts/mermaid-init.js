function initMermaid() {
  if (typeof mermaid === "undefined") {
    return;
  }

  const isDark =
    document.body.getAttribute("data-md-color-scheme") === "slate";

  mermaid.initialize({
    startOnLoad: false,
    theme: isDark ? "dark" : "default",
  });

  const nodes = document.querySelectorAll(".mermaid");
  nodes.forEach((node) => {
    if (node.getAttribute("data-processed")) {
      node.removeAttribute("data-processed");
    }
  });

  mermaid.run({ querySelector: ".mermaid" });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(initMermaid);
} else {
  document.addEventListener("DOMContentLoaded", initMermaid);
}
