const images = document.querySelectorAll('img[data-src]');

const lazyLoad = (img) => {
    img.src = img.dataset.src;
    img.removeAttribute('data-src');
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            lazyLoad(entry.target);
            observer.unobserve(entry.target);
        }
    });
});

images.forEach((img) => observer.observe(img));
