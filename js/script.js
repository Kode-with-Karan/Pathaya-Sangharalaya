var swiper = new Swiper(".slide-content", {
    slidesPerView: 5,
    spaceBetween: 25,
    loop: true,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        320: {
            slidesPerView: 2,
        },
        650: {
            slidesPerView: 3,
        },
        950: {
            slidesPerView: 4,
        },
        1250: {
            slidesPerView: 5,
        },
    },
  });