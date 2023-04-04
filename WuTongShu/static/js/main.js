$(function () {
    "use strict";
    $(window).on('load', function (event) {
        $('.preloader').delay(500).fadeOut(500);
    });
    $(window).on('scroll', function (event) {
        var scroll = $(window).scrollTop();
        if (scroll < 20) {
            $(".navbar-area").removeClass("sticky");
            $(".navbar-area img").attr("src", "assets/images/logo.svg");
        } else {
            $(".navbar-area").addClass("sticky");
            $(".navbar-area img").attr("src", "assets/images/logo-2.svg");
        }
    });
    var scrollLink = $('.page-scroll');
    $(window).scroll(function () {
        var scrollbarLocation = $(this).scrollTop();
        scrollLink.each(function () {
            var sectionOffset = $(this.hash).offset().top - 73;
            if (sectionOffset <= scrollbarLocation) {
                $(this).parent().addClass('active');
                $(this).parent().siblings().removeClass('active');
            }
        });
    });
    $(".navbar-nav a").on('click', function () {
        $(".navbar-collapse").removeClass("show");
    });
    $(".navbar-toggler").on('click', function () {
        $(this).toggleClass("active");
    });
    $(".navbar-nav a").on('click', function () {
        $(".navbar-toggler").removeClass('active');
    });
    $('[href="#side-menu-left"], .overlay-left').on('click', function (event) {
        $('.sidebar-left, .overlay-left').addClass('open');
    });
    $('[href="#close"], .overlay-left').on('click', function (event) {
        $('.sidebar-left, .overlay-left').removeClass('open');
    });
    $('.slider-items-active').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        speed: 800,
        arrows: true,
        prevArrow: '<span class="prev"><i class="lni lni-arrow-left"></i></span>',
        nextArrow: '<span class="next"><i class="lni lni-arrow-right"></i></span>',
        dots: true,
        autoplay: true,
        autoplaySpeed: 5000,
        responsive: [{breakpoint: 1200, settings: {slidesToShow: 3,}}, {
            breakpoint: 992,
            settings: {slidesToShow: 2,}
        }, {breakpoint: 768, settings: {slidesToShow: 2,}}, {
            breakpoint: 576,
            settings: {slidesToShow: 1, arrows: false,}
        }]
    });

    $('.testimonial-active').slick({
        dots: false,
        arrows: true,
        prevArrow: '<span class="prev"><i class="lni lni-arrow-left"></i></span>',
        nextArrow: '<span class="next"><i class="lni lni-arrow-right"></i></span>',
        infinite: true,
        autoplay: true,
        autoplaySpeed: 5000,
        speed: 800,
        slidesToShow: 1,
    });
    $('.video-popup').magnificPopup({type: 'iframe'});
    $('.image-popup').magnificPopup({type: 'image', gallery: {enabled: true}});
    $(window).on('scroll', function (event) {
        if ($(this).scrollTop() > 600) {
            $('.back-to-top').fadeIn(200)
        } else {
            $('.back-to-top').fadeOut(200)
        }
    });
    $('.back-to-top').on('click', function (event) {
        event.preventDefault();
        $('html, body').animate({scrollTop: 0,}, 1500);
    });
});