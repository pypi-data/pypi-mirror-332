import{N as V}from"./Navbar.d28d7928.js";import{B as f}from"./BaseLayout.6877b02b.js";import{a as H}from"./asyncComputed.4fd564dc.js";import{d as A,D as c,f as n,o as e,Y as t,$ as Z,S as v,e8 as $,a as o,ea as w,r as b,c as M,w as C,b as y,a0 as k}from"./index.2dd5159c.js";import"./gateway.b5c36d12.js";import{a as S}from"./organization.05cae81f.js";import{a as _}from"./project.256d8e61.js";import"./tables.748603cc.js";import{_ as z,S as B}from"./Sidebar.a3729df3.js";import{C as x}from"./ContentLayout.a4ded992.js";import{G as N}from"./PhArrowCounterClockwise.vue.69759bf3.js";import{G as P,F as j,I,a as E}from"./PhIdentificationBadge.vue.c43050df.js";import{F}from"./PhKey.vue.5f2e4d78.js";import{G}from"./PhRobot.vue.b708ebad.js";import"./PhChats.vue.b677740a.js";import"./PhSignOut.vue.24b5579f.js";import"./router.11c85616.js";import"./Badge.89fa8c75.js";import"./index.d6be2ad0.js";import"./Avatar.7dd6bc69.js";import"./index.6c2a02cd.js";import"./index.8875f21d.js";import"./BookOutlined.86454b1a.js";import"./popupNotifcation.527420c3.js";import"./record.68cbec00.js";import"./string.bc06ff97.js";import"./index.787f6cf7.js";import"./AbstraLogo.vue_vue_type_script_setup_true_lang.86e80d08.js";import"./Logo.16b7e007.js";import"./index.ed21ba8c.js";(function(){try{var m=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},r=new Error().stack;r&&(m._sentryDebugIds=m._sentryDebugIds||{},m._sentryDebugIds[r]="0ee6a52e-92fb-40a5-952f-7892a2b16937",m._sentryDebugIdIdentifier="sentry-dbid-0ee6a52e-92fb-40a5-952f-7892a2b16937")}catch{}})();const q=["width","height","fill","transform"],D={key:0},O=o("path",{d:"M196,35.52C177.62,25.51,153.48,20,128,20S78.38,25.51,60,35.52C39.37,46.79,28,62.58,28,80v96c0,17.42,11.37,33.21,32,44.48,18.35,10,42.49,15.52,68,15.52s49.62-5.51,68-15.52c20.66-11.27,32-27.06,32-44.48V80C228,62.58,216.63,46.79,196,35.52ZM204,128c0,17-31.21,36-76,36s-76-19-76-36v-8.46a88.9,88.9,0,0,0,8,4.94c18.35,10,42.49,15.52,68,15.52s49.62-5.51,68-15.52a88.9,88.9,0,0,0,8-4.94ZM128,44c44.79,0,76,19,76,36s-31.21,36-76,36S52,97,52,80,83.21,44,128,44Zm0,168c-44.79,0-76-19-76-36v-8.46a88.9,88.9,0,0,0,8,4.94c18.35,10,42.49,15.52,68,15.52s49.62-5.51,68-15.52a88.9,88.9,0,0,0,8-4.94V176C204,193,172.79,212,128,212Z"},null,-1),R=[O],W={key:1},Q=o("path",{d:"M216,80c0,26.51-39.4,48-88,48S40,106.51,40,80s39.4-48,88-48S216,53.49,216,80Z",opacity:"0.2"},null,-1),T=o("path",{d:"M128,24C74.17,24,32,48.6,32,80v96c0,31.4,42.17,56,96,56s96-24.6,96-56V80C224,48.6,181.83,24,128,24Zm80,104c0,9.62-7.88,19.43-21.61,26.92C170.93,163.35,150.19,168,128,168s-42.93-4.65-58.39-13.08C55.88,147.43,48,137.62,48,128V111.36c17.06,15,46.23,24.64,80,24.64s62.94-9.68,80-24.64ZM69.61,53.08C85.07,44.65,105.81,40,128,40s42.93,4.65,58.39,13.08C200.12,60.57,208,70.38,208,80s-7.88,19.43-21.61,26.92C170.93,115.35,150.19,120,128,120s-42.93-4.65-58.39-13.08C55.88,99.43,48,89.62,48,80S55.88,60.57,69.61,53.08ZM186.39,202.92C170.93,211.35,150.19,216,128,216s-42.93-4.65-58.39-13.08C55.88,195.43,48,185.62,48,176V159.36c17.06,15,46.23,24.64,80,24.64s62.94-9.68,80-24.64V176C208,185.62,200.12,195.43,186.39,202.92Z"},null,-1),K=[Q,T],Y={key:2},J=o("path",{d:"M128,24C74.17,24,32,48.6,32,80v96c0,31.4,42.17,56,96,56s96-24.6,96-56V80C224,48.6,181.83,24,128,24Zm80,104c0,9.62-7.88,19.43-21.61,26.92C170.93,163.35,150.19,168,128,168s-42.93-4.65-58.39-13.08C55.88,147.43,48,137.62,48,128V111.36c17.06,15,46.23,24.64,80,24.64s62.94-9.68,80-24.64Zm-21.61,74.92C170.93,211.35,150.19,216,128,216s-42.93-4.65-58.39-13.08C55.88,195.43,48,185.62,48,176V159.36c17.06,15,46.23,24.64,80,24.64s62.94-9.68,80-24.64V176C208,185.62,200.12,195.43,186.39,202.92Z"},null,-1),U=[J],X={key:3},a1=o("path",{d:"M128,26C75.29,26,34,49.72,34,80v96c0,30.28,41.29,54,94,54s94-23.72,94-54V80C222,49.72,180.71,26,128,26Zm0,12c44.45,0,82,19.23,82,42s-37.55,42-82,42S46,102.77,46,80,83.55,38,128,38Zm82,138c0,22.77-37.55,42-82,42s-82-19.23-82-42V154.79C62,171.16,92.37,182,128,182s66-10.84,82-27.21Zm0-48c0,22.77-37.55,42-82,42s-82-19.23-82-42V106.79C62,123.16,92.37,134,128,134s66-10.84,82-27.21Z"},null,-1),l1=[a1],e1={key:4},t1=o("path",{d:"M128,24C74.17,24,32,48.6,32,80v96c0,31.4,42.17,56,96,56s96-24.6,96-56V80C224,48.6,181.83,24,128,24Zm80,104c0,9.62-7.88,19.43-21.61,26.92C170.93,163.35,150.19,168,128,168s-42.93-4.65-58.39-13.08C55.88,147.43,48,137.62,48,128V111.36c17.06,15,46.23,24.64,80,24.64s62.94-9.68,80-24.64ZM69.61,53.08C85.07,44.65,105.81,40,128,40s42.93,4.65,58.39,13.08C200.12,60.57,208,70.38,208,80s-7.88,19.43-21.61,26.92C170.93,115.35,150.19,120,128,120s-42.93-4.65-58.39-13.08C55.88,99.43,48,89.62,48,80S55.88,60.57,69.61,53.08ZM186.39,202.92C170.93,211.35,150.19,216,128,216s-42.93-4.65-58.39-13.08C55.88,195.43,48,185.62,48,176V159.36c17.06,15,46.23,24.64,80,24.64s62.94-9.68,80-24.64V176C208,185.62,200.12,195.43,186.39,202.92Z"},null,-1),o1=[t1],r1={key:5},i1=o("path",{d:"M192.14,42.55C174.94,33.17,152.16,28,128,28S81.06,33.17,63.86,42.55C45.89,52.35,36,65.65,36,80v96c0,14.35,9.89,27.65,27.86,37.45,17.2,9.38,40,14.55,64.14,14.55s46.94-5.17,64.14-14.55c18-9.8,27.86-23.1,27.86-37.45V80C220,65.65,210.11,52.35,192.14,42.55ZM212,176c0,11.29-8.41,22.1-23.69,30.43C172.27,215.18,150.85,220,128,220s-44.27-4.82-60.31-13.57C52.41,198.1,44,187.29,44,176V149.48c4.69,5.93,11.37,11.34,19.86,16,17.2,9.38,40,14.55,64.14,14.55s46.94-5.17,64.14-14.55c8.49-4.63,15.17-10,19.86-16Zm0-48c0,11.29-8.41,22.1-23.69,30.43C172.27,167.18,150.85,172,128,172s-44.27-4.82-60.31-13.57C52.41,150.1,44,139.29,44,128V101.48c4.69,5.93,11.37,11.34,19.86,16,17.2,9.38,40,14.55,64.14,14.55s46.94-5.17,64.14-14.55c8.49-4.63,15.17-10,19.86-16Zm-23.69-17.57C172.27,119.18,150.85,124,128,124s-44.27-4.82-60.31-13.57C52.41,102.1,44,91.29,44,80s8.41-22.1,23.69-30.43C83.73,40.82,105.15,36,128,36s44.27,4.82,60.31,13.57C203.59,57.9,212,68.71,212,80S203.59,102.1,188.31,110.43Z"},null,-1),n1=[i1],s1={name:"PhDatabase"},c1=A({...s1,props:{weight:{type:String},size:{type:[String,Number]},color:{type:String},mirrored:{type:Boolean}},setup(m){const r=m,d=c("weight","regular"),s=c("size","1em"),g=c("color","currentColor"),p=c("mirrored",!1),l=n(()=>{var a;return(a=r.weight)!=null?a:d}),u=n(()=>{var a;return(a=r.size)!=null?a:s}),i=n(()=>{var a;return(a=r.color)!=null?a:g}),h=n(()=>r.mirrored!==void 0?r.mirrored?"scale(-1, 1)":void 0:p?"scale(-1, 1)":void 0);return(a,L)=>(e(),t("svg",$({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 256 256",width:u.value,height:u.value,fill:i.value,transform:h.value},a.$attrs),[Z(a.$slots,"default"),l.value==="bold"?(e(),t("g",D,R)):l.value==="duotone"?(e(),t("g",W,K)):l.value==="fill"?(e(),t("g",Y,U)):l.value==="light"?(e(),t("g",X,l1)):l.value==="regular"?(e(),t("g",e1,o1)):l.value==="thin"?(e(),t("g",r1,n1)):v("",!0)],16,q))}}),u1=["width","height","fill","transform"],m1={key:0},h1=o("path",{d:"M228,56H160L133.33,36a20.12,20.12,0,0,0-12-4H76A20,20,0,0,0,56,52V72H36A20,20,0,0,0,16,92V204a20,20,0,0,0,20,20H188.89A19.13,19.13,0,0,0,208,204.89V184h20.89A19.13,19.13,0,0,0,248,164.89V76A20,20,0,0,0,228,56ZM184,200H40V96H80l28.8,21.6A12,12,0,0,0,116,120h68Zm40-40H208V116a20,20,0,0,0-20-20H120L93.33,76a20.12,20.12,0,0,0-12-4H80V56h40l28.8,21.6A12,12,0,0,0,156,80h68Z"},null,-1),d1=[h1],p1={key:1},g1=o("path",{d:"M232,80v88.89a7.11,7.11,0,0,1-7.11,7.11H200V112a8,8,0,0,0-8-8H120L90.13,81.6a8,8,0,0,0-4.8-1.6H64V56a8,8,0,0,1,8-8h45.33a8,8,0,0,1,4.8,1.6L152,72h72A8,8,0,0,1,232,80Z",opacity:"0.2"},null,-1),L1=o("path",{d:"M224,64H154.67L126.93,43.2a16.12,16.12,0,0,0-9.6-3.2H72A16,16,0,0,0,56,56V72H40A16,16,0,0,0,24,88V200a16,16,0,0,0,16,16H192.89A15.13,15.13,0,0,0,208,200.89V184h16.89A15.13,15.13,0,0,0,240,168.89V80A16,16,0,0,0,224,64ZM192,200H40V88H85.33l29.87,22.4A8,8,0,0,0,120,112h72Zm32-32H208V112a16,16,0,0,0-16-16H122.67L94.93,75.2a16.12,16.12,0,0,0-9.6-3.2H72V56h45.33L147.2,78.4A8,8,0,0,0,152,80h72Z"},null,-1),A1=[g1,L1],v1={key:2},Z1=o("path",{d:"M224,64H154.67L126.93,43.2a16.12,16.12,0,0,0-9.6-3.2H72A16,16,0,0,0,56,56V72H40A16,16,0,0,0,24,88V200a16,16,0,0,0,16,16H192.89A15.13,15.13,0,0,0,208,200.89V184h16.89A15.13,15.13,0,0,0,240,168.89V80A16,16,0,0,0,224,64Zm0,104H208V112a16,16,0,0,0-16-16H122.67L94.93,75.2a16.12,16.12,0,0,0-9.6-3.2H72V56h45.33L147.2,78.4A8,8,0,0,0,152,80h72Z"},null,-1),$1=[Z1],C1={key:3},y1=o("path",{d:"M224,66H154L125.73,44.8a14,14,0,0,0-8.4-2.8H72A14,14,0,0,0,58,56V74H40A14,14,0,0,0,26,88V200a14,14,0,0,0,14,14H192.89A13.12,13.12,0,0,0,206,200.89V182h18.89A13.12,13.12,0,0,0,238,168.89V80A14,14,0,0,0,224,66ZM194,200.89a1.11,1.11,0,0,1-1.11,1.11H40a2,2,0,0,1-2-2V88a2,2,0,0,1,2-2H85.33a2,2,0,0,1,1.2.4l29.87,22.4A6,6,0,0,0,120,110h72a2,2,0,0,1,2,2Zm32-32a1.11,1.11,0,0,1-1.11,1.11H206V112a14,14,0,0,0-14-14H122L93.73,76.8a14,14,0,0,0-8.4-2.8H70V56a2,2,0,0,1,2-2h45.33a2,2,0,0,1,1.2.4L148.4,76.8A6,6,0,0,0,152,78h72a2,2,0,0,1,2,2Z"},null,-1),M1=[y1],V1={key:4},f1=o("path",{d:"M224,64H154.67L126.93,43.2a16.12,16.12,0,0,0-9.6-3.2H72A16,16,0,0,0,56,56V72H40A16,16,0,0,0,24,88V200a16,16,0,0,0,16,16H192.89A15.13,15.13,0,0,0,208,200.89V184h16.89A15.13,15.13,0,0,0,240,168.89V80A16,16,0,0,0,224,64ZM192,200H40V88H85.33l29.87,22.4A8,8,0,0,0,120,112h72Zm32-32H208V112a16,16,0,0,0-16-16H122.67L94.93,75.2a16.12,16.12,0,0,0-9.6-3.2H72V56h45.33L147.2,78.4A8,8,0,0,0,152,80h72Z"},null,-1),H1=[f1],w1={key:5},b1=o("path",{d:"M224,68H153.33l-28.8-21.6a12.05,12.05,0,0,0-7.2-2.4H72A12,12,0,0,0,60,56V76H40A12,12,0,0,0,28,88V200a12,12,0,0,0,12,12H192.89A11.12,11.12,0,0,0,204,200.89V180h20.89A11.12,11.12,0,0,0,236,168.89V80A12,12,0,0,0,224,68ZM196,200.89a3.12,3.12,0,0,1-3.11,3.11H40a4,4,0,0,1-4-4V88a4,4,0,0,1,4-4H85.33a4,4,0,0,1,2.4.8l29.87,22.4a4,4,0,0,0,2.4.8h72a4,4,0,0,1,4,4Zm32-32a3.12,3.12,0,0,1-3.11,3.11H204V112a12,12,0,0,0-12-12H121.33L92.53,78.4a12.05,12.05,0,0,0-7.2-2.4H68V56a4,4,0,0,1,4-4h45.33a4,4,0,0,1,2.4.8L149.6,75.2a4,4,0,0,0,2.4.8h72a4,4,0,0,1,4,4Z"},null,-1),k1=[b1],S1={name:"PhFolders"},_1=A({...S1,props:{weight:{type:String},size:{type:[String,Number]},color:{type:String},mirrored:{type:Boolean}},setup(m){const r=m,d=c("weight","regular"),s=c("size","1em"),g=c("color","currentColor"),p=c("mirrored",!1),l=n(()=>{var a;return(a=r.weight)!=null?a:d}),u=n(()=>{var a;return(a=r.size)!=null?a:s}),i=n(()=>{var a;return(a=r.color)!=null?a:g}),h=n(()=>r.mirrored!==void 0?r.mirrored?"scale(-1, 1)":void 0:p?"scale(-1, 1)":void 0);return(a,L)=>(e(),t("svg",$({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 256 256",width:u.value,height:u.value,fill:i.value,transform:h.value},a.$attrs),[Z(a.$slots,"default"),l.value==="bold"?(e(),t("g",m1,d1)):l.value==="duotone"?(e(),t("g",p1,A1)):l.value==="fill"?(e(),t("g",v1,$1)):l.value==="light"?(e(),t("g",C1,M1)):l.value==="regular"?(e(),t("g",V1,H1)):l.value==="thin"?(e(),t("g",w1,k1)):v("",!0)],16,u1))}}),z1=["width","height","fill","transform"],B1={key:0},x1=o("path",{d:"M128,76a52,52,0,1,0,52,52A52.06,52.06,0,0,0,128,76Zm0,80a28,28,0,1,1,28-28A28,28,0,0,1,128,156Zm113.86-49.57A12,12,0,0,0,236,98.34L208.21,82.49l-.11-31.31a12,12,0,0,0-4.25-9.12,116,116,0,0,0-38-21.41,12,12,0,0,0-9.68.89L128,37.27,99.83,21.53a12,12,0,0,0-9.7-.9,116.06,116.06,0,0,0-38,21.47,12,12,0,0,0-4.24,9.1l-.14,31.34L20,98.35a12,12,0,0,0-5.85,8.11,110.7,110.7,0,0,0,0,43.11A12,12,0,0,0,20,157.66l27.82,15.85.11,31.31a12,12,0,0,0,4.25,9.12,116,116,0,0,0,38,21.41,12,12,0,0,0,9.68-.89L128,218.73l28.14,15.74a12,12,0,0,0,9.7.9,116.06,116.06,0,0,0,38-21.47,12,12,0,0,0,4.24-9.1l.14-31.34,27.81-15.81a12,12,0,0,0,5.85-8.11A110.7,110.7,0,0,0,241.86,106.43Zm-22.63,33.18-26.88,15.28a11.94,11.94,0,0,0-4.55,4.59c-.54,1-1.11,1.93-1.7,2.88a12,12,0,0,0-1.83,6.31L184.13,199a91.83,91.83,0,0,1-21.07,11.87l-27.15-15.19a12,12,0,0,0-5.86-1.53h-.29c-1.14,0-2.3,0-3.44,0a12.08,12.08,0,0,0-6.14,1.51L93,210.82A92.27,92.27,0,0,1,71.88,199l-.11-30.24a12,12,0,0,0-1.83-6.32c-.58-.94-1.16-1.91-1.7-2.88A11.92,11.92,0,0,0,63.7,155L36.8,139.63a86.53,86.53,0,0,1,0-23.24l26.88-15.28a12,12,0,0,0,4.55-4.58c.54-1,1.11-1.94,1.7-2.89a12,12,0,0,0,1.83-6.31L71.87,57A91.83,91.83,0,0,1,92.94,45.17l27.15,15.19a11.92,11.92,0,0,0,6.15,1.52c1.14,0,2.3,0,3.44,0a12.08,12.08,0,0,0,6.14-1.51L163,45.18A92.27,92.27,0,0,1,184.12,57l.11,30.24a12,12,0,0,0,1.83,6.32c.58.94,1.16,1.91,1.7,2.88A11.92,11.92,0,0,0,192.3,101l26.9,15.33A86.53,86.53,0,0,1,219.23,139.61Z"},null,-1),N1=[x1],P1={key:1},j1=o("path",{d:"M230.1,108.76,198.25,90.62c-.64-1.16-1.31-2.29-2-3.41l-.12-36A104.61,104.61,0,0,0,162,32L130,49.89c-1.34,0-2.69,0-4,0L94,32A104.58,104.58,0,0,0,59.89,51.25l-.16,36c-.7,1.12-1.37,2.26-2,3.41l-31.84,18.1a99.15,99.15,0,0,0,0,38.46l31.85,18.14c.64,1.16,1.31,2.29,2,3.41l.12,36A104.61,104.61,0,0,0,94,224l32-17.87c1.34,0,2.69,0,4,0L162,224a104.58,104.58,0,0,0,34.08-19.25l.16-36c.7-1.12,1.37-2.26,2-3.41l31.84-18.1A99.15,99.15,0,0,0,230.1,108.76ZM128,168a40,40,0,1,1,40-40A40,40,0,0,1,128,168Z",opacity:"0.2"},null,-1),I1=o("path",{d:"M128,80a48,48,0,1,0,48,48A48.05,48.05,0,0,0,128,80Zm0,80a32,32,0,1,1,32-32A32,32,0,0,1,128,160Zm109.94-52.79a8,8,0,0,0-3.89-5.4l-29.83-17-.12-33.62a8,8,0,0,0-2.83-6.08,111.91,111.91,0,0,0-36.72-20.67,8,8,0,0,0-6.46.59L128,41.85,97.88,25a8,8,0,0,0-6.47-.6A111.92,111.92,0,0,0,54.73,45.15a8,8,0,0,0-2.83,6.07l-.15,33.65-29.83,17a8,8,0,0,0-3.89,5.4,106.47,106.47,0,0,0,0,41.56,8,8,0,0,0,3.89,5.4l29.83,17,.12,33.63a8,8,0,0,0,2.83,6.08,111.91,111.91,0,0,0,36.72,20.67,8,8,0,0,0,6.46-.59L128,214.15,158.12,231a7.91,7.91,0,0,0,3.9,1,8.09,8.09,0,0,0,2.57-.42,112.1,112.1,0,0,0,36.68-20.73,8,8,0,0,0,2.83-6.07l.15-33.65,29.83-17a8,8,0,0,0,3.89-5.4A106.47,106.47,0,0,0,237.94,107.21Zm-15,34.91-28.57,16.25a8,8,0,0,0-3,3c-.58,1-1.19,2.06-1.81,3.06a7.94,7.94,0,0,0-1.22,4.21l-.15,32.25a95.89,95.89,0,0,1-25.37,14.3L134,199.13a8,8,0,0,0-3.91-1h-.19c-1.21,0-2.43,0-3.64,0a8.1,8.1,0,0,0-4.1,1l-28.84,16.1A96,96,0,0,1,67.88,201l-.11-32.2a8,8,0,0,0-1.22-4.22c-.62-1-1.23-2-1.8-3.06a8.09,8.09,0,0,0-3-3.06l-28.6-16.29a90.49,90.49,0,0,1,0-28.26L61.67,97.63a8,8,0,0,0,3-3c.58-1,1.19-2.06,1.81-3.06a7.94,7.94,0,0,0,1.22-4.21l.15-32.25a95.89,95.89,0,0,1,25.37-14.3L122,56.87a8,8,0,0,0,4.1,1c1.21,0,2.43,0,3.64,0a8,8,0,0,0,4.1-1l28.84-16.1A96,96,0,0,1,188.12,55l.11,32.2a8,8,0,0,0,1.22,4.22c.62,1,1.23,2,1.8,3.06a8.09,8.09,0,0,0,3,3.06l28.6,16.29A90.49,90.49,0,0,1,222.9,142.12Z"},null,-1),E1=[j1,I1],F1={key:2},G1=o("path",{d:"M237.94,107.21a8,8,0,0,0-3.89-5.4l-29.83-17-.12-33.62a8,8,0,0,0-2.83-6.08,111.91,111.91,0,0,0-36.72-20.67,8,8,0,0,0-6.46.59L128,41.85,97.88,25a8,8,0,0,0-6.47-.6A111.92,111.92,0,0,0,54.73,45.15a8,8,0,0,0-2.83,6.07l-.15,33.65-29.83,17a8,8,0,0,0-3.89,5.4,106.47,106.47,0,0,0,0,41.56,8,8,0,0,0,3.89,5.4l29.83,17,.12,33.63a8,8,0,0,0,2.83,6.08,111.91,111.91,0,0,0,36.72,20.67,8,8,0,0,0,6.46-.59L128,214.15,158.12,231a7.91,7.91,0,0,0,3.9,1,8.09,8.09,0,0,0,2.57-.42,112.1,112.1,0,0,0,36.68-20.73,8,8,0,0,0,2.83-6.07l.15-33.65,29.83-17a8,8,0,0,0,3.89-5.4A106.47,106.47,0,0,0,237.94,107.21ZM128,168a40,40,0,1,1,40-40A40,40,0,0,1,128,168Z"},null,-1),q1=[G1],D1={key:3},O1=o("path",{d:"M128,82a46,46,0,1,0,46,46A46.06,46.06,0,0,0,128,82Zm0,80a34,34,0,1,1,34-34A34,34,0,0,1,128,162Zm108-54.4a6,6,0,0,0-2.92-4L202.64,86.22l-.42-.71L202.1,51.2A6,6,0,0,0,200,46.64a110.12,110.12,0,0,0-36.07-20.31,6,6,0,0,0-4.84.45L128.46,43.86h-1L96.91,26.76a6,6,0,0,0-4.86-.44A109.92,109.92,0,0,0,56,46.68a6,6,0,0,0-2.12,4.55l-.16,34.34c-.14.23-.28.47-.41.71L22.91,103.57A6,6,0,0,0,20,107.62a104.81,104.81,0,0,0,0,40.78,6,6,0,0,0,2.92,4l30.42,17.33.42.71.12,34.31A6,6,0,0,0,56,209.36a110.12,110.12,0,0,0,36.07,20.31,6,6,0,0,0,4.84-.45l30.61-17.08h1l30.56,17.1A6.09,6.09,0,0,0,162,230a5.83,5.83,0,0,0,1.93-.32,109.92,109.92,0,0,0,36-20.36,6,6,0,0,0,2.12-4.55l.16-34.34c.14-.23.28-.47.41-.71l30.42-17.29a6,6,0,0,0,2.92-4.05A104.81,104.81,0,0,0,236,107.6Zm-11.25,35.79L195.32,160.1a6.07,6.07,0,0,0-2.28,2.3c-.59,1-1.21,2.11-1.86,3.14a6,6,0,0,0-.91,3.16l-.16,33.21a98.15,98.15,0,0,1-27.52,15.53L133,200.88a6,6,0,0,0-2.93-.77h-.14c-1.24,0-2.5,0-3.74,0a6,6,0,0,0-3.07.76L93.45,217.43a98,98,0,0,1-27.56-15.49l-.12-33.17a6,6,0,0,0-.91-3.16c-.64-1-1.27-2.08-1.86-3.14a6,6,0,0,0-2.27-2.3L31.3,143.4a93,93,0,0,1,0-30.79L60.68,95.9A6.07,6.07,0,0,0,63,93.6c.59-1,1.21-2.11,1.86-3.14a6,6,0,0,0,.91-3.16l.16-33.21A98.15,98.15,0,0,1,93.41,38.56L123,55.12a5.81,5.81,0,0,0,3.07.76c1.24,0,2.5,0,3.74,0a6,6,0,0,0,3.07-.76l29.65-16.56a98,98,0,0,1,27.56,15.49l.12,33.17a6,6,0,0,0,.91,3.16c.64,1,1.27,2.08,1.86,3.14a6,6,0,0,0,2.27,2.3L224.7,112.6A93,93,0,0,1,224.73,143.39Z"},null,-1),R1=[O1],W1={key:4},Q1=o("path",{d:"M128,80a48,48,0,1,0,48,48A48.05,48.05,0,0,0,128,80Zm0,80a32,32,0,1,1,32-32A32,32,0,0,1,128,160Zm109.94-52.79a8,8,0,0,0-3.89-5.4l-29.83-17-.12-33.62a8,8,0,0,0-2.83-6.08,111.91,111.91,0,0,0-36.72-20.67,8,8,0,0,0-6.46.59L128,41.85,97.88,25a8,8,0,0,0-6.47-.6A112.1,112.1,0,0,0,54.73,45.15a8,8,0,0,0-2.83,6.07l-.15,33.65-29.83,17a8,8,0,0,0-3.89,5.4,106.47,106.47,0,0,0,0,41.56,8,8,0,0,0,3.89,5.4l29.83,17,.12,33.62a8,8,0,0,0,2.83,6.08,111.91,111.91,0,0,0,36.72,20.67,8,8,0,0,0,6.46-.59L128,214.15,158.12,231a7.91,7.91,0,0,0,3.9,1,8.09,8.09,0,0,0,2.57-.42,112.1,112.1,0,0,0,36.68-20.73,8,8,0,0,0,2.83-6.07l.15-33.65,29.83-17a8,8,0,0,0,3.89-5.4A106.47,106.47,0,0,0,237.94,107.21Zm-15,34.91-28.57,16.25a8,8,0,0,0-3,3c-.58,1-1.19,2.06-1.81,3.06a7.94,7.94,0,0,0-1.22,4.21l-.15,32.25a95.89,95.89,0,0,1-25.37,14.3L134,199.13a8,8,0,0,0-3.91-1h-.19c-1.21,0-2.43,0-3.64,0a8.08,8.08,0,0,0-4.1,1l-28.84,16.1A96,96,0,0,1,67.88,201l-.11-32.2a8,8,0,0,0-1.22-4.22c-.62-1-1.23-2-1.8-3.06a8.09,8.09,0,0,0-3-3.06l-28.6-16.29a90.49,90.49,0,0,1,0-28.26L61.67,97.63a8,8,0,0,0,3-3c.58-1,1.19-2.06,1.81-3.06a7.94,7.94,0,0,0,1.22-4.21l.15-32.25a95.89,95.89,0,0,1,25.37-14.3L122,56.87a8,8,0,0,0,4.1,1c1.21,0,2.43,0,3.64,0a8.08,8.08,0,0,0,4.1-1l28.84-16.1A96,96,0,0,1,188.12,55l.11,32.2a8,8,0,0,0,1.22,4.22c.62,1,1.23,2,1.8,3.06a8.09,8.09,0,0,0,3,3.06l28.6,16.29A90.49,90.49,0,0,1,222.9,142.12Z"},null,-1),T1=[Q1],K1={key:5},Y1=o("path",{d:"M128,84a44,44,0,1,0,44,44A44.05,44.05,0,0,0,128,84Zm0,80a36,36,0,1,1,36-36A36,36,0,0,1,128,164Zm106-56a4,4,0,0,0-2-2.7l-30.89-17.6q-.47-.82-1-1.62L200.1,51.2a3.94,3.94,0,0,0-1.42-3,107.8,107.8,0,0,0-35.41-19.94,4,4,0,0,0-3.23.29L129,45.87h-2l-31-17.36a4,4,0,0,0-3.23-.3,108.05,108.05,0,0,0-35.39,20,4,4,0,0,0-1.41,3l-.16,34.9-1,1.62L23.9,105.3A4,4,0,0,0,22,108a102.76,102.76,0,0,0,0,40,4,4,0,0,0,1.95,2.7l30.89,17.6q.47.83,1,1.62l.12,34.87a3.94,3.94,0,0,0,1.42,3,107.8,107.8,0,0,0,35.41,19.94,4,4,0,0,0,3.23-.29L127,210.13h2l31,17.36a4,4,0,0,0,3.23.3,108.05,108.05,0,0,0,35.39-20,4,4,0,0,0,1.41-3l.16-34.9,1-1.62L232.1,150.7a4,4,0,0,0,2-2.71A102.76,102.76,0,0,0,234,108Zm-7.48,36.67L196.3,161.84a4,4,0,0,0-1.51,1.53c-.61,1.09-1.25,2.17-1.91,3.24a3.92,3.92,0,0,0-.61,2.1l-.16,34.15a99.8,99.8,0,0,1-29.7,16.77l-30.4-17a4.06,4.06,0,0,0-2-.51H130c-1.28,0-2.57,0-3.84,0a4.1,4.1,0,0,0-2.05.51l-30.45,17A100.23,100.23,0,0,1,63.89,202.9l-.12-34.12a3.93,3.93,0,0,0-.61-2.11c-.66-1-1.3-2.14-1.91-3.23a4,4,0,0,0-1.51-1.53L29.49,144.68a94.78,94.78,0,0,1,0-33.34L59.7,94.16a4,4,0,0,0,1.51-1.53c.61-1.09,1.25-2.17,1.91-3.23a4,4,0,0,0,.61-2.11l.16-34.15a99.8,99.8,0,0,1,29.7-16.77l30.4,17a4.1,4.1,0,0,0,2.05.51c1.28,0,2.57,0,3.84,0a4,4,0,0,0,2.05-.51l30.45-17A100.23,100.23,0,0,1,192.11,53.1l.12,34.12a3.93,3.93,0,0,0,.61,2.11c.66,1,1.3,2.14,1.91,3.23a4,4,0,0,0,1.51,1.53l30.25,17.23A94.78,94.78,0,0,1,226.54,144.66Z"},null,-1),J1=[Y1],U1={name:"PhGearSix"},X1=A({...U1,props:{weight:{type:String},size:{type:[String,Number]},color:{type:String},mirrored:{type:Boolean}},setup(m){const r=m,d=c("weight","regular"),s=c("size","1em"),g=c("color","currentColor"),p=c("mirrored",!1),l=n(()=>{var a;return(a=r.weight)!=null?a:d}),u=n(()=>{var a;return(a=r.size)!=null?a:s}),i=n(()=>{var a;return(a=r.color)!=null?a:g}),h=n(()=>r.mirrored!==void 0?r.mirrored?"scale(-1, 1)":void 0:p?"scale(-1, 1)":void 0);return(a,L)=>(e(),t("svg",$({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 256 256",width:u.value,height:u.value,fill:i.value,transform:h.value},a.$attrs),[Z(a.$slots,"default"),l.value==="bold"?(e(),t("g",B1,N1)):l.value==="duotone"?(e(),t("g",P1,E1)):l.value==="fill"?(e(),t("g",F1,q1)):l.value==="light"?(e(),t("g",D1,R1)):l.value==="regular"?(e(),t("g",W1,T1)):l.value==="thin"?(e(),t("g",K1,J1)):v("",!0)],16,z1))}}),a0=["width","height","fill","transform"],l0={key:0},e0=o("path",{d:"M240.49,63.51a12,12,0,0,0-17,0L192,95,161,64l31.52-31.51a12,12,0,0,0-17-17L144,47,120.49,23.51a12,12,0,1,0-17,17L107,44,56.89,94.14a44,44,0,0,0,0,62.23l12.88,12.88L23.51,215.51a12,12,0,0,0,17,17l46.26-46.26,12.88,12.88a44,44,0,0,0,62.23,0L212,149l3.51,3.52a12,12,0,0,0,17-17L209,112l31.52-31.51A12,12,0,0,0,240.49,63.51Zm-95.6,118.63a20,20,0,0,1-28.29,0L73.86,139.4a20,20,0,0,1,0-28.29L124,61l71,71Z"},null,-1),t0=[e0],o0={key:1},r0=o("path",{d:"M212,132l-58.63,58.63a32,32,0,0,1-45.25,0L65.37,147.88a32,32,0,0,1,0-45.25L124,44Z",opacity:"0.2"},null,-1),i0=o("path",{d:"M237.66,66.34a8,8,0,0,0-11.32,0L192,100.69,155.31,64l34.35-34.34a8,8,0,1,0-11.32-11.32L144,52.69,117.66,26.34a8,8,0,0,0-11.32,11.32L112.69,44l-53,53a40,40,0,0,0,0,56.57l15.71,15.71L26.34,218.34a8,8,0,0,0,11.32,11.32l49.09-49.09,15.71,15.71a40,40,0,0,0,56.57,0l53-53,6.34,6.35a8,8,0,0,0,11.32-11.32L203.31,112l34.35-34.34A8,8,0,0,0,237.66,66.34ZM147.72,185a24,24,0,0,1-33.95,0L71,142.23a24,24,0,0,1,0-33.95l53-53L200.69,132Z"},null,-1),n0=[r0,i0],s0={key:2},c0=o("path",{d:"M237.66,77.66,203.31,112l26.35,26.34a8,8,0,0,1-11.32,11.32L212,143.31l-53,53a40,40,0,0,1-56.57,0L86.75,180.57,37.66,229.66a8,8,0,0,1-11.32-11.32l49.09-49.09L59.72,153.54a40,40,0,0,1,0-56.57l53-53-6.35-6.34a8,8,0,0,1,11.32-11.32L144,52.69l34.34-34.35a8,8,0,1,1,11.32,11.32L155.31,64,192,100.69l34.34-34.35a8,8,0,0,1,11.32,11.32Z"},null,-1),u0=[c0],m0={key:3},h0=o("path",{d:"M236.24,67.76a6,6,0,0,0-8.48,0L192,103.51,152.49,64l35.75-35.76a6,6,0,0,0-8.48-8.48L144,55.51,116.24,27.76a6,6,0,1,0-8.48,8.48L115.51,44,61.13,98.38a38,38,0,0,0,0,53.75l17.13,17.12-50.5,50.51a6,6,0,1,0,8.48,8.48l50.51-50.5,17.13,17.13a38,38,0,0,0,53.74,0L212,140.49l7.76,7.75a6,6,0,0,0,8.48-8.48L200.49,112l35.75-35.76A6,6,0,0,0,236.24,67.76ZM149.13,186.38a26,26,0,0,1-36.77,0L69.62,143.64a26,26,0,0,1,0-36.77L124,52.49,203.51,132Z"},null,-1),d0=[h0],p0={key:4},g0=o("path",{d:"M237.66,66.34a8,8,0,0,0-11.32,0L192,100.69,155.31,64l34.35-34.34a8,8,0,1,0-11.32-11.32L144,52.69,117.66,26.34a8,8,0,0,0-11.32,11.32L112.69,44l-53,53a40,40,0,0,0,0,56.57l15.71,15.71L26.34,218.34a8,8,0,0,0,11.32,11.32l49.09-49.09,15.71,15.71a40,40,0,0,0,56.57,0l53-53,6.34,6.35a8,8,0,0,0,11.32-11.32L203.31,112l34.35-34.34A8,8,0,0,0,237.66,66.34ZM147.72,185a24,24,0,0,1-33.95,0L71,142.23a24,24,0,0,1,0-33.95l53-53L200.69,132Z"},null,-1),L0=[g0],A0={key:5},v0=o("path",{d:"M234.83,69.17a4,4,0,0,0-5.66,0L192,106.34,149.66,64l37.17-37.17a4,4,0,1,0-5.66-5.66L144,58.34,114.83,29.17a4,4,0,0,0-5.66,5.66L118.34,44,62.54,99.8a36.05,36.05,0,0,0,0,50.91l18.55,18.54L29.17,221.17a4,4,0,0,0,5.66,5.66l51.92-51.92,18.54,18.55a36.06,36.06,0,0,0,50.91,0l55.8-55.8,9.17,9.17a4,4,0,0,0,5.66-5.66L197.66,112l37.17-37.17A4,4,0,0,0,234.83,69.17ZM150.54,187.8a28,28,0,0,1-39.59,0L68.2,145.05a28,28,0,0,1,0-39.59L124,49.66,206.34,132Z"},null,-1),Z0=[v0],$0={name:"PhPlug"},C0=A({...$0,props:{weight:{type:String},size:{type:[String,Number]},color:{type:String},mirrored:{type:Boolean}},setup(m){const r=m,d=c("weight","regular"),s=c("size","1em"),g=c("color","currentColor"),p=c("mirrored",!1),l=n(()=>{var a;return(a=r.weight)!=null?a:d}),u=n(()=>{var a;return(a=r.size)!=null?a:s}),i=n(()=>{var a;return(a=r.color)!=null?a:g}),h=n(()=>r.mirrored!==void 0?r.mirrored?"scale(-1, 1)":void 0:p?"scale(-1, 1)":void 0);return(a,L)=>(e(),t("svg",$({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 256 256",width:u.value,height:u.value,fill:i.value,transform:h.value},a.$attrs),[Z(a.$slots,"default"),l.value==="bold"?(e(),t("g",l0,t0)):l.value==="duotone"?(e(),t("g",o0,n0)):l.value==="fill"?(e(),t("g",s0,u0)):l.value==="light"?(e(),t("g",m0,d0)):l.value==="regular"?(e(),t("g",p0,L0)):l.value==="thin"?(e(),t("g",A0,Z0)):v("",!0)],16,a0))}}),y0=["width","height","fill","transform"],M0={key:0},V0=o("path",{d:"M156,228a12,12,0,0,1-12,12H112a12,12,0,0,1,0-24h32A12,12,0,0,1,156,228ZM128,116a16,16,0,1,0-16-16A16,16,0,0,0,128,116Zm99.53,40.7-12.36,55.63a19.9,19.9,0,0,1-12.88,14.53A20.16,20.16,0,0,1,195.6,228a19.87,19.87,0,0,1-12.29-4.27L157.17,204H98.83L72.69,223.74A19.87,19.87,0,0,1,60.4,228a20.16,20.16,0,0,1-6.69-1.15,19.9,19.9,0,0,1-12.88-14.53L28.47,156.7a20.1,20.1,0,0,1,4.16-17.14l27.83-33.4A127,127,0,0,1,69.11,69.7c13.27-33.25,37-54.1,46.64-61.52a20,20,0,0,1,24.5,0c9.6,7.42,33.37,28.27,46.64,61.52a127,127,0,0,1,8.65,36.46l27.83,33.4A20.1,20.1,0,0,1,227.53,156.7ZM101.79,180h52.42c19.51-35.7,23-69.78,10.39-101.4C154.4,53,136.2,35.9,128,29.12,119.8,35.9,101.6,53,91.4,78.6,78.78,110.22,82.28,144.3,101.79,180Zm-22.55,8.72a168,168,0,0,1-16.92-47.3l-10,12,10.58,47.64Zm124.43-35.31-10-12a168,168,0,0,1-16.92,47.3l16.33,12.33Z"},null,-1),f0=[V0],H0={key:1},w0=o("path",{d:"M94.81,192,65.36,214.24a8,8,0,0,1-12.81-4.51L40.19,154.1a8,8,0,0,1,1.66-6.86l30.31-36.33C71,134.25,76.7,161.43,94.81,192Zm119.34-44.76-30.31-36.33c1.21,23.34-4.54,50.52-22.65,81.09l29.45,22.24a8,8,0,0,0,12.81-4.51l12.36-55.63A8,8,0,0,0,214.15,147.24Z",opacity:"0.2"},null,-1),b0=o("path",{d:"M152,224a8,8,0,0,1-8,8H112a8,8,0,0,1,0-16h32A8,8,0,0,1,152,224ZM128,112a12,12,0,1,0-12-12A12,12,0,0,0,128,112Zm95.62,43.83-12.36,55.63a16,16,0,0,1-25.51,9.11L158.51,200h-61L70.25,220.57a16,16,0,0,1-25.51-9.11L32.38,155.83a16.09,16.09,0,0,1,3.32-13.71l28.56-34.26a123.07,123.07,0,0,1,8.57-36.67c12.9-32.34,36-52.63,45.37-59.85a16,16,0,0,1,19.6,0c9.34,7.22,32.47,27.51,45.37,59.85a123.07,123.07,0,0,1,8.57,36.67l28.56,34.26A16.09,16.09,0,0,1,223.62,155.83ZM99.43,184h57.14c21.12-37.54,25.07-73.48,11.74-106.88C156.55,47.64,134.49,29,128,24c-6.51,5-28.57,23.64-40.33,53.12C74.36,110.52,78.31,146.46,99.43,184Zm-15,5.85Q68.28,160.5,64.83,132.16L48,152.36,60.36,208l.18-.13ZM208,152.36l-16.83-20.2q-3.42,28.28-19.56,57.69l23.85,18,.18.13Z"},null,-1),k0=[w0,b0],S0={key:2},_0=o("path",{d:"M152,224a8,8,0,0,1-8,8H112a8,8,0,0,1,0-16h32A8,8,0,0,1,152,224Zm71.62-68.17-12.36,55.63a16,16,0,0,1-25.51,9.11L158.51,200h-61L70.25,220.57a16,16,0,0,1-25.51-9.11L32.38,155.83a16.09,16.09,0,0,1,3.32-13.71l28.56-34.26a123.07,123.07,0,0,1,8.57-36.67c12.9-32.34,36-52.63,45.37-59.85a16,16,0,0,1,19.6,0c9.34,7.22,32.47,27.51,45.37,59.85a123.07,123.07,0,0,1,8.57,36.67l28.56,34.26A16.09,16.09,0,0,1,223.62,155.83Zm-139.23,34Q68.28,160.5,64.83,132.16L48,152.36,60.36,208l.18-.13ZM140,100a12,12,0,1,0-12,12A12,12,0,0,0,140,100Zm68,52.36-16.83-20.2q-3.42,28.28-19.56,57.69l23.85,18,.18.13Z"},null,-1),z0=[_0],B0={key:3},x0=o("path",{d:"M150,224a6,6,0,0,1-6,6H112a6,6,0,0,1,0-12h32A6,6,0,0,1,150,224ZM128,110a10,10,0,1,0-10-10A10,10,0,0,0,128,110Zm93.67,45.4L209.31,211A14,14,0,0,1,187,219l-27.79-21H96.82L69,219a14,14,0,0,1-22.34-8L34.33,155.4a14.06,14.06,0,0,1,2.91-12l29-34.76a121.28,121.28,0,0,1,8.48-36.71c12.72-31.88,35.52-51.88,44.73-59a14,14,0,0,1,17.16,0c9.21,7.12,32,27.12,44.73,59a121.28,121.28,0,0,1,8.48,36.71l29,34.76A14.06,14.06,0,0,1,221.67,155.4ZM98.26,186h59.48c21.93-38.46,26.12-75.33,12.43-109.62-11.95-30-34.35-48.87-40.93-54a2,2,0,0,0-2.48,0c-6.58,5.09-29,24-40.93,54C72.14,110.67,76.33,147.54,98.26,186ZM87,190.4c-12-21.49-18.9-42.6-20.62-63.19L46.46,151.08a2,2,0,0,0-.42,1.71l12.37,55.64a2,2,0,0,0,3.2,1.13l.13-.11Zm122.57-39.32-19.89-23.87c-1.72,20.59-8.6,41.7-20.62,63.19l25.23,19,.13.11a2,2,0,0,0,3.2-1.13L210,152.79A2,2,0,0,0,209.54,151.08Z"},null,-1),N0=[x0],P0={key:4},j0=o("path",{d:"M152,224a8,8,0,0,1-8,8H112a8,8,0,0,1,0-16h32A8,8,0,0,1,152,224ZM128,112a12,12,0,1,0-12-12A12,12,0,0,0,128,112Zm95.62,43.83-12.36,55.63a16,16,0,0,1-25.51,9.11L158.51,200h-61L70.25,220.57a16,16,0,0,1-25.51-9.11L32.38,155.83a16.09,16.09,0,0,1,3.32-13.71l28.56-34.26a123.07,123.07,0,0,1,8.57-36.67c12.9-32.34,36-52.63,45.37-59.85a16,16,0,0,1,19.6,0c9.34,7.22,32.47,27.51,45.37,59.85a123.07,123.07,0,0,1,8.57,36.67l28.56,34.26A16.09,16.09,0,0,1,223.62,155.83ZM99.43,184h57.14c21.12-37.54,25.07-73.48,11.74-106.88C156.55,47.64,134.49,29,128,24c-6.51,5-28.57,23.64-40.33,53.12C74.36,110.52,78.31,146.46,99.43,184Zm-15,5.85Q68.28,160.5,64.83,132.16L48,152.36,60.36,208l.18-.13ZM208,152.36l-16.83-20.2q-3.42,28.28-19.56,57.69l23.85,18,.18.13Z"},null,-1),I0=[j0],E0={key:5},F0=o("path",{d:"M148,224a4,4,0,0,1-4,4H112a4,4,0,0,1,0-8h32A4,4,0,0,1,148,224ZM128,108a8,8,0,1,0-8-8A8,8,0,0,0,128,108Zm91.72,47L207.35,210.6a11.9,11.9,0,0,1-7.72,8.71,12.17,12.17,0,0,1-4,.69,11.94,11.94,0,0,1-7.43-2.6L159.85,196H96.15L67.81,217.4a11.94,11.94,0,0,1-7.43,2.6,12.17,12.17,0,0,1-4-.69,11.9,11.9,0,0,1-7.72-8.71L36.28,155a12,12,0,0,1,2.5-10.28l29.35-35.23c3.3-53.33,41.83-86.68,52.52-94.94a12,12,0,0,1,14.7,0c10.69,8.26,49.22,41.61,52.52,94.94l29.35,35.23A12,12,0,0,1,219.72,155ZM97.11,188h61.78C214.07,92.49,145,32.05,130.46,20.84a4,4,0,0,0-4.92,0C111,32.05,41.93,92.49,97.11,188Zm-7.52,2.93C75.12,165.56,68.93,142.52,68,122.06L44.92,149.8a4,4,0,0,0-.83,3.43l12.36,55.63a4,4,0,0,0,6.41,2.26l.09-.07ZM211.08,149.8,188,122.06c-.89,20.46-7.08,43.5-21.55,68.87l26.64,20.12.09.07a4,4,0,0,0,6.41-2.26l12.36-55.63A4,4,0,0,0,211.08,149.8Z"},null,-1),G0=[F0],q0={name:"PhRocket"},D0=A({...q0,props:{weight:{type:String},size:{type:[String,Number]},color:{type:String},mirrored:{type:Boolean}},setup(m){const r=m,d=c("weight","regular"),s=c("size","1em"),g=c("color","currentColor"),p=c("mirrored",!1),l=n(()=>{var a;return(a=r.weight)!=null?a:d}),u=n(()=>{var a;return(a=r.size)!=null?a:s}),i=n(()=>{var a;return(a=r.color)!=null?a:g}),h=n(()=>r.mirrored!==void 0?r.mirrored?"scale(-1, 1)":void 0:p?"scale(-1, 1)":void 0);return(a,L)=>(e(),t("svg",$({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 256 256",width:u.value,height:u.value,fill:i.value,transform:h.value},a.$attrs),[Z(a.$slots,"default"),l.value==="bold"?(e(),t("g",M0,f0)):l.value==="duotone"?(e(),t("g",H0,k0)):l.value==="fill"?(e(),t("g",S0,z0)):l.value==="light"?(e(),t("g",B0,N0)):l.value==="regular"?(e(),t("g",P0,I0)):l.value==="thin"?(e(),t("g",E0,G0)):v("",!0)],16,y0))}}),O0=A({__name:"Project",setup(m){const d=w().params.projectId,{result:s}=H(()=>_.get(d).then(async i=>{const h=await S.get(i.organizationId);return{project:i,organization:h}})),g=n(()=>{var i,h,a,L;return((i=s.value)==null?void 0:i.organization)&&s.value.project?[{label:"My organizations",path:"/organizations"},{label:(a=(h=s.value)==null?void 0:h.organization)==null?void 0:a.name,path:`/organizations/${(L=s.value)==null?void 0:L.organization.id}`},{label:s.value.project.name,path:`/projects/${s.value.project.id}`}]:void 0}),p=n(()=>{var i;return(i=s.value)==null?void 0:i.organization.billingMetadata}),l=n(()=>{var i;return(i=s.value)==null?void 0:i.organization.id}),u=n(()=>{var i;return(i=s.value)!=null&&i.project?[{name:"Monitoring",items:[{name:"Stages",path:"live",icon:P},{name:"Builds",path:"builds",icon:D0},{name:"Logs",icon:N,path:"logs"},{name:"Tasks",path:"tasks",icon:j}]},{name:"Resources",items:[{name:"Tables",path:"tables",icon:c1},{name:"Files",path:"files",icon:_1},{name:"Connectors",path:"connectors",icon:C0,unavailable:!s.value.organization.featureFlags.CONNECTORS_CONSOLE},{name:"Agents",path:"agents",icon:G,unavailable:!s.value.organization.featureFlags.CONNECTORS_CONSOLE}]},{name:"Configuration",items:[{name:"API Keys",path:"api-keys",icon:F},{name:"Env Vars",path:"env-vars",icon:I},{name:"Subdomain",icon:X1,path:"settings"},{name:"Access Control",icon:E,path:"access-control"}]}]:[]});return(i,h)=>{const a=b("RouterView");return e(),M(f,null,{content:C(()=>[y(x,null,{default:C(()=>[p.value&&l.value?(e(),M(z,{key:0,"billing-metadata":p.value,"organization-id":l.value},null,8,["billing-metadata","organization-id"])):v("",!0),y(a)]),_:1})]),navbar:C(()=>[y(V,{class:"nav",breadcrumb:g.value},null,8,["breadcrumb"])]),sidebar:C(()=>[y(B,{class:"sidebar",sections:u.value},null,8,["sections"])]),_:1})}}});const C2=k(O0,[["__scopeId","data-v-7a704e7c"]]);export{C2 as default};
//# sourceMappingURL=Project.84f480ed.js.map
