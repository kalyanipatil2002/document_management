document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.querySelector('.image-carousel');
    let scrollAmount = 0;
    const scrollStep = 1; // Amount to scroll each step
    const delay = 30; // Delay in ms between each step

    function scrollCarousel() {
        scrollAmount += scrollStep;
        carousel.style.transform = `translateX(-${scrollAmount}px)`;

        if (scrollAmount >= carousel.scrollWidth / carousel.children.length) {
            scrollAmount = 0;
            carousel.style.transform = `translateX(0)`;
        }
    }

    setInterval(scrollCarousel, delay);
});
