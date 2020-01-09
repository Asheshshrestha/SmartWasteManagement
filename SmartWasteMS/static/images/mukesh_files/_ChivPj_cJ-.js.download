if (self.CavalryLogger) { CavalryLogger.start_js(["shUpY"]); }

__d("ArtilleryReporting",["Artillery","Banzai"],(function(a,b,c,d,e,f){var g="artillery_javascript_trace",h=!1;e.exports.init=function(){if(h)return;h=!0;b("Artillery").addRetroactiveListener("posttrace",function(a){b("Artillery").isEnabled()&&b("Banzai").post(g,a,{retry:!0,delay:10*1e3})})}}),null);