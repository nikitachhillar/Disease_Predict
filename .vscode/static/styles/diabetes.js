
document.addEventListener( 'DOMContentLoaded',function(){
 var searchpara=document.getElementById("search_para").innerHTML;
 searchpara=searchpara.toString();
 document.getElementById("search").onclick =function ()
 {highlight_word(searchpara)};	
},false);

function highlight_word(searchpara)
{
 var text=document.getElementById("search_text").value;
 if(text)
 {
  var pattern=new RegExp("("+text+")", "gi");
  var new_text=searchpara.replace(pattern, "<span class='highlight'>"+text+"</span>");
  document.getElementById("search_para").innerHTML=new_text;
 }
}
