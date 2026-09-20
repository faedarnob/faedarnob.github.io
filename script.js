/**
 * Faed Ahmed Arnob - Research Portfolio & Academic CV
 * Interactive scripts: Theme toggle, filtering, copy utilities, smooth scrolling
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initScrollProgress();
  initNavHighlight();
  initMobileMenu();
  initProjectFilters();
  initPublicationFilters();
  initAccordions();
  initCopyButtons();
});

/* --- Theme Toggle (Dark / Light Mode) --- */
function initTheme() {
  const toggleBtn = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  
  // Prefer stored theme or default to dark
  const storedTheme = localStorage.getItem('faed_portfolio_theme');
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  const initialTheme = storedTheme ? storedTheme : (prefersDark ? 'dark' : 'dark');

  document.documentElement.setAttribute('data-theme', initialTheme);
  updateThemeIcon(initialTheme);

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('faed_portfolio_theme', newTheme);
      updateThemeIcon(newTheme);
    });
  }
}

function updateThemeIcon(theme) {
  const themeIcon = document.getElementById('theme-icon');
  if (!themeIcon) return;
  if (theme === 'dark') {
    themeIcon.className = 'fas fa-sun';
    themeIcon.setAttribute('title', 'Switch to Light Mode');
  } else {
    themeIcon.className = 'fas fa-moon';
    themeIcon.setAttribute('title', 'Switch to Dark Mode');
  }
}

/* --- Scroll Progress Bar --- */
function initScrollProgress() {
  const progressBar = document.getElementById('scroll-progress');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (totalHeight <= 0) return;
    const progress = (window.pageYOffset / totalHeight) * 100;
    progressBar.style.width = `${progress}%`;
  });
}

/* --- Active Nav Link on Scroll --- */
function initNavHighlight() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }, {
    rootMargin: '-20% 0px -70% 0px'
  });

  sections.forEach(sec => observer.observe(sec));
}

/* --- Mobile Menu Drawer --- */
function initMobileMenu() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const navMenu = document.getElementById('nav-menu');

  if (!menuBtn || !navMenu) return;

  menuBtn.addEventListener('click', () => {
    navMenu.classList.toggle('open');
    const isOpen = navMenu.classList.contains('open');
    menuBtn.innerHTML = isOpen ? '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
  });

  // Close when clicking any nav link
  document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('open');
      menuBtn.innerHTML = '<i class="fas fa-bars"></i>';
    });
  });
}

/* --- Project Category Filters --- */
function initProjectFilters() {
  const filterBtns = document.querySelectorAll('#project-filters .filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const category = card.getAttribute('data-category') || '';
        if (filterValue === 'all' || category.includes(filterValue)) {
          card.style.display = 'flex';
          card.style.opacity = '1';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* --- Publication Filters --- */
function initPublicationFilters() {
  const filterBtns = document.querySelectorAll('#pub-filters .filter-btn');
  const pubCards = document.querySelectorAll('.pub-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      pubCards.forEach(card => {
        const category = card.getAttribute('data-category') || '';
        if (filterValue === 'all' || category === filterValue) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* --- Collapsible Accordions for Abstract & BibTeX --- */
function initAccordions() {
  // Toggle Abstract
  document.querySelectorAll('.btn-toggle-abstract').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = btn.getAttribute('data-target');
      const collapseEl = document.getElementById(targetId);
      if (!collapseEl) return;

      const isOpen = collapseEl.classList.contains('open');
      // Close all other open collapses in this pub card
      const parentCard = btn.closest('.pub-card');
      if (parentCard) {
        parentCard.querySelectorAll('.pub-collapse').forEach(el => {
          if (el !== collapseEl) el.classList.remove('open');
        });
      }

      collapseEl.classList.toggle('open');
      btn.innerHTML = isOpen 
        ? '<i class="far fa-file-alt"></i> Abstract' 
        : '<i class="fas fa-chevron-up"></i> Hide Abstract';
    });
  });

  // Toggle BibTeX
  document.querySelectorAll('.btn-toggle-bibtex').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = btn.getAttribute('data-target');
      const collapseEl = document.getElementById(targetId);
      if (!collapseEl) return;

      const isOpen = collapseEl.classList.contains('open');
      const parentCard = btn.closest('.pub-card');
      if (parentCard) {
        parentCard.querySelectorAll('.pub-collapse').forEach(el => {
          if (el !== collapseEl) el.classList.remove('open');
        });
      }

      collapseEl.classList.toggle('open');
      btn.innerHTML = isOpen 
        ? '<i class="fas fa-quote-right"></i> BibTeX' 
        : '<i class="fas fa-chevron-up"></i> Hide BibTeX';
    });
  });
}

/* --- Copy Utilities with Toast Notification --- */
function initCopyButtons() {
  // Copy BibTeX
  document.querySelectorAll('.btn-copy-bibtex').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-target');
      const codeEl = document.getElementById(targetId);
      if (!codeEl) return;

      const text = codeEl.innerText.trim();
      navigator.clipboard.writeText(text).then(() => {
        showToast('BibTeX citation copied to clipboard!');
      }).catch(err => {
        console.error('Failed to copy text: ', err);
      });
    });
  });

  // Copy Email button
  document.querySelectorAll('.btn-copy-email').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const email = 'faed.arnob60@gmail.com';
      navigator.clipboard.writeText(email).then(() => {
        showToast('Email address copied to clipboard (faed.arnob60@gmail.com)');
      });
    });
  });
}

/* --- Toast Feedback Notification --- */
function showToast(message) {
  let toast = document.getElementById('portfolio-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'portfolio-toast';
    toast.className = 'toast';
    document.body.appendChild(toast);
  }

  toast.innerHTML = `<i class="fas fa-check-circle" style="color: var(--accent-emerald);"></i> <span>${message}</span>`;
  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, 3200);
}
