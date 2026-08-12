/* HiTide Biotech · shared interactions */
(function(){
  'use strict';

  /* ---- scroll progress + nav shadow ---- */
  var nav = document.querySelector('.nav');
  var prog = document.getElementById('progress');
  function onScroll(){
    var st = window.scrollY || document.documentElement.scrollTop;
    if(nav) nav.classList.toggle('scrolled', st > 30);
    if(prog){
      var h = document.documentElement.scrollHeight - window.innerHeight;
      prog.style.width = (h>0 ? (st/h*100) : 0) + '%';
    }
  }
  window.addEventListener('scroll', onScroll, {passive:true});
  onScroll();

  /* ---- mobile menu ---- */
  var burger = document.querySelector('.hamburger');
  var mmenu = document.querySelector('.mobile-menu');
  if(burger && mmenu){
    burger.addEventListener('click', function(){
      burger.classList.toggle('open');
      mmenu.classList.toggle('open');
    });
    mmenu.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){ burger.classList.remove('open'); mmenu.classList.remove('open'); });
    });
  }

  /* ---- reveal on scroll ---- */
  var revs = document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window && revs.length){
    var ro = new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('visible'); ro.unobserve(e.target);} });
    }, {threshold:.12, rootMargin:'0px 0px -50px 0px'});
    revs.forEach(function(el){ ro.observe(el); });
  } else { revs.forEach(function(el){ el.classList.add('visible'); }); }

  /* ---- counters ---- */
  var counters = document.querySelectorAll('[data-count]');
  if('IntersectionObserver' in window && counters.length){
    var co = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(!e.isIntersecting) return;
        var el = e.target, target = parseFloat(el.dataset.count), suf = el.dataset.suffix || '';
        if(isNaN(target)){ co.unobserve(el); return; }
        var cur = 0, step = Math.max(1, target/45), dur = 30;
        var t = setInterval(function(){
          cur += step;
          if(cur >= target){ cur = target; clearInterval(t); }
          el.textContent = (Number.isInteger(target)? Math.floor(cur) : cur.toFixed(1)) + suf;
        }, dur);
        co.unobserve(el);
      });
    }, {threshold:.5});
    counters.forEach(function(el){ co.observe(el); });
  }

  /* ---- lightbox ---- */
  var lb = document.createElement('div');
  lb.className = 'lightbox';
  lb.innerHTML = '<button class="lightbox-close" aria-label="close">&times;</button><img alt=""><div class="lightbox-cap"></div>';
  document.body.appendChild(lb);
  var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('.lightbox-cap');
  function openLB(src, cap){ lbImg.src = src; lbCap.textContent = cap||''; lb.classList.add('open'); document.body.style.overflow='hidden'; }
  function closeLB(){ lb.classList.remove('open'); lbImg.src=''; document.body.style.overflow=''; }
  document.addEventListener('click', function(e){
    var z = e.target.closest('[data-zoom]');
    if(z){
      var img = z.tagName==='IMG'? z : z.querySelector('img');
      if(img){ openLB(img.getAttribute('src'), img.getAttribute('data-name')||img.alt||''); }
    }
  });
  lb.addEventListener('click', closeLB);
  document.addEventListener('keydown', function(e){ if(lb.classList.contains('open') && (e.key==='Escape'||e.key===' ')){ e.preventDefault(); closeLB(); } });

  /* ---- generic tabs ---- */
  document.querySelectorAll('[data-tabs]').forEach(function(group){
    var tabs = group.querySelectorAll('.tab');
    tabs.forEach(function(tab){
      tab.addEventListener('click', function(){
        var id = tab.dataset.tab;
        tabs.forEach(function(t){ t.classList.remove('active'); });
        tab.classList.add('active');
        group.querySelectorAll('.pane').forEach(function(p){ p.classList.toggle('active', p.dataset.pane===id); });
      });
    });
  });

  /* ---- accordions ---- */
  document.querySelectorAll('.acc-head').forEach(function(h){
    h.addEventListener('click', function(){ h.parentElement.classList.toggle('open'); });
  });

  /* ---- cert slider arrows ---- */
  var track = document.getElementById('certTrack');
  if(track){
    var prev = document.getElementById('certPrev'), next = document.getElementById('certNext');
    var amt = function(){ return track.clientWidth * .6; };
    if(prev) prev.addEventListener('click', function(){ track.scrollBy({left:-amt(),behavior:'smooth'}); });
    if(next) next.addEventListener('click', function(){ track.scrollBy({left:amt(),behavior:'smooth'}); });
  }

  /* ---- active nav link by path ---- */
  var path = location.pathname.split('/').pop();
  document.querySelectorAll('.nav-links a[data-nav]').forEach(function(a){
    if(a.getAttribute('data-nav') === (path||'index.html')) a.classList.add('active');
  });

  /* ---- language toggle (zh / en) ---- */
  var I18N = window.__I18N__ || {'zh':{}, 'en':{}};
  function applyLang(lang){
    var dict = I18N[lang] || {};
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var key = el.getAttribute('data-i18n');
      if(dict[key] != null) el.textContent = dict[key];
    });
    var tEl = document.querySelector('title[data-en-title]');
    if(tEl){
      tEl.textContent = (lang === 'en')
        ? (tEl.getAttribute('data-en-title') || tEl.textContent)
        : (tEl.getAttribute('data-zh-title') || tEl.textContent);
    }
    document.documentElement.lang = (lang === 'en') ? 'en' : 'zh-CN';
    document.body.classList.toggle('lang-en', lang === 'en');
    var zh = document.getElementById('langZh'), en = document.getElementById('langEn');
    if(zh) zh.classList.toggle('on', lang === 'zh');
    if(en) en.classList.toggle('on', lang === 'en');
    try { localStorage.setItem('hitide_lang', lang); } catch(e){}
  }
  var zhBtn = document.getElementById('langZh'), enBtn = document.getElementById('langEn');
  if(zhBtn) zhBtn.addEventListener('click', function(){ applyLang('zh'); });
  if(enBtn) enBtn.addEventListener('click', function(){ applyLang('en'); });
  var saved = null;
  try { saved = localStorage.getItem('hitide_lang'); } catch(e){}
  if(saved === 'en' && enBtn) applyLang('en');

  /* ---- products: filter + search + symptom matcher ---- */
  var pGrid = document.getElementById('pGrid');
  if(pGrid){
    var pChips = document.getElementById('pChips');
    var pSearch = document.getElementById('pSearch');
    var pEmpty = document.getElementById('pEmpty');
    function applyFilter(){
      var cat = (pChips && pChips.querySelector('.chip.active')) ? pChips.querySelector('.chip.active').dataset.cat : 'all';
      var q = (pSearch && pSearch.value || '').trim().toLowerCase();
      var shown = 0;
      pGrid.querySelectorAll('.product').forEach(function(a){
        var okCat = (cat==='all' || a.dataset.cat===cat);
        var hay = ((a.dataset.search||'') + ' ' + (a.dataset.name||'')).toLowerCase();
        var okQ = !q || hay.indexOf(q) > -1;
        var vis = okCat && okQ;
        a.style.display = vis ? '' : 'none';
        if(vis) shown++;
      });
      if(pEmpty) pEmpty.style.display = shown ? 'none' : 'block';
    }
    if(pChips){
      pChips.querySelectorAll('.chip').forEach(function(b){
        b.addEventListener('click', function(){
          pChips.querySelectorAll('.chip').forEach(function(x){ x.classList.remove('active'); });
          b.classList.add('active');
          applyFilter();
        });
      });
    }
    if(pSearch) pSearch.addEventListener('input', applyFilter);
    applyFilter();

    var M = window.__MATCHER__ || [];
    var mSpecies = document.getElementById('mSpecies');
    var mSymptom = document.getElementById('mSymptom');
    var mResult = document.getElementById('mResult');
    var mCards = document.getElementById('mCards');
    if(mResult) mResult.style.display = 'none';
    function renderRec(id){
      var card = pGrid.querySelector('.product[href$="'+id+'.html"]');
      if(!card || !mResult || !mCards) return;
      var clone = card.cloneNode(true);
      clone.removeAttribute('style');
      mCards.innerHTML = '';
      mCards.appendChild(clone);
      mResult.style.display = 'block';
      mResult.scrollIntoView({behavior:'smooth', block:'center'});
    }
    if(mSpecies){
      mSpecies.querySelectorAll('.pill').forEach(function(b){
        b.addEventListener('click', function(){
          var isEn = document.body.classList.contains('lang-en');
          mSpecies.querySelectorAll('.pill').forEach(function(x){ x.classList.remove('active'); });
          b.classList.add('active');
          var sp = b.dataset.species;
          var entry = M.filter(function(e){ return e.sp === sp; })[0];
          mSymptom.innerHTML = entry
            ? entry.sym.map(function(s){ return '<button class="pill" data-id="'+s.id+'">'+ (isEn ? (s.en||s.n) : s.n) +'</button>'; }).join('')
            : '<span style="color:var(--ink-3);font-size:13px;">'+(isEn?'No data available':'暂无数据')+'</span>';
          if(mResult) mResult.style.display = 'none';
          mSymptom.querySelectorAll('.pill').forEach(function(sb){
            sb.addEventListener('click', function(){
              mSymptom.querySelectorAll('.pill').forEach(function(x){ x.classList.remove('active'); });
              sb.classList.add('active');
              renderRec(sb.dataset.id);
            });
          });
        });
      });
    }
  }
})();
