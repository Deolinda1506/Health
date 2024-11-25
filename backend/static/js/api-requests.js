const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

fetch('/save/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
    },
    body: JSON.stringify({ key: 'value' }),
});
