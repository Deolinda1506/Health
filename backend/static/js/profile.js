const profile = document.querySelector('.profile');
const userBtn = document.querySelector('#user-btn');

userBtn.onclick = () => {
    profile.classList.toggle('active');
};
