import{_}from"./Login.vue_vue_type_script_setup_true_lang.ea7b3bde.js";import{d as l,eo as m,ea as b,o as g,Y as y,b as w,u as n,a0 as k}from"./index.2dd5159c.js";import{u as h}from"./workspaceStore.0cf70627.js";import"./Logo.16b7e007.js";import"./string.bc06ff97.js";import"./CircularLoading.ad5989fc.js";import"./index.787f6cf7.js";import"./url.12524b23.js";import"./colorHelpers.d7b212d4.js";(function(){try{var e=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},o=new Error().stack;o&&(e._sentryDebugIds=e._sentryDebugIds||{},e._sentryDebugIds[o]="610f86cb-4350-46e3-baf8-a00dffccaf14",e._sentryDebugIdIdentifier="sentry-dbid-610f86cb-4350-46e3-baf8-a00dffccaf14")}catch{}})();const v={class:"runner"},I=l({__name:"Login",setup(e){const o=m(),a=b(),t=h(),f=async()=>{const{redirect:r,...s}=a.query;if(r){await o.push({path:r,query:s,params:a.params});return}o.push({name:"playerHome",query:s})};return(r,s)=>{var c,u,d,p,i;return g(),y("div",v,[w(_,{"logo-url":(u=(c=n(t).state.workspace)==null?void 0:c.logoUrl)!=null?u:void 0,"brand-name":(d=n(t).state.workspace)==null?void 0:d.brandName,locale:(i=(p=n(t).state.workspace)==null?void 0:p.language)!=null?i:"en",onDone:f},null,8,["logo-url","brand-name","locale"])])}}});const C=k(I,[["__scopeId","data-v-cb33c596"]]);export{C as default};
//# sourceMappingURL=Login.f9a9b0e4.js.map
