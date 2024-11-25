window.addEventListener('resize', () => {
    if (window.innerWidth < 768) {
        document.querySelector('.side-bar').classList.add('mobile');
    } else {
        document.querySelector('.side-bar').classList.remove('mobile');
    }
});
