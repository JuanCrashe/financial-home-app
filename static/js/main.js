/**
 * Main JavaScript for Housing Finance App
 */

document.addEventListener("DOMContentLoaded", () => {
  // Sidebar Toggle Logic for Mobile
  const sidebar = document.querySelector(".sidebar");
  const sidebarToggle = document.getElementById("sidebarToggle");
  const mainContent = document.querySelector(".main-content"); // Used for overlay click if we implement one

  if (sidebarToggle) {
    sidebarToggle.addEventListener("click", (e) => {
      e.stopPropagation(); // Prevent immediate closing if we have document click listener
      sidebar.classList.toggle("show");
    });
  }

  // Close sidebar when clicking outside on mobile
  document.addEventListener("click", (e) => {
    if (window.innerWidth < 992) {
      if (
        sidebar.classList.contains("show") &&
        !sidebar.contains(e.target) &&
        e.target !== sidebarToggle &&
        !sidebarToggle.contains(e.target)
      ) {
        sidebar.classList.remove("show");
      }
    }
  });
});
