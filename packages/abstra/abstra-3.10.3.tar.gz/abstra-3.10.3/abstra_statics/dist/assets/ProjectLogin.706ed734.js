import{_ as f}from"./AbstraLogo.vue_vue_type_script_setup_true_lang.86e80d08.js";import{B as y}from"./BaseLayout.6877b02b.js";import{d as l,E as m,L as b,a0 as u,a_ as v,a$ as g,o as _,Y as h,a as r,Z as s,ea as w,eo as S,X as L,c as k,w as n,b as i,u as $}from"./index.2dd5159c.js";import{u as x}from"./editor.86896781.js";import{b as B}from"./index.6c2a02cd.js";import"./Logo.16b7e007.js";import"./workspaceStore.0cf70627.js";import"./url.12524b23.js";import"./colorHelpers.d7b212d4.js";import"./linters.542b8f2a.js";import"./asyncComputed.4fd564dc.js";import"./index.8875f21d.js";import"./Avatar.7dd6bc69.js";import"./index.d6be2ad0.js";(function(){try{var e=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},o=new Error().stack;o&&(e._sentryDebugIds=e._sentryDebugIds||{},e._sentryDebugIds[o]="544bb6aa-61d2-4951-99c0-d7c5c7f951ba",e._sentryDebugIdIdentifier="sentry-dbid-544bb6aa-61d2-4951-99c0-d7c5c7f951ba")}catch{}})();const I=l({props:{loading:{type:Boolean,default:!0},color:{type:String,default:"#ea576a"},size:{type:String,default:"10px"},radius:{type:String,default:"100%"}},setup(e){const o=m({spinnerStyle:{width:e.size,height:e.size,borderRadius:e.radius,backgroundColor:e.color}});return{...b(o)}}});const P={class:"v-spinner"};function D(e,o,a,c,d,p){return v((_(),h("div",P,[r("div",{class:"v-beat v-beat-odd",style:s(e.spinnerStyle)},null,4),r("div",{class:"v-beat v-beat-even",style:s(e.spinnerStyle)},null,4),r("div",{class:"v-beat v-beat-odd",style:s(e.spinnerStyle)},null,4)],512)),[[g,e.loading]])}const R=u(I,[["render",D],["__scopeId","data-v-06538001"]]),j={class:"content"},z=l({__name:"ProjectLogin",setup(e){const o=w(),a=S(),c=x();function d(){const t=new URL(location.href);t.searchParams.delete("api-key"),a.replace(t.pathname+t.search)}function p(){const t=o.query["api-key"];if(typeof t=="string")return t}return L(async()=>{const t=p();if(!t){a.push({name:"error"});return}await c.createLogin(t).then(d),a.push({name:"workspace"})}),(t,C)=>(_(),k(y,null,{navbar:n(()=>[i($(B),{style:{padding:"5px 25px",border:"1px solid #f0f0f0"}},{title:n(()=>[i(f)]),_:1})]),content:n(()=>[r("div",j,[i(R)])]),_:1}))}});const J=u(z,[["__scopeId","data-v-944edebb"]]);export{J as default};
//# sourceMappingURL=ProjectLogin.706ed734.js.map
