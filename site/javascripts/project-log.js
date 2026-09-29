(function () {
  const CONFIG = {
    repoOwner: "mihailsapogov1978-arch",
    repoName: "my-docs",
    label: "Spravky_obr",
  };

  function escapeHtml(value) {
    return String(value ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function githubIssuesUrl(extra) {
    const base = `https://api.github.com/repos/${CONFIG.repoOwner}/${CONFIG.repoName}/issues`;
    const params = new URLSearchParams({
      labels: CONFIG.label,
      sort: "updated",
      direction: "desc",
      state: "open",
      ...extra,
    });
    return `${base}?${params.toString()}`;
  }

  function newIssueUrl(title, body) {
    const params = new URLSearchParams({
      labels: CONFIG.label,
      title: title,
      body: body || "",
    });
    return `https://github.com/${CONFIG.repoOwner}/${CONFIG.repoName}/issues/new?${params.toString()}`;
  }

  async function loadRecentComments() {
    const container = document.getElementById("recent-comments");
    if (!container) {
      return;
    }

    try {
      const response = await fetch(githubIssuesUrl({ per_page: "3" }));
      if (!response.ok) {
        container.textContent = "Не удалось загрузить обсуждения.";
        return;
      }

      const issues = await response.json();
      if (!issues.length) {
        container.textContent = "Пока нет комментариев. Будьте первым!";
        return;
      }

      const list = document.createElement("div");
      const heading = document.createElement("p");
      heading.innerHTML = "<strong>Последние обсуждения</strong>";
      list.appendChild(heading);

      issues.forEach((issue) => {
        const row = document.createElement("div");
        row.className = "project-log__item";
        const link = document.createElement("a");
        link.href = issue.html_url;
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        link.textContent = String(issue.title || "").replace("[Spravky_obr] ", "");
        const meta = document.createElement("small");
        meta.textContent = `Обновлено: ${new Date(issue.updated_at).toLocaleDateString("ru-RU")}`;
        row.appendChild(link);
        row.appendChild(document.createElement("br"));
        row.appendChild(meta);
        list.appendChild(row);
      });

      container.replaceChildren(list);
    } catch (error) {
      container.textContent = "Ошибка загрузки комментариев.";
    }
  }

  function formatIssueBody(text) {
    if (!text) {
      return "";
    }
    let formatted = text;
    const metaIndex = formatted.lastIndexOf("\n---\n");
    if (metaIndex !== -1) {
      formatted = formatted.substring(0, metaIndex);
    }
    formatted = formatted.trim();
    if (formatted.length > 200) {
      formatted = `${formatted.substring(0, 200)}...`;
    }
    return escapeHtml(formatted).replace(/\n/g, "<br>");
  }

  async function loadLogEntries() {
    const container = document.getElementById("log-container");
    if (!container) {
      return;
    }

    const statusEl = document.getElementById("connection-status");
    if (statusEl) {
      statusEl.textContent = "Загрузка записей...";
    }

    try {
      const response = await fetch(
        githubIssuesUrl({ state: "all", per_page: "30" })
      );
      if (!response.ok) {
        container.textContent = `Не удалось загрузить лог (HTTP ${response.status}). Если репозиторий закрытый, записи будут доступны только через GitHub.`;
        return;
      }

      const issues = await response.json();
      const stats = document.getElementById("stats");
      if (stats) {
        const openIssues = issues.filter((item) => item.state === "open").length;
        const closedIssues = issues.filter((item) => item.state === "closed").length;
        stats.textContent = `Всего: ${issues.length}. Открыто: ${openIssues}. Закрыто: ${closedIssues}.`;
      }

      if (!issues.length) {
        container.textContent = "Лог пуст.";
        return;
      }

      const wrap = document.createElement("div");
      issues.forEach((issue) => {
        const card = document.createElement("article");
        card.className = "project-log__item";
        const title = document.createElement("a");
        title.href = issue.html_url;
        title.target = "_blank";
        title.rel = "noopener noreferrer";
        title.textContent = issue.title || "Запись";
        const body = document.createElement("div");
        body.innerHTML = formatIssueBody(issue.body);
        const meta = document.createElement("small");
        meta.textContent = `${issue.state === "open" ? "Открыто" : "Закрыто"} · ${new Date(issue.created_at).toLocaleString("ru-RU")}`;
        card.appendChild(title);
        card.appendChild(body);
        card.appendChild(meta);
        wrap.appendChild(card);
      });
      container.replaceChildren(wrap);
      if (statusEl) {
        statusEl.textContent = `Загружено записей: ${issues.length}`;
      }
    } catch (error) {
      container.textContent = "Ошибка сети при загрузке лога.";
    }
  }

  function bindComposer() {
    const button = document.getElementById("log-submit");
    const textarea = document.getElementById("log-entry");
    if (!button || !textarea) {
      return;
    }

    const submit = () => {
      const text = textarea.value.trim();
      if (!text) {
        return;
      }
      const typeInput = document.querySelector('input[name="entry-type"]:checked');
      const type = typeInput ? typeInput.value : "note";
      const prefixes = {
        note: "Заметка",
        task: "Задача",
        question: "Вопрос",
        idea: "Идея",
      };
      const title = `[${prefixes[type] || "Заметка"}] ${text.slice(0, 70)}`;
      window.open(newIssueUrl(title, text), "_blank", "noopener,noreferrer");
    };

    button.addEventListener("click", submit);
    textarea.addEventListener("keydown", (event) => {
      if (event.ctrlKey && event.key === "Enter") {
        submit();
      }
    });
  }

  function init() {
    loadRecentComments();
    loadLogEntries();
    bindComposer();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
