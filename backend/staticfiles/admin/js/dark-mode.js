const toggleBtn = document.getElementById('toggle-btn');
const body = document.body;
let darkMode = localStorage.getItem('dark-mode');

const enableDarkMode = () => {
    toggleBtn.classList.replace('fa-sun', 'fa-moon');
    body.classList.add('dark');
    localStorage.setItem('dark-mode', 'enabled');
};

const disableDarkMode = () => {
    toggleBtn.classList.replace('fa-moon', 'fa-sun');
    body.classList.remove('dark');
    localStorage.setItem('dark-mode', 'disabled');
};

if (darkMode === 'enabled') {
    enableDarkMode();
}

toggleBtn.onclick = () => {
    darkMode = localStorage.getItem('dark-mode');
    darkMode === 'disabled' ? enableDarkMode() : disableDarkMode();
};
