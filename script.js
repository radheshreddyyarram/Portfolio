document.addEventListener('DOMContentLoaded', () => {
    // --- Navigation Toggle for Mobile ---
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const links = document.querySelectorAll('.nav-links li');

    hamburger.addEventListener('click', () => {
        // Toggle Nav
        navLinks.classList.toggle('active');

        // Burger Animation
        hamburger.classList.toggle('active');

        // Prevent background scrolling
        document.body.classList.toggle('no-scroll');
    });

    // Close mobile menu when a link is clicked
    links.forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                hamburger.classList.remove('active');
                document.body.classList.remove('no-scroll');
            }
        });
    });

    // --- Navbar Background Change on Scroll ---
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // --- Scroll Reveal Animations ---
    const fadeElements = document.querySelectorAll('.fade-in, .fade-up');

    const appearOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const appearOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, appearOptions);

    fadeElements.forEach(el => {
        appearOnScroll.observe(el);
    });

    // --- Custom Cursor ---
    // Only initialize if device has a fine pointer (mouse) to avoid breaking mobile touch
    if (window.matchMedia("(pointer: fine)").matches) {
        const cursor = document.createElement('div');
        cursor.classList.add('cursor-minimal');
        document.body.appendChild(cursor);

        window.addEventListener('mousemove', (e) => {
            cursor.style.left = `${e.clientX}px`;
            cursor.style.top = `${e.clientY}px`;
        });

        // Add hover effect for interactive elements
        const interactables = document.querySelectorAll('a, button, input, textarea, .btn, .project-card, .overview-card, .contact-method-card');
        interactables.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursor.classList.add('hover');
            });
            el.addEventListener('mouseleave', () => {
                cursor.classList.remove('hover');
            });
        });
    }

    // --- Dynamic Copyright Year ---
    const footerText = document.querySelector('footer p');
    if (footerText) {
        const year = new Date().getFullYear();
        footerText.innerHTML = `&copy; ${year} Radhesh Reddy Yarram. Built with passion.`;
    }

    // --- Active Page Navigation Highlighting ---
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navItems = document.querySelectorAll('.nav-links a');
    navItems.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active-link');
        }
    });
});
