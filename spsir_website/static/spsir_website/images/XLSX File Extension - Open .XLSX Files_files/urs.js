$(document).ready(function(){loadRatings();$(".hoverStar").hover(function(){var b=$(this).data("termid");var a=$(this).data("starnum");hoverStarOn(b,a)},function(){var b=$(this).data("termid");var a=$(this).data("starnum");hoverStarOff(b)});$(".userStar").click(function(){var b=$(this).data("starnum"),e=$(this).data("termid");var j="#ratingStar1"+e,h="#ratingStar2"+e,f="#ratingStar3"+e,d="#ratingStar4"+e,c="#ratingStar5"+e,a="#voteWord"+e,g="#voteThanks"+e,l="#voteCount"+e,k="#avgVote"+e,i=TYPE;$(a).html(" Votes");$(".voteStar").hide();$(g).show();if(b==5){$(j).removeClass("fullStar").addClass("userStar");$(h+","+f+","+d+","+c).removeClass("fullStar halfStar emptyStar").addClass("userStar")}else{if(b==4){$(j).removeClass("fullStar").addClass("userStar");$(h+","+f+","+d).removeClass("fullStar halfStar emptyStar").addClass("userStar");$(c).removeClass("fullStar halfStar userStar").addClass("emptyStar")}else{if(b==3){$(j).removeClass("fullStar").addClass("userStar");$(h+","+f).removeClass("fullStar halfStar emptyStar").addClass("userStar");$(d+","+c).removeClass("fullStar halfStar userStar").addClass("emptyStar")}else{if(b==2){$(j).removeClass("fullStar").addClass("userStar");$(h).removeClass("fullStar halfStar emptyStar").addClass("userStar");$(f+","+d+","+c).removeClass("fullStar halfStar userStar").addClass("emptyStar")}else{$(j).removeClass("fullStar").addClass("userStar");$(h+","+f+","+d+","+c).removeClass("fullStar halfStar userStar").addClass("emptyStar")}}}}$(".ratingMsg").hide();$.ajax({type:"POST",url:"/lib/urs_scripts.php",data:{actionType:"vote",termType:i,voteRating:b,termID:e},success:function(o){var n=$.parseJSON(o);var m=n[0];var p=n[1];$(l).html(p);if(i=="e"){$(k).html(m)}else{$(k).html("<b>"+m+"</b> / 5")}}})})});function loadRatings(){var a=new Date().getTime();if(TYPE=="e"){$.post("/lib/urs_scripts.php",{extensions:extArr,termType:TYPE,actionType:"load",safariFix:a},function(j){var r=$.parseJSON(j);var q=extArr.length;for(var k=0;k<q;k++){var o=extArr[k];var f=r[o]["Vote"];if(f!=0){var b=parseFloat(r[o]["Avg"]).toFixed(1);var c=r[o]["Votes"];var m="#ratingStar1"+o;var l="#ratingStar2"+o;var h="#ratingStar3"+o;var g="#ratingStar4"+o;var e="#ratingStar5"+o;var p="#avgVote"+o;var d="#voteCount"+o;var n="#voteWord"+o;$(n).html(" Votes");$(p).html(b);$(d).html(c);if(f==5){$(m).removeClass("fullStar").addClass("userStar");$(l+","+h+","+g+","+e).removeClass("fullStar halfStar emptyStar").addClass("userStar")}else{if(f==4){$(m).removeClass("fullStar").addClass("userStar");$(l+","+h+","+g).removeClass("fullStar halfStar emptyStar").addClass("userStar");$(e).removeClass("fullStar halfStar emptyStar").addClass("emptyStar")}else{if(f==3){$(m).removeClass("fullStar").addClass("userStar");$(l+","+h).removeClass("fullStar halfStar emptyStar").addClass("userStar");$(g+","+e).removeClass("fullStar halfStar emptyStar").addClass("emptyStar")}else{if(f==2){$(m).removeClass("fullStar").addClass("userStar");$(l).removeClass("fullStar halfStar emptyStar").addClass("userStar");$(h+","+g+","+e).removeClass("fullStar halfStar emptyStar").addClass("emptyStar")}else{$(m).removeClass("fullStar").addClass("userStar");$(l+","+h+","+g+","+e).removeClass("fullStar halfStar emptyStar").addClass("emptyStar")}}}}}}})}else{$.post("/lib/urs_scripts.php",{softID:SOFTID,termType:TYPE,actionType:"load",safariFix:a},function(h){var n=$.parseJSON(h);var f=n.Vote;if(f!=0){var b=parseFloat(n.Avg).toFixed(1);var c=n.Votes;var k="#ratingStar1"+SOFTID;var j="#ratingStar2"+SOFTID;var i="#ratingStar3"+SOFTID;var g="#ratingStar4"+SOFTID;var e="#ratingStar5"+SOFTID;var m="#avgVote"+SOFTID;var d="#voteCount"+SOFTID;var l="#voteWord"+SOFTID;$(l).html(" Votes");$(m).html("<b>"+b+"</b> / 5");$(d).html(c);if(f==5){$(k).removeClass("fullStar").addClass("userStar");$(j+","+i+","+g+","+e).removeClass("fullStar halfStar emptyStar").addClass("userStar")}else{if(f==4){$(k).removeClass("fullStar").addClass("userStar");$(j+","+i+","+g).removeClass("fullStar halfStar emptyStar").addClass("userStar");$(e).removeClass("fullStar halfStar emptyStar").addClass("emptyStar")}else{if(f==3){$(k).removeClass("fullStar").addClass("userStar");$(j+","+i).removeClass("fullStar halfStar emptyStar").addClass("userStar");$(g+","+e).removeClass("fullStar halfStar emptyStar").addClass("emptyStar")}else{if(f==2){$(k).removeClass("fullStar").addClass("userStar");$(j).removeClass("fullStar halfStar emptyStar").addClass("userStar");$(i+","+g+","+e).removeClass("fullStar halfStar emptyStar").addClass("emptyStar")}else{$(k).removeClass("fullStar").addClass("userStar");$(j+","+i+","+g+","+e).removeClass("fullStar halfStar emptyStar").addClass("emptyStar")}}}}}})}}function hoverStarOn(b,c){var a=".greyStar"+b;var h=".ratingStar"+b;var j=".userStar"+b;var i="#userStar1"+b;var g="#userStar2"+b;var f="#userStar3"+b;var e="#userStar4"+b;var d="#userStar5"+b;var o="#rateMsg1"+b;var n="#rateMsg2"+b;var m="#rateMsg3"+b;var l="#rateMsg4"+b;var k="#rateMsg5"+b;$(a).show();$(h).hide();$(j).hide();$(".ratingMsg").hide();if(c==1){$(o).show();$(i).show()}else{if(c==2){$(n+","+i+","+g).show()}else{if(c==3){$(m+","+i+","+g+","+f).show()}else{if(c==4){$(l+","+i+","+g+","+f+","+e).show()}else{$(k+","+i+","+g+","+f+","+e+","+d).show()}}}}}function hoverStarOff(a){var c=".greyStar"+a;var d=".ratingStar"+a;var b=".userStar"+a;$(c).hide();$(b).hide();$(d).show();$(".ratingMsg").hide()};