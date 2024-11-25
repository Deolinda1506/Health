window.addEventListener('resize', () => {
    if (window.innerWidth < 768) {
        document.querySelector('.sidebar').classList.add('mobile');
    } else {
        document.querySelector('.sidebar').classList.remove('mobile');
    }
});
