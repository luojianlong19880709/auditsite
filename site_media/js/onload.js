$(document).ready(function(){
	var defaultOptions = Highcharts.setOptions({
         lang: { 
        	 test1Title: 'hour',
             test2Title: 'day',  
             test3Title: 'month',
             shortMonths: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
             rangeSelectorZoom: '',
           // weekdays:['周一','周二','周三','周四','周五','周六','周日']
            weekdays:['周日','周一','周二','周三','周四','周五','周六']
         },
	chart: {
        backgroundColor: {//渐变背景
           linearGradient: {x1:0,y1:0,x2:1,y2:1},
           stops: [
              [0, 'rgb(255, 255, 255)'],
              [1, 'rgb(200, 200, 255)']
           ]
        },
        borderWidth: 2,
        borderRadius: 4,
        plotShadow: true,//plot绘图区域样式
        plotBorderWidth: 1,
        plotBorderColor:"#aaa",
        borderColor:"#b8cfdf"
     },
     colors:['#55BF3B','#ff0066','#ff0bb2','#35abfe','#aa17fe','#ff64eb','#dafc88','#fdd103','#43fddc'],
         global:{
        	 useUTC:false
     }
	/*
         chart: {
             backgroundColor: {//渐变背景
                linearGradient: [0, 0, 0, 100],
                stops: [
                   [0, 'rgb(166, 166, 166)'],
                   [1, 'rgb(96, 96, 96)']
                ]
             },
             borderWidth: 0,
             borderRadius: 5,
             plotShadow: false,//plot绘图区域样式
             plotBorderWidth: 1,
             plotBorderColor:"#444"
          },
         
          title: {//标题样式
             style: { 
                color: '#FFF',
                font: '16px Lucida Grande, Lucida Sans Unicode, Verdana, Arial, Helvetica, sans-serif'
             }
          },
          xAxis: {//x轴样式
             gridLineWidth: 1,
             gridLineColor:"#008040",
             lineWidth: 0,
           //  labels: false,
             tickWidth:0,
             labels:{
             	style:{
             		color:"#fff"
             	}
             },
             title: {
                style: {
                   color: '#fff',
                   font: 'bold 12px Lucida Grande, Lucida Sans Unicode, Verdana, Arial, Helvetica, sans-serif'
                }            
             }
          },
          yAxis: {//y
              gridLineWidth: 1,
           gridLineColor:"#008040",
           lineWidth: 0,
           tickWidth: 0,
           labels: {
              style: {
                 color: '#fff'
              }
           }
          // title:false
        },
        
        plotOptions: {//画图选项
           line: {
              dataLabels: {
                 color: '#CCC'
              },
              marker: {//标记圆点样式
                 radius:2
              },
              lineWidth:1
              // color:"#00ff00"
           },
           area:{
        	   fillColor:"#00ff00"
           }
        },
       
       legend:false,
       global:{
    	   useUTC:false
       }
        */
     });

         
});
function dropIts(){
	//alert($("input[name=min]").val());
	//return true;
	}
	
	function leftAddTime(obj){
return true;
}
function rightAddTime(obj){
return true;
}
 function getTimeBetween(beginId,endId){
  var begin = $("#"+beginId).val();
  var end = $("#"+endId).val();
 var result = new Array();
 result[0]=0;
 result[1]="hour";
 if(begin=="" && end==""){
   return result;
 }else{
   if(begin!=""){
    $("#"+beginId+"hidden").val(begin);
    }
    if(end!=""){
     $("#"+endId+"hidden").val(end);
    }
 }
             begin = begin.replace("-","/").replace("-","/");
             end = end.replace("-","/").replace("-","/");
			 var b=0,e=0;
			 if(begin!=""){
			    b= parseInt(new Date(begin+":00:00").getTime()/1000/60/60/24);
			 }
			 if(end!=""){
			    e= parseInt(new Date(end+":00:00").getTime()/1000/60/60/24);
			 }else{
			    e=parseInt(new Date().getTime()/1000/60/60/24)
			 }
			 var res = parseInt(e-b);
			 if(res<=1){
			    result[0]=3;
			    result[1]="minute";
			 }else if(res>7 && res<60){
			 result[0]=1;
			 result[1]="day";
			 }else if(res>60){
			    result[0]=2;
			 result[1]="month";
			    }
			 return result;
		 }

function getFormatDate(date, dateformat)
{
date = new Date(date);
    if (isNaN(date)) return null;
    var format = dateformat;
    var o = {
        "M+": date.getMonth() + 1,
        "d+": date.getDate(),
        "h+": date.getHours(),
        "m+": date.getMinutes(),
        "s+": date.getSeconds(),
        "q+": Math.floor((date.getMonth() + 3) / 3),
        "S": date.getMilliseconds()
    }
    if (/(y+)/.test(format))
    {
        format = format.replace(RegExp.$1, (date.getFullYear() + "")
    .substr(4 - RegExp.$1.length));
    }
    for (var k in o)
    {
        if (new RegExp("(" + k + ")").test(format))
        {
            format = format.replace(RegExp.$1, RegExp.$1.length == 1 ? o[k]
        : ("00" + o[k]).substr(("" + o[k]).length));
        }
    }
    return format;
}
var dateformat="yyyy-MM-dd hh";
function clickLeftScrollBar(beginId,endId,addOrDis){
 var begin = $("#"+beginId+"hidden").val();
 var end = $("#"+endId+"hidden").val();
 
  begin = begin.replace("-","/").replace("-","/");
  end = end.replace("-","/").replace("-","/");
  var flag=false;
   if(end!=""){
   if(addOrDis=="left"){
   $("#"+endId).val(getFormatDate(new Date(end+":00:00").getTime()-(24*3600*1000),dateformat));
   }else{
  if(parseInt(new Date(end+":00:00").getTime()/1000/60/60/24)-parseInt(new Date().getTime()/1000/60/60/24)==0){
      return false;
    }else{
     $("#"+endId).val(getFormatDate(new Date(end+":00:00").getTime()+(24*3600*1000),dateformat));
   }
   }
   flag=true;
 }
 
  if(begin!=""){
    if(addOrDis=="left"){
    $("#"+beginId).val(getFormatDate(new Date(begin+":00:00").getTime()-(24*3600*1000),dateformat));
    }else{
     $("#"+beginId).val(getFormatDate(new Date(begin+":00:00").getTime()+(24*3600*1000),dateformat));
    }
    flag=true;
  }

 return flag;
}

function addCommas(nStr) {
    nStr += '';
    var x = nStr.split('.');
    var x1 = x[0];
    var x2 = (x.length > 1)?('.' + x[1]): '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
    }

    return x1 + x2;
}



       