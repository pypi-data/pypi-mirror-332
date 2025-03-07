"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[204],{27784:function(e,t,n){n.d(t,{Z:function(){return X}});var r=n(27573),i=n(7653),a=n(5772),s=n(13908),o=n(80840),l=n(87285),d=n(70790),c=n(93296),p=n(81695),u=n(56146),h=n(92859),x=n(412),m=n(7109);function f(e){return e.filter(e=>"application"===e.type_id)}function v(){(0,x.v9)(e=>e.environment.environmentLoadedValues);let e=(0,x.v9)(e=>{var t;return null==e?void 0:null===(t=e.userInfo)||void 0===t?void 0:t.userInfoLoadedValues}),t=(0,p.useSearchParams)().get("application"),n=async n=>{try{c.ZP.loading("Fetching latest data",{id:"fetching",position:"bottom-center"});let t=await s.Z.get(n,{headers:{Accept:"application/json",Authorization:(0,m.Z)(e),superduper_reverse_proxy:"http://localhost:8000"}});return console.log(n,t.data),c.ZP.dismiss("fetching"),t.data}catch(e){c.ZP.dismiss("fetching"),console.error("Error fetching Services API data from /webui/restapi/db/show?application=".concat(t))}},[v,g]=(0,i.useState)(null),[j,y]=(0,i.useState)(null),w=e=>{let t={};return e.forEach((e,n)=>{let r=e.type_id;t[r]||(t[r]={type_id:r,payload:[]}),t[r].payload.push({id:n+1,identifier:e.identifier,type_id:e.type_id,status:"online",timestamp:""})}),Object.values(t)},{data:b,error:N}=(0,d.ZP)("".concat("".concat("http://localhost:8000","/db/show?application=").concat(t)),n,{refreshInterval:6e4,shouldRetryOnError:!1});(0,i.useEffect)(()=>{b?(g(w(b.filter(e=>"application"!==e.type_id))),y(w(f(b)))):(g(w(f([]))),y(w(f([]))))},[b,N]);let[k,_]=(0,i.useState)(!1);return(0,i.useEffect)(()=>{if(v&&0===v.length){let e=setTimeout(()=>{_(!0)},1e3);return()=>clearTimeout(e)}_(!1)},[v]),(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(u.aG,{children:(0,r.jsxs)(u.Jb,{children:[(0,r.jsx)(u.gN,{children:(0,r.jsx)(u.At,{href:"/webui",children:"Home"})}),(0,r.jsx)(u.bg,{}),(0,r.jsx)(u.gN,{children:(0,r.jsx)(u.At,{href:"/webui/application",children:"Application"})}),(0,r.jsx)(u.bg,{}),(0,r.jsx)(u.gN,{children:(0,r.jsx)(u.AG,{children:t})})]})}),(0,r.jsx)("br",{}),(0,r.jsx)(h.Z,{title:"".concat(t&&t," components"),description:"View all the components that are currently deployed as part of the ".concat(t," application"),buttonText:"Edit ".concat(t&&t),buttonLink:"/webui/add-application?type_id=application&identifier=".concat(t)}),(0,r.jsx)("br",{}),(0,r.jsxs)("div",{children:[v?v.length>0?v.map((e,t)=>(0,r.jsx)(o.Z,{data:e},t)):!k&&(0,r.jsx)(a.Z,{}):(0,r.jsx)(a.Z,{}),k&&(0,r.jsx)(l.Z,{header:"No component found in ".concat(t," application"),description:"Something went wrong. Please try again later.",createDeployment:"hide"})]}),(0,r.jsx)("br",{}),(0,r.jsx)("br",{}),(0,r.jsx)("br",{}),(0,r.jsx)("br",{})]})}var g=n(96764);let j=i.forwardRef(function(e,t){let{title:n,titleId:r,...a}=e;return i.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 20 20",fill:"currentColor","aria-hidden":"true","data-slot":"icon",ref:t,"aria-labelledby":r},a),n?i.createElement("title",{id:r},n):null,i.createElement("path",{fillRule:"evenodd",d:"M4.25 5.5a.75.75 0 0 0-.75.75v8.5c0 .414.336.75.75.75h8.5a.75.75 0 0 0 .75-.75v-4a.75.75 0 0 1 1.5 0v4A2.25 2.25 0 0 1 12.75 17h-8.5A2.25 2.25 0 0 1 2 14.75v-8.5A2.25 2.25 0 0 1 4.25 4h5a.75.75 0 0 1 0 1.5h-5Z",clipRule:"evenodd"}),i.createElement("path",{fillRule:"evenodd",d:"M6.194 12.753a.75.75 0 0 0 1.06.053L16.5 4.44v2.81a.75.75 0 0 0 1.5 0v-4.5a.75.75 0 0 0-.75-.75h-4.5a.75.75 0 0 0 0 1.5h2.553l-9.056 8.194a.75.75 0 0 0-.053 1.06Z",clipRule:"evenodd"}))});var y=n(36531);function w(e){let{identifier:t}=e,[n,a]=(0,i.useState)(null);(0,x.v9)(e=>e.environment.environmentLoadedValues);let o=(0,x.v9)(e=>{var t;return null==e?void 0:null===(t=e.userInfo)||void 0===t?void 0:t.userInfoLoadedValues});return(0,i.useEffect)(()=>{if(t){let e=()=>{console.error("Error fetching application data from /webui/restapi/db/show?type_id=application&identifier=".concat(t))};(async()=>{try{let e=(await s.Z.get("".concat("".concat("http://localhost:8000","/db/show?type_id=application&identifier=").concat(t)),{headers:{Accept:"application/json",Authorization:(0,m.Z)(o),superduper_reverse_proxy:"http://localhost:8000"}})).data.slice(-1)[0];console.log("Latest Version:",e);let n=await s.Z.get("".concat("".concat("http://localhost:8000","/db/show?type_id=application&identifier=").concat(t,"&version=").concat(e)),{headers:{Accept:"application/json",Authorization:(0,m.Z)(o),superduper_reverse_proxy:"http://localhost:8000"}});console.log("JSON DATA",n.data),a(n.data)}catch(n){console.error("Error fetching application data from /webui/restapi/db/show?type_id=application&identifier=".concat(t),n),e()}})()}},[t]),(0,r.jsx)(r.Fragment,{children:(0,r.jsx)("a",{href:null==n?void 0:n.link,className:"flex gap-x-2",target:"_blank",rel:"noopener noreferrer",children:(0,r.jsxs)(y.z,{variant:"outline",disabled:!(null==n?void 0:n.link),children:["Open",(0,r.jsx)(j,{className:"ml-2 -mr-0.5 h-5 w-5 flex-none text-gray-400","aria-hidden":"true"})]})})})}n(86288),n(24776);var b=n(1930);n(97747);var N=n(11277),k=n(70694);n(98348);var _=n(27496),Z=n(85293),A=n(22392);n(40020),n(19234),n(83346);var L=n(59916);n(72513);var E=n(64520),C=n(46346);function P(e){let{open:t,setOpen:n,deleteError:a,setDeleteError:s,setDeletedName:o}=e,[l,d]=(0,i.useState)("");return(0,i.useEffect)(()=>{a&&d(JSON.stringify(a,null,2))},[a]),(0,r.jsx)(E.aR,{open:t,children:(0,r.jsxs)(E._T,{className:"max-w-[90vw] md:max-w-[600px]",children:[(0,r.jsx)(E.fY,{children:(0,r.jsx)(E.f$,{children:a?"Error deleting":"Deleting..."})}),(0,r.jsx)(E.yT,{className:"max-h-[60vh]",children:a?(0,r.jsxs)("div",{className:"space-y-2",children:[(0,r.jsx)("p",{className:"text-sm font-medium text-destructive",children:"An error occurred:"}),(0,r.jsx)(A.default,{className:"block w-full rounded-md border-2 py-1.5 text-gray-900 shadow-lg ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600",mode:"json",theme:"github",name:"errorEditor",value:l,readOnly:!0,fontSize:13,showPrintMargin:!1,showGutter:!0,highlightActiveLine:!1,setOptions:{enableBasicAutocompletion:!1,enableLiveAutocompletion:!1,enableSnippets:!1,showLineNumbers:!0,tabSize:2,useWorker:!1,wrap:!0},height:"350px",width:"100%"})]}):"Deleting. Please wait..."}),(0,r.jsx)(E.xo,{children:(0,r.jsx)(E.le,{onClick:()=>{s(!1),o(""),n(!1)},children:"Close"})})]})})}n(45246);let{getReasonPhrase:I}=n(70194),S={offline:"text-gray-500 bg-gray-100/10",online:"text-green-400 bg-green-400/10",error:"text-rose-400 bg-rose-400/10",pending:"text-yellow-400 bg-yellow-400/10"};function z(e){var t;(0,x.v9)(e=>e.environment.environmentLoadedValues);let n=(0,x.v9)(e=>{var t;return null==e?void 0:null===(t=e.userInfo)||void 0===t?void 0:t.userInfoLoadedValues}),a=(0,x.I0)(),[o,l]=(0,i.useState)({type_id:"",identifier:"",version:""}),[d,p]=(0,i.useState)(!1),[u,h]=(0,i.useState)(!1),[f,v]=(0,i.useState)(""),j=e=>{v(e.target.value)},[A,I]=(0,i.useState)(""),[z,F]=(0,i.useState)(""),[W,G]=(0,i.useState)(!1),[X,J]=(0,i.useState)(!1),[U,q]=(0,i.useState)(!1),H=async e=>{let t;try{if((null==e?void 0:e.identifier)!==f){c.ZP.error("Identifier does not match. Type it carefully.",{id:"delete-deployment"});return}q(!0),p(!1),t=c.ZP.loading("Deleting component..."),console.log("Deleting component:",e);let r=await s.Z.post("".concat("".concat("http://localhost:8000","/db/remove?type_id=").concat(e.type_id,"&identifier=").concat(e.identifier)),{headers:{Accept:"application/json",Authorization:(0,m.Z)(n),superduper_reverse_proxy:"http://localhost:8000"}});console.log("Delete Component API data:",r.data),(null==r?void 0:r.status)===200?(c.ZP.success("Component deleted successfully",{id:t}),I("Success: ".concat(r.data.message||"Component deleted successfully")),F("success"),setTimeout(()=>{q(!1),window.location.reload()},3e3)):r&&(console.error("Error deleting component:",r.data),I("Failed to delete component"),F("error"),setTimeout(()=>{J((null==r?void 0:r.data)||r||"Something went wrong. Please try again later. Check the console.log for the details.")},1e3),setErrorMsg("Error deleting application!"),h(!0))}catch(e){var r;console.error("Error deleting component:",e),console.error("Detail Error error?.response?.data:",null==e?void 0:null===(r=e.response)||void 0===r?void 0:r.data),setTimeout(()=>{var t;J((null==e?void 0:null===(t=e.response)||void 0===t?void 0:t.data)||e)},1e3),h(!0),t?c.ZP.error("Error deleting component",{id:t}):c.ZP.error("Error deleting component"),I("Error Deleting Component"),F("error")}},Y=e.data;return(0,r.jsxs)(r.Fragment,{children:[(0,r.jsxs)(C.x,{className:"max-w-7xl whitespace-nowrap",children:[(0,r.jsxs)("div",{className:" bg-white px-4 py-0 sm:px-6",children:[(0,r.jsx)("div",{className:"mx-auto max-w-7xl pr-4 pt-5 pb-0 sm:pr-6 lg:pr-8",children:(0,r.jsx)("div",{className:"mx-auto flex max-w-2xl items-center justify-between gap-x-8 lg:mx-0 lg:max-w-none",children:(0,r.jsxs)("div",{className:"flex items-center gap-x-4",children:[(0,r.jsx)("div",{className:"border rounded-lg p-2",children:(null==Y?void 0:Y.type_id)=="model"?(0,r.jsx)(O,{className:"w-6 h-6 text-black"}):(null==Y?void 0:Y.type_id)=="datatype"?(0,r.jsx)(R,{className:"w-6 h-6 text-black"}):(null==Y?void 0:Y.type_id)=="listener"?(0,r.jsx)(D,{className:"w-6 h-6 text-black"}):(null==Y?void 0:Y.type_id)=="metric"?(0,r.jsx)(T,{className:"w-6 h-6 text-black"}):(null==Y?void 0:Y.type_id)=="serializer"?(0,r.jsx)(M,{className:"w-6 h-6 text-black"}):(null==Y?void 0:Y.type_id)=="encoder"?(0,r.jsx)(B,{className:"w-6 h-6 text-black"}):(null==Y?void 0:Y.type_id)=="vector_index"?(0,r.jsx)(V,{className:"w-6 h-6 text-black"}):(0,r.jsx)(L.Z,{className:"w-6 h-6 text-black"})}),(0,r.jsx)("h1",{children:(0,r.jsxs)("div",{className:"text-base font-semibold leading-6 text-gray-900",children:["application"===(t=null==Y?void 0:Y.type_id)?"Deployed Applications":t.replace(/_/g," ").split(" ").map(e=>e.charAt(0).toUpperCase()+e.slice(1).toLowerCase()).join(" ")," "]})})]})})}),(0,r.jsxs)("div",{className:" bg-white px-4 py-5 sm:px-6",children:[(0,r.jsx)("div",{className:"-ml-4 -mt-4 flex flex-wrap items-center justify-between sm:flex-nowrap border-b border-gray-200",children:(0,r.jsx)("div",{className:"ml-4 mt-4 flex-shrink-0"})}),(0,r.jsx)("ul",{role:"list",className:"divide-y divide-red/5",children:Y.payload.map(e=>{let t=null==e?void 0:e.pending;return(0,r.jsxs)("li",{className:"relative flex items-center space-x-4 py-4 ".concat(t?"opacity-50 pointer-events-none":""),children:[(0,r.jsxs)("div",{className:"min-w-0 flex-auto ".concat(t?"pointer-events-none":""),children:[(0,r.jsxs)("div",{className:"flex items-center gap-x-3",children:[(0,r.jsx)("div",{className:function(){for(var e=arguments.length,t=Array(e),n=0;n<e;n++)t[n]=arguments[n];return t.filter(Boolean).join(" ")}(S[e.status],"flex-none rounded-full p-1"),children:(0,r.jsx)("div",{className:"h-2 w-2 rounded-full bg-current"})}),(0,r.jsx)("h2",{className:"min-w-0 text-sm font-semibold leading-6 text-black",children:(0,r.jsx)("a",{href:"/webui/show?application=".concat(e.identifier),className:"flex gap-x-2",children:(0,r.jsx)("span",{className:"whitespace-nowrap",children:e.identifier})})})]}),(0,r.jsx)("div",{className:"mt-3 flex items-center gap-x-2.5 text-xs leading-5 text-gray-400",children:(0,r.jsx)("p",{className:"whitespace-nowrap",children:e.timestamp})})]}),(0,r.jsx)(w,{identifier:e.identifier}),(0,r.jsx)("a",{href:"/webui/add-application?type_id=".concat(e.type_id,"&identifier=").concat(e.identifier),className:"flex gap-x-2",children:(0,r.jsxs)(y.z,{variant:"outline",disabled:t,children:["Edit","  "]})}),(0,Z.M)(t?"pending":"running"),(0,r.jsxs)(k.yo,{children:[(0,r.jsx)(k.aM,{asChild:!0,children:(0,r.jsxs)(y.z,{variant:"outline",onClick:()=>{t||a((0,_.t)(e))},className:t?"pointer-events-auto opacity-100":"",children:["Inspect","  ",(0,r.jsx)(g.Z,{className:"ml-2 -mr-0.5 h-5 w-5 flex-none text-gray-400","aria-hidden":"true"})]})}),(0,r.jsxs)(k.ue,{className:"overflow-auto w-[800px] sm:w-[800px] sm:max-w-none",children:[(0,r.jsxs)(k.Tu,{children:[(0,r.jsx)("div",{className:"flex justify-between items-center",children:(0,r.jsx)(k.bC,{children:(0,r.jsxs)("div",{children:[(0,r.jsxs)("h1",{className:"text-lg font-semibold leading-6 text-gray-900",children:[e.type_id,"/",e.identifier]}),(0,r.jsxs)("p",{className:"text-sm text-gray-600",children:["type_id: ",e.type_id,", identifier:"," ",e.identifier]})]})})}),(0,r.jsx)("br",{})]}),(0,r.jsx)("div",{className:"grid gap-4 py-4 overflow-visible",children:(0,r.jsx)(N.Z,{data:e})}),(0,r.jsxs)(k.FF,{children:[(0,r.jsx)("a",{href:"/webui/add-application?type_id=".concat(e.type_id,"&identifier=").concat(e.identifier),children:(0,r.jsxs)(y.z,{className:"px-8 mt-6",variant:"outline",disabled:t,children:["Edit ",e.identifier]})}),(0,r.jsxs)(y.z,{variant:"destructive",className:"px-8 mt-6",onClick:()=>{l({type_id:e.type_id,identifier:e.identifier,version:e.version||""}),p(!0)},children:["Delete ",e.identifier]}),(0,r.jsxs)(E.aR,{open:d,onOpenChange:p,children:[(0,r.jsx)(E.vW,{asChild:!0}),(0,r.jsxs)(E._T,{children:[(0,r.jsxs)(E.fY,{children:[(0,r.jsx)(E.f$,{children:"Confirm Deletion"}),(0,r.jsxs)(E.yT,{children:["To confirm deletion, please type the identifier"," ",(0,r.jsx)("strong",{children:o.identifier})," ","below."]})]}),(0,r.jsx)("div",{className:"mt-4",children:(0,r.jsx)(b.I,{type:"text",placeholder:"Type the identifier here",value:f,onChange:j,className:"w-full"})}),(0,r.jsxs)(E.xo,{children:[(0,r.jsx)(E.le,{onClick:()=>p(!1),children:"Cancel"}),(0,r.jsx)(E.OL,{onClick:()=>{if(o.identifier!==f){c.ZP.error("Identifier does not match. Please type it carefully.");return}p(!1),H(o)},disabled:f!==o.identifier,children:"Delete"})]})]})]})]})]})]})]},e.id)})})]})]}),(0,r.jsx)(C.B,{orientation:"horizontal"})]}),(0,r.jsx)(P,{open:U,setOpen:q,deleteError:X,setDeleteError:J,setDeletedName:v})]})}function B(e){return(0,r.jsxs)("svg",{...e,xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",children:[(0,r.jsx)("polyline",{points:"16 18 22 12 16 6"}),(0,r.jsx)("polyline",{points:"8 6 2 12 8 18"})]})}function T(e){return(0,r.jsxs)("svg",{...e,xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",children:[(0,r.jsx)("path",{d:"m12 14 4-4"}),(0,r.jsx)("path",{d:"M3.34 19a10 10 0 1 1 17.32 0"})]})}function M(e){return(0,r.jsxs)("svg",{...e,xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",children:[(0,r.jsx)("line",{x1:"12",x2:"12",y1:"2",y2:"6"}),(0,r.jsx)("line",{x1:"12",x2:"12",y1:"18",y2:"22"}),(0,r.jsx)("line",{x1:"4.93",x2:"7.76",y1:"4.93",y2:"7.76"}),(0,r.jsx)("line",{x1:"16.24",x2:"19.07",y1:"16.24",y2:"19.07"}),(0,r.jsx)("line",{x1:"2",x2:"6",y1:"12",y2:"12"}),(0,r.jsx)("line",{x1:"18",x2:"22",y1:"12",y2:"12"}),(0,r.jsx)("line",{x1:"4.93",x2:"7.76",y1:"19.07",y2:"16.24"}),(0,r.jsx)("line",{x1:"16.24",x2:"19.07",y1:"7.76",y2:"4.93"})]})}function R(e){return(0,r.jsxs)("svg",{...e,xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",children:[(0,r.jsx)("polyline",{points:"4 7 4 4 20 4 20 7"}),(0,r.jsx)("line",{x1:"9",x2:"15",y1:"20",y2:"20"}),(0,r.jsx)("line",{x1:"12",x2:"12",y1:"4",y2:"20"})]})}function V(e){return(0,r.jsxs)("svg",{...e,xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",children:[(0,r.jsx)("ellipse",{cx:"12",cy:"5",rx:"9",ry:"3"}),(0,r.jsx)("path",{d:"M3 5V19A9 3 0 0 0 21 19V5"}),(0,r.jsx)("path",{d:"M3 12A9 3 0 0 0 21 12"})]})}function D(e){return(0,r.jsxs)("svg",{...e,xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",children:[(0,r.jsx)("path",{d:"M6 8.5a6.5 6.5 0 1 1 13 0c0 6-6 6-6 10a3.5 3.5 0 1 1-7 0"}),(0,r.jsx)("path",{d:"M15 8.5a2.5 2.5 0 0 0-5 0v1a2 2 0 1 1 0 4"})]})}function O(e){return(0,r.jsxs)("svg",{...e,xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",children:[(0,r.jsx)("path",{d:"M12 8V4H8"}),(0,r.jsx)("rect",{width:"16",height:"12",x:"4",y:"8",rx:"2"}),(0,r.jsx)("path",{d:"M2 14h2"}),(0,r.jsx)("path",{d:"M20 14h2"}),(0,r.jsx)("path",{d:"M15 13v2"}),(0,r.jsx)("path",{d:"M9 13v2"})]})}function F(){(0,x.v9)(e=>e.environment.environmentLoadedValues);let e=(0,x.v9)(e=>{var t;return null==e?void 0:null===(t=e.userInfo)||void 0===t?void 0:t.userInfoLoadedValues}),t=async t=>{try{c.ZP.loading("Fetching latest data",{id:"fetching",position:"bottom-center"});let t=await s.Z.get("".concat("".concat("http://localhost:8000","/db/show?type_id=application&show_status=true")),{headers:{Accept:"application/json",Authorization:(0,m.Z)(e),superduper_reverse_proxy:"http://localhost:8000"}});return console.log("/db/show?type_id=application&show_status=true API data:",t.data),c.ZP.dismiss("fetching"),t.data}catch(e){c.ZP.dismiss("fetching"),console.error("Error fetching Services API data")}},[n,o]=(0,i.useState)(null),p=e=>{let t={};return e.forEach((e,n)=>{let r="application";t[r]||(t[r]={type_id:r,payload:[]}),t[r].payload.push({id:n+1,identifier:e.identifier,pending:"pending"==e.status,type_id:"application",status:"pending"==e.status?"pending":"online",timestamp:""})}),Object.values(t)},{data:u,error:f}=(0,d.ZP)("".concat("".concat("http://localhost:8000","/db/show")),t,{refreshInterval:12e4,shouldRetryOnError:!1});(0,i.useEffect)(()=>{u?o(p(u)):o(p([]))},[u,f]);let[v,g]=(0,i.useState)(!1);return(0,i.useEffect)(()=>{if(n&&0===n.length){let e=setTimeout(()=>{g(!0)},1e3);return()=>clearTimeout(e)}g(!1)},[n]),(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(h.Z,{title:"Applications",description:"View all your agent applications running, or create a new one.",buttonText:"Add Application",buttonLink:"/webui/add-application"}),(0,r.jsx)("br",{}),(0,r.jsxs)("div",{children:[n?n.length>0?n.map((e,t)=>(0,r.jsx)(z,{data:e},t)):!v&&(0,r.jsx)(a.Z,{}):(0,r.jsx)(a.Z,{}),v&&(0,r.jsx)(l.Z,{header:"No Application Found",description:"Get started by adding a new application.",createDeployment:"hide"})]}),(0,r.jsx)("br",{}),(0,r.jsx)("br",{}),(0,r.jsx)("br",{}),(0,r.jsx)("br",{})]})}n(26716),n(45439);var W=n(74859);let{getReasonPhrase:G}=n(70194);function X(e){let{application:t}=e,n=(0,x.v9)(e=>e.environment.environmentLoadedValues),i=(0,x.v9)(e=>{var t;return null==e?void 0:null===(t=e.userInfo)||void 0===t?void 0:t.userInfoLoadedValues}),a=(0,x.v9)(e=>e.deploymentName.deploymentNameLoadedValues.name),o=async e=>{try{return(await s.Z.get(e,{headers:{Accept:"application/json",Authorization:(0,m.Z)(i),superduper_reverse_proxy:W.env.NEXT_PUBLIC_API||n.NEXT_PUBLIC_API}})).data}catch(e){var t,r;throw{status:(null===(t=e.response)||void 0===t?void 0:t.status)||500,message:(null===(r=e.response)||void 0===r?void 0:r.data)||"An unexpected error occurred"}}},l=async e=>{try{return(await s.Z.get(e,{headers:{Accept:"application/json",Authorization:(0,m.Z)(i),superduper_reverse_proxy:"http://localhost:8000"}})).data}catch(e){var t,n;throw{status:(null===(t=e.response)||void 0===t?void 0:t.status)||500,message:(null===(n=e.response)||void 0===n?void 0:n.data)||"An unexpected error occurred"}}},{data:c,error:p}=(0,d.ZP)("".concat("".concat(W.env.NEXT_PUBLIC_API,"/deployments/").concat(a)),o,{refreshInterval:3e4,shouldRetryOnError:!1}),{data:u,error:h}=(0,d.ZP)("".concat("".concat("http://localhost:8000","/health")),l,{refreshInterval:3e4,shouldRetryOnError:!1});return(0,r.jsx)(r.Fragment,{children:t?(0,r.jsx)(F,{}):(0,r.jsx)(v,{})})}},56146:function(e,t,n){n.d(t,{AG:function(){return u},At:function(){return p},Jb:function(){return d},aG:function(){return l},bg:function(){return h},gN:function(){return c}});var r=n(27573),i=n(7653),a=n(85688),s=n(8828),o=n(18580);let l=i.forwardRef((e,t)=>{let{...n}=e;return(0,r.jsx)("nav",{ref:t,"aria-label":"breadcrumb",...n})});l.displayName="Breadcrumb";let d=i.forwardRef((e,t)=>{let{className:n,...i}=e;return(0,r.jsx)("ol",{ref:t,className:(0,o.cn)("flex flex-wrap items-center gap-1.5 break-words text-sm text-muted-foreground sm:gap-2.5",n),...i})});d.displayName="BreadcrumbList";let c=i.forwardRef((e,t)=>{let{className:n,...i}=e;return(0,r.jsx)("li",{ref:t,className:(0,o.cn)("inline-flex items-center gap-1.5",n),...i})});c.displayName="BreadcrumbItem";let p=i.forwardRef((e,t)=>{let{asChild:n,className:i,...a}=e,l=n?s.g7:"a";return(0,r.jsx)(l,{ref:t,className:(0,o.cn)("transition-colors hover:text-foreground",i),...a})});p.displayName="BreadcrumbLink";let u=i.forwardRef((e,t)=>{let{className:n,...i}=e;return(0,r.jsx)("span",{ref:t,role:"link","aria-disabled":"true","aria-current":"page",className:(0,o.cn)("font-normal text-foreground",n),...i})});u.displayName="BreadcrumbPage";let h=e=>{let{children:t,className:n,...i}=e;return(0,r.jsx)("li",{role:"presentation","aria-hidden":"true",className:(0,o.cn)("[&>svg]:size-3.5",n),...i,children:null!=t?t:(0,r.jsx)(a.XCv,{})})};h.displayName="BreadcrumbSeparator"},53896:function(e,t,n){n.d(t,{Z:function(){return r}});let r=(0,n(84313).Z)("CheckCircle",[["path",{d:"M22 11.08V12a10 10 0 1 1-5.93-9.14",key:"g774vq"}],["path",{d:"m9 11 3 3L22 4",key:"1pflzl"}]])},23919:function(e,t,n){n.d(t,{Z:function(){return r}});let r=(0,n(84313).Z)("Loader2",[["path",{d:"M21 12a9 9 0 1 1-6.219-8.56",key:"13zald"}]])},63643:function(e,t,n){n.d(t,{Z:function(){return r}});let r=(0,n(84313).Z)("XCircle",[["circle",{cx:"12",cy:"12",r:"10",key:"1mglay"}],["path",{d:"m15 9-6 6",key:"1uzhvr"}],["path",{d:"m9 9 6 6",key:"z0biqf"}]])},51423:function(e,t,n){var r=n(7653);let i=r.forwardRef(function(e,t){let{title:n,titleId:i,...a}=e;return r.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true","data-slot":"icon",ref:t,"aria-labelledby":i},a),n?r.createElement("title",{id:i},n):null,r.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M21.75 6.75a4.5 4.5 0 0 1-4.884 4.484c-1.076-.091-2.264.071-2.95.904l-7.152 8.684a2.548 2.548 0 1 1-3.586-3.586l8.684-7.152c.833-.686.995-1.874.904-2.95a4.5 4.5 0 0 1 6.336-4.486l-3.276 3.276a3.004 3.004 0 0 0 2.25 2.25l3.276-3.276c.256.565.398 1.192.398 1.852Z"}),r.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M4.867 19.125h.008v.008h-.008v-.008Z"}))});t.Z=i}}]);