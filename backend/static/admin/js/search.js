const searchInput = document.getElementById('search-input');
const searchDropdown = document.querySelector('.search-dropdown');

searchInput.addEventListener('input', async (e) => {
    const query = e.target.value.trim();

    if (query) {
        const response = await fetch(`/search-doctors?q=${query}`);
        const results = await response.json();

        searchDropdown.innerHTML = results
            .map(
                (result) =>
                    `<div class="search-result">${result.name} - ${result.specialty}</div>`
            )
            .join('');
        searchDropdown.classList.add('active');
    } else {
        searchDropdown.classList.remove('active');
    }
});
