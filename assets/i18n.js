/* Shared i18n runtime — same pattern as echo-sim, htn-risk and score2-ap.
   Korean is the document default and is read straight out of the markup, so a
   page can never carry a Korean string that has no English counterpart without
   it being obvious. Each page defines I18N_EN before loading this file. */
var I18N = { ko: {}, en: (typeof I18N_EN === 'object' && I18N_EN) ? I18N_EN : {} };

(function(){
  var n = document.querySelectorAll('[data-i18n]'), i, j;
  for(i = 0; i < n.length; i++) I18N.ko[n[i].getAttribute('data-i18n')] = n[i].innerHTML;
  I18N.ko.doc_title = document.title;
  var a = document.querySelectorAll('[data-i18n-attr]');
  for(i = 0; i < a.length; i++){
    var spec = a[i].getAttribute('data-i18n-attr').split('|');
    for(j = 0; j < spec.length; j++){
      var p = spec[j].split(':');
      if(p.length === 2) I18N.ko[p[1]] = a[i].getAttribute(p[0]);
    }
  }
})();

var LANG = (function(){
  try{ var s = localStorage.getItem('tipcode-lang');
       if(s === 'ko' || s === 'en') return s; }catch(e){}
  return (navigator.language || '').toLowerCase().indexOf('ko') === 0 ? 'ko' : 'en';
})();

function t(k){
  var d = I18N[LANG];
  if(d && d[k] !== undefined) return d[k];
  return (I18N.ko[k] !== undefined) ? I18N.ko[k] : k;
}
function applyStaticI18n(){
  document.documentElement.setAttribute('lang', LANG);
  document.title = t('doc_title');
  var n = document.querySelectorAll('[data-i18n]'), i, j;
  for(i = 0; i < n.length; i++) n[i].innerHTML = t(n[i].getAttribute('data-i18n'));
  var a = document.querySelectorAll('[data-i18n-attr]');
  for(i = 0; i < a.length; i++){
    var spec = a[i].getAttribute('data-i18n-attr').split('|');
    for(j = 0; j < spec.length; j++){
      var p = spec[j].split(':');
      if(p.length === 2) a[i].setAttribute(p[0], t(p[1]));
    }
  }
  var kb = document.getElementById('lang-ko'), eb = document.getElementById('lang-en');
  if(kb) kb.setAttribute('aria-pressed', LANG === 'ko');
  if(eb) eb.setAttribute('aria-pressed', LANG === 'en');
}
function setLang(l){
  if(l !== 'ko' && l !== 'en') return;
  LANG = l;
  try{ localStorage.setItem('tipcode-lang', l); }catch(e){}
  applyStaticI18n();
}
applyStaticI18n();
