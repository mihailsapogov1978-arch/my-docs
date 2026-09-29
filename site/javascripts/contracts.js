function initContractRows() {
  const rows = document.querySelectorAll(".contract-row");
  if (!rows.length) {
    return;
  }

  let currentOpen = null;
  rows.forEach((row) => {
    row.addEventListener("click", () => {
      const targetId = row.getAttribute("data-target");
      const detailsRow = document.getElementById(targetId);
      if (!detailsRow) {
        return;
      }

      if (currentOpen && currentOpen !== detailsRow) {
        currentOpen.style.display = "none";
      }

      if (detailsRow.style.display === "none" || detailsRow.style.display === "") {
        detailsRow.style.display = "table-row";
        currentOpen = detailsRow;
      } else {
        detailsRow.style.display = "none";
        currentOpen = null;
      }
    });
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(initContractRows);
} else {
  document.addEventListener("DOMContentLoaded", initContractRows);
}
