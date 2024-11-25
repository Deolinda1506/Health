// Helper to fetch CSRF token
const getCSRFToken = () => {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
};

// Example usage in AJAX request
const fetchWithCSRF = (url, options) => {
    options.headers = {
        ...options.headers,
        'X-CSRFToken': getCSRFToken(),
    };
    return fetch(url, options);
};
