document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('dashboard-btn').addEventListener('click', () => {
    window.location.href = "/dashboard";  // Adjust if needed
  });

  document.getElementById('logout-btn').addEventListener('click', () => {
    window.location.href = "/logout";  // Adjust if needed
  });
});
