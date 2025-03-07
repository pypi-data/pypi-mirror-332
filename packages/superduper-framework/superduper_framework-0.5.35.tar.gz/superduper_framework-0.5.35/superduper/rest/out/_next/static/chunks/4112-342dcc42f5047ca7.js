"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[4112],{70194:function(e,t,r){r.r(t),r.d(t,{ACCEPTED:function(){return l},BAD_GATEWAY:function(){return a},BAD_REQUEST:function(){return u},CONFLICT:function(){return T},CONTINUE:function(){return c},CREATED:function(){return R},EXPECTATION_FAILED:function(){return s},FAILED_DEPENDENCY:function(){return d},FORBIDDEN:function(){return N},GATEWAY_TIMEOUT:function(){return _},GONE:function(){return O},HTTP_VERSION_NOT_SUPPORTED:function(){return I},IM_A_TEAPOT:function(){return A},INSUFFICIENT_SPACE_ON_RESOURCE:function(){return f},INSUFFICIENT_STORAGE:function(){return S},INTERNAL_SERVER_ERROR:function(){return C},LENGTH_REQUIRED:function(){return p},LOCKED:function(){return D},METHOD_FAILURE:function(){return U},METHOD_NOT_ALLOWED:function(){return P},MOVED_PERMANENTLY:function(){return L},MOVED_TEMPORARILY:function(){return h},MULTIPLE_CHOICES:function(){return M},MULTI_STATUS:function(){return v},NETWORK_AUTHENTICATION_REQUIRED:function(){return w},NON_AUTHORITATIVE_INFORMATION:function(){return g},NOT_ACCEPTABLE:function(){return y},NOT_FOUND:function(){return b},NOT_IMPLEMENTED:function(){return F},NOT_MODIFIED:function(){return H},NO_CONTENT:function(){return m},OK:function(){return x},PARTIAL_CONTENT:function(){return Y},PAYMENT_REQUIRED:function(){return G},PERMANENT_REDIRECT:function(){return Q},PRECONDITION_FAILED:function(){return W},PRECONDITION_REQUIRED:function(){return B},PROCESSING:function(){return V},PROXY_AUTHENTICATION_REQUIRED:function(){return q},REQUESTED_RANGE_NOT_SATISFIABLE:function(){return K},REQUEST_HEADER_FIELDS_TOO_LARGE:function(){return j},REQUEST_TIMEOUT:function(){return k},REQUEST_TOO_LONG:function(){return X},REQUEST_URI_TOO_LONG:function(){return z},RESET_CONTENT:function(){return Z},ReasonPhrases:function(){return E},SEE_OTHER:function(){return $},SERVICE_UNAVAILABLE:function(){return J},SWITCHING_PROTOCOLS:function(){return ee},StatusCodes:function(){return i},TEMPORARY_REDIRECT:function(){return et},TOO_MANY_REQUESTS:function(){return er},UNAUTHORIZED:function(){return en},UNPROCESSABLE_ENTITY:function(){return eo},UNSUPPORTED_MEDIA_TYPE:function(){return ei},USE_PROXY:function(){return eE},default:function(){return es},getReasonPhrase:function(){return eu},getStatusCode:function(){return eT},getStatusText:function(){return ec}});var n,o,i,E,l=202,a=502,u=400,T=409,c=100,R=201,s=417,d=424,N=403,_=504,O=410,I=505,A=418,f=419,S=507,C=500,p=411,D=423,U=420,P=405,L=301,h=302,v=207,M=300,w=511,m=204,g=203,y=406,b=404,F=501,H=304,x=200,Y=206,G=402,Q=308,W=412,B=428,V=102,q=407,j=431,k=408,X=413,z=414,K=416,Z=205,$=303,J=503,ee=101,et=307,er=429,en=401,eo=422,ei=415,eE=305,el={202:"Accepted",502:"Bad Gateway",400:"Bad Request",409:"Conflict",100:"Continue",201:"Created",417:"Expectation Failed",424:"Failed Dependency",403:"Forbidden",504:"Gateway Timeout",410:"Gone",505:"HTTP Version Not Supported",418:"I'm a teapot",419:"Insufficient Space on Resource",507:"Insufficient Storage",500:"Internal Server Error",411:"Length Required",423:"Locked",420:"Method Failure",405:"Method Not Allowed",301:"Moved Permanently",302:"Moved Temporarily",207:"Multi-Status",300:"Multiple Choices",511:"Network Authentication Required",204:"No Content",203:"Non Authoritative Information",406:"Not Acceptable",404:"Not Found",501:"Not Implemented",304:"Not Modified",200:"OK",206:"Partial Content",402:"Payment Required",308:"Permanent Redirect",412:"Precondition Failed",428:"Precondition Required",102:"Processing",103:"Early Hints",426:"Upgrade Required",407:"Proxy Authentication Required",431:"Request Header Fields Too Large",408:"Request Timeout",413:"Request Entity Too Large",414:"Request-URI Too Long",416:"Requested Range Not Satisfiable",205:"Reset Content",303:"See Other",503:"Service Unavailable",101:"Switching Protocols",307:"Temporary Redirect",429:"Too Many Requests",401:"Unauthorized",451:"Unavailable For Legal Reasons",422:"Unprocessable Entity",415:"Unsupported Media Type",305:"Use Proxy",421:"Misdirected Request"},ea={Accepted:202,"Bad Gateway":502,"Bad Request":400,Conflict:409,Continue:100,Created:201,"Expectation Failed":417,"Failed Dependency":424,Forbidden:403,"Gateway Timeout":504,Gone:410,"HTTP Version Not Supported":505,"I'm a teapot":418,"Insufficient Space on Resource":419,"Insufficient Storage":507,"Internal Server Error":500,"Length Required":411,Locked:423,"Method Failure":420,"Method Not Allowed":405,"Moved Permanently":301,"Moved Temporarily":302,"Multi-Status":207,"Multiple Choices":300,"Network Authentication Required":511,"No Content":204,"Non Authoritative Information":203,"Not Acceptable":406,"Not Found":404,"Not Implemented":501,"Not Modified":304,OK:200,"Partial Content":206,"Payment Required":402,"Permanent Redirect":308,"Precondition Failed":412,"Precondition Required":428,Processing:102,"Early Hints":103,"Upgrade Required":426,"Proxy Authentication Required":407,"Request Header Fields Too Large":431,"Request Timeout":408,"Request Entity Too Large":413,"Request-URI Too Long":414,"Requested Range Not Satisfiable":416,"Reset Content":205,"See Other":303,"Service Unavailable":503,"Switching Protocols":101,"Temporary Redirect":307,"Too Many Requests":429,Unauthorized:401,"Unavailable For Legal Reasons":451,"Unprocessable Entity":422,"Unsupported Media Type":415,"Use Proxy":305,"Misdirected Request":421};function eu(e){var t=el[e.toString()];if(!t)throw Error("Status code does not exist: "+e);return t}function eT(e){var t=ea[e];if(!t)throw Error("Reason phrase does not exist: "+e);return t}var ec=eu;(n=i||(i={}))[n.CONTINUE=100]="CONTINUE",n[n.SWITCHING_PROTOCOLS=101]="SWITCHING_PROTOCOLS",n[n.PROCESSING=102]="PROCESSING",n[n.EARLY_HINTS=103]="EARLY_HINTS",n[n.OK=200]="OK",n[n.CREATED=201]="CREATED",n[n.ACCEPTED=202]="ACCEPTED",n[n.NON_AUTHORITATIVE_INFORMATION=203]="NON_AUTHORITATIVE_INFORMATION",n[n.NO_CONTENT=204]="NO_CONTENT",n[n.RESET_CONTENT=205]="RESET_CONTENT",n[n.PARTIAL_CONTENT=206]="PARTIAL_CONTENT",n[n.MULTI_STATUS=207]="MULTI_STATUS",n[n.MULTIPLE_CHOICES=300]="MULTIPLE_CHOICES",n[n.MOVED_PERMANENTLY=301]="MOVED_PERMANENTLY",n[n.MOVED_TEMPORARILY=302]="MOVED_TEMPORARILY",n[n.SEE_OTHER=303]="SEE_OTHER",n[n.NOT_MODIFIED=304]="NOT_MODIFIED",n[n.USE_PROXY=305]="USE_PROXY",n[n.TEMPORARY_REDIRECT=307]="TEMPORARY_REDIRECT",n[n.PERMANENT_REDIRECT=308]="PERMANENT_REDIRECT",n[n.BAD_REQUEST=400]="BAD_REQUEST",n[n.UNAUTHORIZED=401]="UNAUTHORIZED",n[n.PAYMENT_REQUIRED=402]="PAYMENT_REQUIRED",n[n.FORBIDDEN=403]="FORBIDDEN",n[n.NOT_FOUND=404]="NOT_FOUND",n[n.METHOD_NOT_ALLOWED=405]="METHOD_NOT_ALLOWED",n[n.NOT_ACCEPTABLE=406]="NOT_ACCEPTABLE",n[n.PROXY_AUTHENTICATION_REQUIRED=407]="PROXY_AUTHENTICATION_REQUIRED",n[n.REQUEST_TIMEOUT=408]="REQUEST_TIMEOUT",n[n.CONFLICT=409]="CONFLICT",n[n.GONE=410]="GONE",n[n.LENGTH_REQUIRED=411]="LENGTH_REQUIRED",n[n.PRECONDITION_FAILED=412]="PRECONDITION_FAILED",n[n.REQUEST_TOO_LONG=413]="REQUEST_TOO_LONG",n[n.REQUEST_URI_TOO_LONG=414]="REQUEST_URI_TOO_LONG",n[n.UNSUPPORTED_MEDIA_TYPE=415]="UNSUPPORTED_MEDIA_TYPE",n[n.REQUESTED_RANGE_NOT_SATISFIABLE=416]="REQUESTED_RANGE_NOT_SATISFIABLE",n[n.EXPECTATION_FAILED=417]="EXPECTATION_FAILED",n[n.IM_A_TEAPOT=418]="IM_A_TEAPOT",n[n.INSUFFICIENT_SPACE_ON_RESOURCE=419]="INSUFFICIENT_SPACE_ON_RESOURCE",n[n.METHOD_FAILURE=420]="METHOD_FAILURE",n[n.MISDIRECTED_REQUEST=421]="MISDIRECTED_REQUEST",n[n.UNPROCESSABLE_ENTITY=422]="UNPROCESSABLE_ENTITY",n[n.LOCKED=423]="LOCKED",n[n.FAILED_DEPENDENCY=424]="FAILED_DEPENDENCY",n[n.UPGRADE_REQUIRED=426]="UPGRADE_REQUIRED",n[n.PRECONDITION_REQUIRED=428]="PRECONDITION_REQUIRED",n[n.TOO_MANY_REQUESTS=429]="TOO_MANY_REQUESTS",n[n.REQUEST_HEADER_FIELDS_TOO_LARGE=431]="REQUEST_HEADER_FIELDS_TOO_LARGE",n[n.UNAVAILABLE_FOR_LEGAL_REASONS=451]="UNAVAILABLE_FOR_LEGAL_REASONS",n[n.INTERNAL_SERVER_ERROR=500]="INTERNAL_SERVER_ERROR",n[n.NOT_IMPLEMENTED=501]="NOT_IMPLEMENTED",n[n.BAD_GATEWAY=502]="BAD_GATEWAY",n[n.SERVICE_UNAVAILABLE=503]="SERVICE_UNAVAILABLE",n[n.GATEWAY_TIMEOUT=504]="GATEWAY_TIMEOUT",n[n.HTTP_VERSION_NOT_SUPPORTED=505]="HTTP_VERSION_NOT_SUPPORTED",n[n.INSUFFICIENT_STORAGE=507]="INSUFFICIENT_STORAGE",n[n.NETWORK_AUTHENTICATION_REQUIRED=511]="NETWORK_AUTHENTICATION_REQUIRED",(o=E||(E={})).ACCEPTED="Accepted",o.BAD_GATEWAY="Bad Gateway",o.BAD_REQUEST="Bad Request",o.CONFLICT="Conflict",o.CONTINUE="Continue",o.CREATED="Created",o.EXPECTATION_FAILED="Expectation Failed",o.FAILED_DEPENDENCY="Failed Dependency",o.FORBIDDEN="Forbidden",o.GATEWAY_TIMEOUT="Gateway Timeout",o.GONE="Gone",o.HTTP_VERSION_NOT_SUPPORTED="HTTP Version Not Supported",o.IM_A_TEAPOT="I'm a teapot",o.INSUFFICIENT_SPACE_ON_RESOURCE="Insufficient Space on Resource",o.INSUFFICIENT_STORAGE="Insufficient Storage",o.INTERNAL_SERVER_ERROR="Internal Server Error",o.LENGTH_REQUIRED="Length Required",o.LOCKED="Locked",o.METHOD_FAILURE="Method Failure",o.METHOD_NOT_ALLOWED="Method Not Allowed",o.MOVED_PERMANENTLY="Moved Permanently",o.MOVED_TEMPORARILY="Moved Temporarily",o.MULTI_STATUS="Multi-Status",o.MULTIPLE_CHOICES="Multiple Choices",o.NETWORK_AUTHENTICATION_REQUIRED="Network Authentication Required",o.NO_CONTENT="No Content",o.NON_AUTHORITATIVE_INFORMATION="Non Authoritative Information",o.NOT_ACCEPTABLE="Not Acceptable",o.NOT_FOUND="Not Found",o.NOT_IMPLEMENTED="Not Implemented",o.NOT_MODIFIED="Not Modified",o.OK="OK",o.PARTIAL_CONTENT="Partial Content",o.PAYMENT_REQUIRED="Payment Required",o.PERMANENT_REDIRECT="Permanent Redirect",o.PRECONDITION_FAILED="Precondition Failed",o.PRECONDITION_REQUIRED="Precondition Required",o.PROCESSING="Processing",o.EARLY_HINTS="Early Hints",o.UPGRADE_REQUIRED="Upgrade Required",o.PROXY_AUTHENTICATION_REQUIRED="Proxy Authentication Required",o.REQUEST_HEADER_FIELDS_TOO_LARGE="Request Header Fields Too Large",o.REQUEST_TIMEOUT="Request Timeout",o.REQUEST_TOO_LONG="Request Entity Too Large",o.REQUEST_URI_TOO_LONG="Request-URI Too Long",o.REQUESTED_RANGE_NOT_SATISFIABLE="Requested Range Not Satisfiable",o.RESET_CONTENT="Reset Content",o.SEE_OTHER="See Other",o.SERVICE_UNAVAILABLE="Service Unavailable",o.SWITCHING_PROTOCOLS="Switching Protocols",o.TEMPORARY_REDIRECT="Temporary Redirect",o.TOO_MANY_REQUESTS="Too Many Requests",o.UNAUTHORIZED="Unauthorized",o.UNAVAILABLE_FOR_LEGAL_REASONS="Unavailable For Legal Reasons",o.UNPROCESSABLE_ENTITY="Unprocessable Entity",o.UNSUPPORTED_MEDIA_TYPE="Unsupported Media Type",o.USE_PROXY="Use Proxy",o.MISDIRECTED_REQUEST="Misdirected Request";var eR=function(){return(eR=Object.assign||function(e){for(var t,r=1,n=arguments.length;r<n;r++)for(var o in t=arguments[r])Object.prototype.hasOwnProperty.call(t,o)&&(e[o]=t[o]);return e}).apply(this,arguments)},es=eR(eR({},{ACCEPTED:l,BAD_GATEWAY:a,BAD_REQUEST:u,CONFLICT:T,CONTINUE:c,CREATED:R,EXPECTATION_FAILED:s,FORBIDDEN:N,GATEWAY_TIMEOUT:_,GONE:O,HTTP_VERSION_NOT_SUPPORTED:I,IM_A_TEAPOT:A,INSUFFICIENT_SPACE_ON_RESOURCE:f,INSUFFICIENT_STORAGE:S,INTERNAL_SERVER_ERROR:C,LENGTH_REQUIRED:p,LOCKED:D,METHOD_FAILURE:U,METHOD_NOT_ALLOWED:P,MOVED_PERMANENTLY:L,MOVED_TEMPORARILY:h,MULTI_STATUS:v,MULTIPLE_CHOICES:M,NETWORK_AUTHENTICATION_REQUIRED:w,NO_CONTENT:m,NON_AUTHORITATIVE_INFORMATION:g,NOT_ACCEPTABLE:y,NOT_FOUND:b,NOT_IMPLEMENTED:F,NOT_MODIFIED:H,OK:x,PARTIAL_CONTENT:Y,PAYMENT_REQUIRED:G,PERMANENT_REDIRECT:Q,PRECONDITION_FAILED:W,PRECONDITION_REQUIRED:B,PROCESSING:V,PROXY_AUTHENTICATION_REQUIRED:q,REQUEST_HEADER_FIELDS_TOO_LARGE:j,REQUEST_TIMEOUT:k,REQUEST_TOO_LONG:X,REQUEST_URI_TOO_LONG:z,REQUESTED_RANGE_NOT_SATISFIABLE:K,RESET_CONTENT:Z,SEE_OTHER:$,SERVICE_UNAVAILABLE:J,SWITCHING_PROTOCOLS:ee,TEMPORARY_REDIRECT:et,TOO_MANY_REQUESTS:er,UNAUTHORIZED:en,UNPROCESSABLE_ENTITY:eo,UNSUPPORTED_MEDIA_TYPE:ei,USE_PROXY:eE}),{getStatusCode:eT,getStatusText:ec})},84313:function(e,t,r){r.d(t,{Z:function(){return E}});var n=r(7653),o={xmlns:"http://www.w3.org/2000/svg",width:24,height:24,viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:2,strokeLinecap:"round",strokeLinejoin:"round"};let i=e=>e.replace(/([a-z0-9])([A-Z])/g,"$1-$2").toLowerCase().trim(),E=(e,t)=>{let r=(0,n.forwardRef)((r,E)=>{let{color:l="currentColor",size:a=24,strokeWidth:u=2,absoluteStrokeWidth:T,className:c="",children:R,...s}=r;return(0,n.createElement)("svg",{ref:E,...o,width:a,height:a,stroke:l,strokeWidth:T?24*Number(u)/Number(a):u,className:["lucide","lucide-".concat(i(e)),c].join(" "),...s},[...t.map(e=>{let[t,r]=e;return(0,n.createElement)(t,r)}),...Array.isArray(R)?R:[R]])});return r.displayName="".concat(e),r}},46065:function(e,t,r){r.d(t,{Z:function(){return n}});let n=(0,r(84313).Z)("AlertCircle",[["circle",{cx:"12",cy:"12",r:"10",key:"1mglay"}],["line",{x1:"12",x2:"12",y1:"8",y2:"12",key:"1pkeuh"}],["line",{x1:"12",x2:"12.01",y1:"16",y2:"16",key:"4dfq90"}]])},15155:function(e,t,r){r.d(t,{Z:function(){return n}});let n=(0,r(84313).Z)("AlertTriangle",[["path",{d:"m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z",key:"c3ski4"}],["path",{d:"M12 9v4",key:"juzpu7"}],["path",{d:"M12 17h.01",key:"p32p05"}]])},2966:function(e,t,r){r.d(t,{Z:function(){return n}});let n=(0,r(84313).Z)("ChevronRight",[["path",{d:"m9 18 6-6-6-6",key:"mthhwq"}]])},2461:function(e,t,r){r.d(t,{Z:function(){return n}});let n=(0,r(84313).Z)("RotateCcw",[["path",{d:"M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8",key:"1357e3"}],["path",{d:"M3 3v5h5",key:"1xhq8a"}]])},90206:function(e,t,r){r.d(t,{u:function(){return n}});function n(e,[t,r]){return Math.min(r,Math.max(t,e))}},3864:function(e,t,r){r.d(t,{B:function(){return l}});var n=r(7653),o=r(27573),i=r(94492),E=r(8828);function l(e){let t=e+"CollectionProvider",[r,l]=function(e,t=[]){let r=[],i=()=>{let t=r.map(e=>n.createContext(e));return function(r){let o=r?.[e]||t;return n.useMemo(()=>({[`__scope${e}`]:{...r,[e]:o}}),[r,o])}};return i.scopeName=e,[function(t,i){let E=n.createContext(i),l=r.length;function a(t){let{scope:r,children:i,...a}=t,u=r?.[e][l]||E,T=n.useMemo(()=>a,Object.values(a));return(0,o.jsx)(u.Provider,{value:T,children:i})}return r=[...r,i],a.displayName=t+"Provider",[a,function(r,o){let a=o?.[e][l]||E,u=n.useContext(a);if(u)return u;if(void 0!==i)return i;throw Error(`\`${r}\` must be used within \`${t}\``)}]},function(...e){let t=e[0];if(1===e.length)return t;let r=()=>{let r=e.map(e=>({useScope:e(),scopeName:e.scopeName}));return function(e){let o=r.reduce((t,{useScope:r,scopeName:n})=>{let o=r(e)[`__scope${n}`];return{...t,...o}},{});return n.useMemo(()=>({[`__scope${t.scopeName}`]:o}),[o])}};return r.scopeName=t.scopeName,r}(i,...t)]}(t),[a,u]=r(t,{collectionRef:{current:null},itemMap:new Map}),T=e=>{let{scope:t,children:r}=e,i=n.useRef(null),E=n.useRef(new Map).current;return(0,o.jsx)(a,{scope:t,itemMap:E,collectionRef:i,children:r})};T.displayName=t;let c=e+"CollectionSlot",R=n.forwardRef((e,t)=>{let{scope:r,children:n}=e,l=u(c,r),a=(0,i.e)(t,l.collectionRef);return(0,o.jsx)(E.g7,{ref:a,children:n})});R.displayName=c;let s=e+"CollectionItemSlot",d="data-radix-collection-item",N=n.forwardRef((e,t)=>{let{scope:r,children:l,...a}=e,T=n.useRef(null),c=(0,i.e)(t,T),R=u(s,r);return n.useEffect(()=>(R.itemMap.set(T,{ref:T,...a}),()=>void R.itemMap.delete(T))),(0,o.jsx)(E.g7,{[d]:"",ref:c,children:l})});return N.displayName=s,[{Provider:T,Slot:R,ItemSlot:N},function(t){let r=u(e+"CollectionConsumer",t);return n.useCallback(()=>{let e=r.collectionRef.current;if(!e)return[];let t=Array.from(e.querySelectorAll("[".concat(d,"]")));return Array.from(r.itemMap.values()).sort((e,r)=>t.indexOf(e.ref.current)-t.indexOf(r.ref.current))},[r.collectionRef,r.itemMap])},l]}},21004:function(e,t,r){r.d(t,{gm:function(){return i}});var n=r(7653);r(27573);var o=n.createContext(void 0);function i(e){let t=n.useContext(o);return e||t||"ltr"}},86705:function(e,t,r){r.d(t,{Ns:function(){return z},fC:function(){return k},gb:function(){return p},l_:function(){return X},q4:function(){return y}});var n=r(7653),o=r(78378),i=r(65622),E=r(99933),l=r(94492),a=r(523),u=r(21004),T=r(81523),c=r(90206),R=r(46196),s=r(27573),d="ScrollArea",[N,_]=(0,E.b)(d),[O,I]=N(d),A=n.forwardRef((e,t)=>{let{__scopeScrollArea:r,type:i="hover",dir:E,scrollHideDelay:a=600,...T}=e,[c,R]=n.useState(null),[d,N]=n.useState(null),[_,I]=n.useState(null),[A,f]=n.useState(null),[S,C]=n.useState(null),[p,D]=n.useState(0),[U,P]=n.useState(0),[L,h]=n.useState(!1),[v,M]=n.useState(!1),w=(0,l.e)(t,e=>R(e)),m=(0,u.gm)(E);return(0,s.jsx)(O,{scope:r,type:i,dir:m,scrollHideDelay:a,scrollArea:c,viewport:d,onViewportChange:N,content:_,onContentChange:I,scrollbarX:A,onScrollbarXChange:f,scrollbarXEnabled:L,onScrollbarXEnabledChange:h,scrollbarY:S,onScrollbarYChange:C,scrollbarYEnabled:v,onScrollbarYEnabledChange:M,onCornerWidthChange:D,onCornerHeightChange:P,children:(0,s.jsx)(o.WV.div,{dir:m,...T,ref:w,style:{position:"relative","--radix-scroll-area-corner-width":p+"px","--radix-scroll-area-corner-height":U+"px",...e.style}})})});A.displayName=d;var f="ScrollAreaViewport",S=n.forwardRef((e,t)=>{let{__scopeScrollArea:r,children:i,nonce:E,...a}=e,u=I(f,r),T=n.useRef(null),c=(0,l.e)(t,T,u.onViewportChange);return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)("style",{dangerouslySetInnerHTML:{__html:"[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}"},nonce:E}),(0,s.jsx)(o.WV.div,{"data-radix-scroll-area-viewport":"",...a,ref:c,style:{overflowX:u.scrollbarXEnabled?"scroll":"hidden",overflowY:u.scrollbarYEnabled?"scroll":"hidden",...e.style},children:(0,s.jsx)("div",{ref:u.onContentChange,style:{minWidth:"100%",display:"table"},children:i})})]})});S.displayName=f;var C="ScrollAreaScrollbar",p=n.forwardRef((e,t)=>{let{forceMount:r,...o}=e,i=I(C,e.__scopeScrollArea),{onScrollbarXEnabledChange:E,onScrollbarYEnabledChange:l}=i,a="horizontal"===e.orientation;return n.useEffect(()=>(a?E(!0):l(!0),()=>{a?E(!1):l(!1)}),[a,E,l]),"hover"===i.type?(0,s.jsx)(D,{...o,ref:t,forceMount:r}):"scroll"===i.type?(0,s.jsx)(U,{...o,ref:t,forceMount:r}):"auto"===i.type?(0,s.jsx)(P,{...o,ref:t,forceMount:r}):"always"===i.type?(0,s.jsx)(L,{...o,ref:t}):null});p.displayName=C;var D=n.forwardRef((e,t)=>{let{forceMount:r,...o}=e,E=I(C,e.__scopeScrollArea),[l,a]=n.useState(!1);return n.useEffect(()=>{let e=E.scrollArea,t=0;if(e){let r=()=>{window.clearTimeout(t),a(!0)},n=()=>{t=window.setTimeout(()=>a(!1),E.scrollHideDelay)};return e.addEventListener("pointerenter",r),e.addEventListener("pointerleave",n),()=>{window.clearTimeout(t),e.removeEventListener("pointerenter",r),e.removeEventListener("pointerleave",n)}}},[E.scrollArea,E.scrollHideDelay]),(0,s.jsx)(i.z,{present:r||l,children:(0,s.jsx)(P,{"data-state":l?"visible":"hidden",...o,ref:t})})}),U=n.forwardRef((e,t)=>{var r,o;let{forceMount:E,...l}=e,a=I(C,e.__scopeScrollArea),u="horizontal"===e.orientation,T=q(()=>d("SCROLL_END"),100),[c,d]=(r="hidden",o={hidden:{SCROLL:"scrolling"},scrolling:{SCROLL_END:"idle",POINTER_ENTER:"interacting"},interacting:{SCROLL:"interacting",POINTER_LEAVE:"idle"},idle:{HIDE:"hidden",SCROLL:"scrolling",POINTER_ENTER:"interacting"}},n.useReducer((e,t)=>{let r=o[e][t];return null!=r?r:e},r));return n.useEffect(()=>{if("idle"===c){let e=window.setTimeout(()=>d("HIDE"),a.scrollHideDelay);return()=>window.clearTimeout(e)}},[c,a.scrollHideDelay,d]),n.useEffect(()=>{let e=a.viewport,t=u?"scrollLeft":"scrollTop";if(e){let r=e[t],n=()=>{let n=e[t];r!==n&&(d("SCROLL"),T()),r=n};return e.addEventListener("scroll",n),()=>e.removeEventListener("scroll",n)}},[a.viewport,u,d,T]),(0,s.jsx)(i.z,{present:E||"hidden"!==c,children:(0,s.jsx)(L,{"data-state":"hidden"===c?"hidden":"visible",...l,ref:t,onPointerEnter:(0,R.M)(e.onPointerEnter,()=>d("POINTER_ENTER")),onPointerLeave:(0,R.M)(e.onPointerLeave,()=>d("POINTER_LEAVE"))})})}),P=n.forwardRef((e,t)=>{let r=I(C,e.__scopeScrollArea),{forceMount:o,...E}=e,[l,a]=n.useState(!1),u="horizontal"===e.orientation,T=q(()=>{if(r.viewport){let e=r.viewport.offsetWidth<r.viewport.scrollWidth,t=r.viewport.offsetHeight<r.viewport.scrollHeight;a(u?e:t)}},10);return j(r.viewport,T),j(r.content,T),(0,s.jsx)(i.z,{present:o||l,children:(0,s.jsx)(L,{"data-state":l?"visible":"hidden",...E,ref:t})})}),L=n.forwardRef((e,t)=>{let{orientation:r="vertical",...o}=e,i=I(C,e.__scopeScrollArea),E=n.useRef(null),l=n.useRef(0),[a,u]=n.useState({content:0,viewport:0,scrollbar:{size:0,paddingStart:0,paddingEnd:0}}),T=G(a.viewport,a.content),c={...o,sizes:a,onSizesChange:u,hasThumb:!!(T>0&&T<1),onThumbChange:e=>E.current=e,onThumbPointerUp:()=>l.current=0,onThumbPointerDown:e=>l.current=e};function R(e,t){return function(e,t,r){let n=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"ltr",o=Q(r),i=t||o/2,E=r.scrollbar.paddingStart+i,l=r.scrollbar.size-r.scrollbar.paddingEnd-(o-i),a=r.content-r.viewport;return B([E,l],"ltr"===n?[0,a]:[-1*a,0])(e)}(e,l.current,a,t)}return"horizontal"===r?(0,s.jsx)(h,{...c,ref:t,onThumbPositionChange:()=>{if(i.viewport&&E.current){let e=W(i.viewport.scrollLeft,a,i.dir);E.current.style.transform="translate3d(".concat(e,"px, 0, 0)")}},onWheelScroll:e=>{i.viewport&&(i.viewport.scrollLeft=e)},onDragScroll:e=>{i.viewport&&(i.viewport.scrollLeft=R(e,i.dir))}}):"vertical"===r?(0,s.jsx)(v,{...c,ref:t,onThumbPositionChange:()=>{if(i.viewport&&E.current){let e=W(i.viewport.scrollTop,a);E.current.style.transform="translate3d(0, ".concat(e,"px, 0)")}},onWheelScroll:e=>{i.viewport&&(i.viewport.scrollTop=e)},onDragScroll:e=>{i.viewport&&(i.viewport.scrollTop=R(e))}}):null}),h=n.forwardRef((e,t)=>{let{sizes:r,onSizesChange:o,...i}=e,E=I(C,e.__scopeScrollArea),[a,u]=n.useState(),T=n.useRef(null),c=(0,l.e)(t,T,E.onScrollbarXChange);return n.useEffect(()=>{T.current&&u(getComputedStyle(T.current))},[T]),(0,s.jsx)(m,{"data-orientation":"horizontal",...i,ref:c,sizes:r,style:{bottom:0,left:"rtl"===E.dir?"var(--radix-scroll-area-corner-width)":0,right:"ltr"===E.dir?"var(--radix-scroll-area-corner-width)":0,"--radix-scroll-area-thumb-width":Q(r)+"px",...e.style},onThumbPointerDown:t=>e.onThumbPointerDown(t.x),onDragScroll:t=>e.onDragScroll(t.x),onWheelScroll:(t,r)=>{if(E.viewport){let n=E.viewport.scrollLeft+t.deltaX;e.onWheelScroll(n),n>0&&n<r&&t.preventDefault()}},onResize:()=>{T.current&&E.viewport&&a&&o({content:E.viewport.scrollWidth,viewport:E.viewport.offsetWidth,scrollbar:{size:T.current.clientWidth,paddingStart:Y(a.paddingLeft),paddingEnd:Y(a.paddingRight)}})}})}),v=n.forwardRef((e,t)=>{let{sizes:r,onSizesChange:o,...i}=e,E=I(C,e.__scopeScrollArea),[a,u]=n.useState(),T=n.useRef(null),c=(0,l.e)(t,T,E.onScrollbarYChange);return n.useEffect(()=>{T.current&&u(getComputedStyle(T.current))},[T]),(0,s.jsx)(m,{"data-orientation":"vertical",...i,ref:c,sizes:r,style:{top:0,right:"ltr"===E.dir?0:void 0,left:"rtl"===E.dir?0:void 0,bottom:"var(--radix-scroll-area-corner-height)","--radix-scroll-area-thumb-height":Q(r)+"px",...e.style},onThumbPointerDown:t=>e.onThumbPointerDown(t.y),onDragScroll:t=>e.onDragScroll(t.y),onWheelScroll:(t,r)=>{if(E.viewport){let n=E.viewport.scrollTop+t.deltaY;e.onWheelScroll(n),n>0&&n<r&&t.preventDefault()}},onResize:()=>{T.current&&E.viewport&&a&&o({content:E.viewport.scrollHeight,viewport:E.viewport.offsetHeight,scrollbar:{size:T.current.clientHeight,paddingStart:Y(a.paddingTop),paddingEnd:Y(a.paddingBottom)}})}})}),[M,w]=N(C),m=n.forwardRef((e,t)=>{let{__scopeScrollArea:r,sizes:i,hasThumb:E,onThumbChange:u,onThumbPointerUp:T,onThumbPointerDown:c,onThumbPositionChange:d,onDragScroll:N,onWheelScroll:_,onResize:O,...A}=e,f=I(C,r),[S,p]=n.useState(null),D=(0,l.e)(t,e=>p(e)),U=n.useRef(null),P=n.useRef(""),L=f.viewport,h=i.content-i.viewport,v=(0,a.W)(_),w=(0,a.W)(d),m=q(O,10);function g(e){U.current&&N({x:e.clientX-U.current.left,y:e.clientY-U.current.top})}return n.useEffect(()=>{let e=e=>{let t=e.target;(null==S?void 0:S.contains(t))&&v(e,h)};return document.addEventListener("wheel",e,{passive:!1}),()=>document.removeEventListener("wheel",e,{passive:!1})},[L,S,h,v]),n.useEffect(w,[i,w]),j(S,m),j(f.content,m),(0,s.jsx)(M,{scope:r,scrollbar:S,hasThumb:E,onThumbChange:(0,a.W)(u),onThumbPointerUp:(0,a.W)(T),onThumbPositionChange:w,onThumbPointerDown:(0,a.W)(c),children:(0,s.jsx)(o.WV.div,{...A,ref:D,style:{position:"absolute",...A.style},onPointerDown:(0,R.M)(e.onPointerDown,e=>{0===e.button&&(e.target.setPointerCapture(e.pointerId),U.current=S.getBoundingClientRect(),P.current=document.body.style.webkitUserSelect,document.body.style.webkitUserSelect="none",f.viewport&&(f.viewport.style.scrollBehavior="auto"),g(e))}),onPointerMove:(0,R.M)(e.onPointerMove,g),onPointerUp:(0,R.M)(e.onPointerUp,e=>{let t=e.target;t.hasPointerCapture(e.pointerId)&&t.releasePointerCapture(e.pointerId),document.body.style.webkitUserSelect=P.current,f.viewport&&(f.viewport.style.scrollBehavior=""),U.current=null})})})}),g="ScrollAreaThumb",y=n.forwardRef((e,t)=>{let{forceMount:r,...n}=e,o=w(g,e.__scopeScrollArea);return(0,s.jsx)(i.z,{present:r||o.hasThumb,children:(0,s.jsx)(b,{ref:t,...n})})}),b=n.forwardRef((e,t)=>{let{__scopeScrollArea:r,style:i,...E}=e,a=I(g,r),u=w(g,r),{onThumbPositionChange:T}=u,c=(0,l.e)(t,e=>u.onThumbChange(e)),d=n.useRef(),N=q(()=>{d.current&&(d.current(),d.current=void 0)},100);return n.useEffect(()=>{let e=a.viewport;if(e){let t=()=>{if(N(),!d.current){let t=V(e,T);d.current=t,T()}};return T(),e.addEventListener("scroll",t),()=>e.removeEventListener("scroll",t)}},[a.viewport,N,T]),(0,s.jsx)(o.WV.div,{"data-state":u.hasThumb?"visible":"hidden",...E,ref:c,style:{width:"var(--radix-scroll-area-thumb-width)",height:"var(--radix-scroll-area-thumb-height)",...i},onPointerDownCapture:(0,R.M)(e.onPointerDownCapture,e=>{let t=e.target.getBoundingClientRect(),r=e.clientX-t.left,n=e.clientY-t.top;u.onThumbPointerDown({x:r,y:n})}),onPointerUp:(0,R.M)(e.onPointerUp,u.onThumbPointerUp)})});y.displayName=g;var F="ScrollAreaCorner",H=n.forwardRef((e,t)=>{let r=I(F,e.__scopeScrollArea),n=!!(r.scrollbarX&&r.scrollbarY);return"scroll"!==r.type&&n?(0,s.jsx)(x,{...e,ref:t}):null});H.displayName=F;var x=n.forwardRef((e,t)=>{let{__scopeScrollArea:r,...i}=e,E=I(F,r),[l,a]=n.useState(0),[u,T]=n.useState(0),c=!!(l&&u);return j(E.scrollbarX,()=>{var e;let t=(null===(e=E.scrollbarX)||void 0===e?void 0:e.offsetHeight)||0;E.onCornerHeightChange(t),T(t)}),j(E.scrollbarY,()=>{var e;let t=(null===(e=E.scrollbarY)||void 0===e?void 0:e.offsetWidth)||0;E.onCornerWidthChange(t),a(t)}),c?(0,s.jsx)(o.WV.div,{...i,ref:t,style:{width:l,height:u,position:"absolute",right:"ltr"===E.dir?0:void 0,left:"rtl"===E.dir?0:void 0,bottom:0,...e.style}}):null});function Y(e){return e?parseInt(e,10):0}function G(e,t){let r=e/t;return isNaN(r)?0:r}function Q(e){let t=G(e.viewport,e.content),r=e.scrollbar.paddingStart+e.scrollbar.paddingEnd;return Math.max((e.scrollbar.size-r)*t,18)}function W(e,t){let r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"ltr",n=Q(t),o=t.scrollbar.paddingStart+t.scrollbar.paddingEnd,i=t.scrollbar.size-o,E=t.content-t.viewport,l=(0,c.u)(e,"ltr"===r?[0,E]:[-1*E,0]);return B([0,E],[0,i-n])(l)}function B(e,t){return r=>{if(e[0]===e[1]||t[0]===t[1])return t[0];let n=(t[1]-t[0])/(e[1]-e[0]);return t[0]+n*(r-e[0])}}var V=function(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:()=>{},r={left:e.scrollLeft,top:e.scrollTop},n=0;return!function o(){let i={left:e.scrollLeft,top:e.scrollTop},E=r.left!==i.left,l=r.top!==i.top;(E||l)&&t(),r=i,n=window.requestAnimationFrame(o)}(),()=>window.cancelAnimationFrame(n)};function q(e,t){let r=(0,a.W)(e),o=n.useRef(0);return n.useEffect(()=>()=>window.clearTimeout(o.current),[]),n.useCallback(()=>{window.clearTimeout(o.current),o.current=window.setTimeout(r,t)},[r,t])}function j(e,t){let r=(0,a.W)(t);(0,T.b)(()=>{let t=0;if(e){let n=new ResizeObserver(()=>{cancelAnimationFrame(t),t=window.requestAnimationFrame(r)});return n.observe(e),()=>{window.cancelAnimationFrame(t),n.unobserve(e)}}},[e,r])}var k=A,X=S,z=H}}]);