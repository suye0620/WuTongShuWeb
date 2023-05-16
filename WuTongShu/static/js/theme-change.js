const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
const currentTheme = localStorage.getItem('theme');
const themeImg = document.querySelector('#logo-img');
const darkImage = '/static/images/wutongshu-logo/logo-dark.png';
const lightImage = '/static/images/wutongshu-logo/logo-light.png';
if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);

    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
        // 如果打开即为暗黑模式，则也设置好对应的暗黑logo
        themeImg.src = darkImage;
    }
}

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        themeImg.src = darkImage;
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
        themeImg.src = lightImage;
    }
}

toggleSwitch.addEventListener('change', switchTheme, false);